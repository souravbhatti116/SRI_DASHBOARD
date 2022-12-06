#project_files >>> inventory_RFID >>> views.py

from flask import Flask, Blueprint, redirect, render_template, url_for, flash
from project_files.init import db
from project_files.models import InventoryRfidModel
from project_files.Inventory_RFID.forms import RFIDAddForm, RFIDUpdateForm, RFIDSearchForm


inventoryRFID_blueprints = Blueprint('inventoryRFID', __name__, template_folder ='templates/Inventory_RFID')


@inventoryRFID_blueprints.route('/addRFID', methods=['GET', 'POST'])
def addRFID():

    form = RFIDAddForm()
    if form.validate_on_submit():
            
        name = form.name.data
        desc = form.desc.data
        ven = form.ven.data
        loc = form.loc.data

        newItem = InventoryRfidModel(name, desc, ven, loc)

        db.session.add(newItem)
        db.session.commit()

        flash('New Item has been Added Successfully.')

        return redirect(url_for('inventoryRFID.listRFID'))

    return render_template('addRFID.html', form=form)

@inventoryRFID_blueprints.route('/updateRFID/<id>', methods=["GET", "POST"])   
def updateRFID(id):
    itemData = InventoryRfidModel.query.get(id)
    form = RFIDUpdateForm()

    if form.validate_on_submit():

        itemData.item_name = form.name.data
        itemData.item_desc = form.desc.data
        itemData.item_ven = form.ven.data
        itemData.item_loc = form.loc.data

        db.session.commit()
        flash('Updated Successfully.')
        return redirect(url_for('inventoryRFID.listRFID'))

    return render_template('updateRFID.html', form = form, itemData = itemData)





@inventoryRFID_blueprints.route('/listRFID', methods=["GET", "POST"])
def listRFID():

    keyword = False

    form = RFIDSearchForm()

    if form.validate_on_submit():

        keyword = form.keyword.data
        datafilter = form.datafilter.data

        keyword = form.keyword.data
        datafilter = form.datafilter.data

        if keyword == '':
            datalist = InventoryRfidModel.query.all()

            return render_template('listviewRFID.html', keyword=keyword, datalist=datalist, form=form)

        elif keyword != '' and datafilter == 'Name':
            keyword = form.keyword.data
            form.keyword.data = ''
            # datalist = Inventory214Model.query.filter_by(name=keyword).all()
            datalist = InventoryRfidModel.query.filter(InventoryRfidModel.item_name.like(f'%{keyword}%')).all()
            return render_template('listviewRFID.html', form=form, datalist=datalist)

        elif keyword != '' and datafilter == 'Description':
            keyword = form.keyword.data
            form.keyword.data = ''
            # datalist = Inventory214Model.query.filter_by(desc=keyword).all()
            datalist = InventoryRfidModel.query.filter(InventoryRfidModel.item_desc.like(f'%{keyword}%')).all()

            return render_template('listviewRFID.html', form=form, datalist=datalist)

    datalist = InventoryRfidModel.query.all()

    return render_template('listviewRFID.html', datalist= datalist, form=form)



@inventoryRFID_blueprints.route('/deleteRFID/<id>')
def deleteRFID(id):
    itemData = InventoryRfidModel.query.get(id)
    db.session.delete(itemData)
    db.session.commit()
    flash(f"{itemData} deleted successfully.")
    return redirect(url_for('inventoryRFID.listRFID'))

