#project_files >>> inventory_214 >>> views.py
import requests
import json
from flask import Blueprint, render_template, redirect, url_for,flash
from project_files.QR_Code_Lookup.forms import QRSearchForm

QrCodeData_blueprints = Blueprint('QrCodeData', __name__, template_folder='templates/QR_Code_Lookup', static_folder='static')

@QrCodeData_blueprints.route('/qrCodeLookup', methods = ["GET", "POST"])
def qrCodeLookup():
    qrCode = False
    form = QRSearchForm()
    dataDict = False
    status = False
    if form.validate_on_submit():

        qrCode = form.qrCode.data
        form.qrCode.data = ''
        try:  
            url = "http://vmprdate.eastus.cloudapp.azure.com:9000/api/v1/manifest/?qrcode=" + qrCode
            r = requests.get(url)
            rawjson = json.loads(r.text)
            data = rawjson['data']
            dataDict = data[0]

            # comments = data[0]['comment']
            # string = str(comments)
            # listOfString = string.split("|")
            # commentList = listOfString
            return render_template('QrCodeData.html', form=form, qrCode=qrCode, datadict=dataDict)
        except KeyError:
            return redirect(url_for('QrCodeData.qrCodeLookup'))

    return render_template('QrCodeData.html', form = form, qrCode= qrCode)
