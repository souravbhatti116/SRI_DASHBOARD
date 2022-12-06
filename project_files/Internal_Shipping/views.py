from datetime import *
import json
import requests
from project_files.init import db
from flask import Blueprint, render_template, redirect, url_for
from project_files.Internal_Shipping.forms import IntShipForm
from project_files.models import IntShipLogModel


intShip_blueprints = Blueprint('intShip', __name__, template_folder='templates/Internal_Shipping')


@intShip_blueprints.route('/internalShipping', methods = ['GET', 'POST'])
def internalShipping():

    qrCode  = False 
    form = IntShipForm()

    if form.validate_on_submit():
        tstamp = str(datetime.now().strftime("%Y-%m-%d"))
        customer = form.intShip_Customer.data
        location = form.intShip_Location.data
        product = form.intShip_Product.data
        qrCode = form.intShip_QrCode.data

        form.intShip_QrCode.data = ""
    
        try:

            Look_up_url = "http://vmprdate.eastus.cloudapp.azure.com:9000/api/v1/manifest/?qrcode=" + qrCode
            response = requests.get(Look_up_url)
            rawjson = json.loads(response.text)
            dictData = rawjson['data']
            data = dictData[0]['qrcode']
        except KeyError:
            return "<h1> No Data Found <h1>"

        if data == qrCode:
            upload_url = f"http://vmprdshipapp.eastus2.cloudapp.azure.com:8080/upload?qrcode={qrCode}&customer={customer}&customer_location={location}&ship_date={tstamp}&color={product}&trackonomy_shipping_number=test&po_text=None&engineering=None"
            response = requests.get(upload_url, timeout=5)

            addIntShipLog = IntShipLogModel(tstamp = tstamp, customer = customer, productName= product, location=location, qrCode=qrCode)
            db.session.add(addIntShipLog)
            db.session.commit()
            form.intShip_QrCode.data = ""
            status = "Uploaded Successfully."
            return render_template('IntshipForm.html', form = form, qrCode= qrCode, status = status)
        

            # url = "http://vmprdate.eastus.cloudapp.azure.com:9000/api/v1/manifest/?qrcode=" + qrCode
            # response = requests.get(url)
            # rawjson = json.loads(response.text)
            # dictData = rawjson['data'] 

            # return render_template('IntshipForm.html', form = form, qrCode = qrCode,  dictData = dictData)
            


    return render_template('IntshipForm.html', form = form)



@intShip_blueprints.route('/intShipLog/<int:pageNum>', methods = ['GET', 'POST'])
def intShipLog(pageNum):


    
    log = IntShipLogModel.query.paginate(page = pageNum, per_page=20, error_out = True)

  
    
    return render_template("intShipLog.html", log=log)


@intShip_blueprints.route('/intShipDetails/<qrCode>')
def intShipDetails(qrCode):

    url = "http://vmprdate.eastus.cloudapp.azure.com:9000/api/v1/manifest/?qrcode=" + qrCode
    r = requests.get(url)
    rawjson = json.loads(r.text)
    data = rawjson['data']
    dataDict = data[0]
    return render_template('intShipDetails.html', datadict=dataDict)