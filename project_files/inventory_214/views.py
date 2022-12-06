
#project_files >>> inventory_214 >>> views.py

from flask import Blueprint, render_template, redirect, url_for,flash
from project_files.init import db
from project_files.models import Inventory214Model
from project_files.inventory_214.forms import AddInventory, UpdateInventory, InventorySearchForm


inventor214_blueprints = Blueprint('inventory214', __name__, template_folder='templates/inventory_214', static_folder='static')

@inventor214_blueprints.route('/addItem', methods = ["GET", "POST"])
def addItem():

    form = AddInventory()

    if form.validate_on_submit():

        name = form.name.data
        desc = form.desc.data
        ven = form.ven.data
        loc = form.loc.data

        newItem = Inventory214Model(name, desc, ven, loc)

        db.session.add(newItem)
        db.session.commit()

        flash('New Item has been Added Successfully.')

        return redirect(url_for('inventory214.list'))
    
    return render_template('add.html', form=form)



@inventor214_blueprints.route('/updateItem/<id>', methods = ["GET", "POST"])
def updateItem(id):
    itemData = Inventory214Model.query.get(id)
    form = UpdateInventory()



    if form.validate_on_submit():

        itemData.item_name = form.name.data
        itemData.item_desc = form.desc.data
        itemData.item_ven = form.ven.data
        itemData.item_loc = form.loc.data
        
        db.session.commit()


        flash(f'Updated Successfully.')
        return redirect(url_for('inventory214.list'))

    return render_template('update.html', form = form, itemData = itemData)

@inventor214_blueprints.route('/list', methods = ["GET", "POST"])
def list():

    keyword = False

    form = InventorySearchForm()

    if form.validate_on_submit():

        keyword = form.keyword.data
        datafilter = form.datafilter.data

        if keyword == '':
            datalist = Inventory214Model.query.all()

            return render_template('listview.html', keyword=keyword, datalist=datalist, form=form)

        elif keyword != '' and datafilter == 'Name':
            keyword = form.keyword.data
            form.keyword.data = ''
            # datalist = Inventory214Model.query.filter_by(name=keyword).all()
            datalist = Inventory214Model.query.filter(Inventory214Model.item_name.like(f'%{keyword}%')).all()
            return render_template('listview.html', form=form, datalist=datalist)

        elif keyword != '' and datafilter == 'Description':
            keyword = form.keyword.data
            form.keyword.data = ''
            # datalist = Inventory214Model.query.filter_by(desc=keyword).all()
            datalist = Inventory214Model.query.filter(Inventory214Model.item_desc.like(f'%{keyword}%')).all()

            return render_template('listview.html', form=form, datalist=datalist)


    datalist = Inventory214Model.query.all()

    return render_template('listview.html', datalist=datalist, form=form)

@inventor214_blueprints.route('/delete/<id>')
def delete(id):
    itemData = Inventory214Model.query.get(id)
    db.session.delete(itemData)
    db.session.commit()
    flash(f"{itemData} deleted successfully.")
    return redirect(url_for('inventory214.list'))

