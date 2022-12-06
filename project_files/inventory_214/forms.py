from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, InputRequired


class InventorySearchForm(FlaskForm):

    keyword = StringField('Keyword')
    datafilter = RadioField('Search From', choices=[('Name', 'Name'), ('Description', 'Description')])
    submit = SubmitField('Search')



class AddInventory(FlaskForm):
    
    name = StringField('Item Name', validators=[DataRequired()])
    desc = StringField('Description', validators=[InputRequired()])
    ven = StringField('Vendor')
    loc = StringField('Location')
    submit = SubmitField('Add Item')


class UpdateInventory(FlaskForm):
    
    name = StringField('Item Name', validators=[DataRequired()])
    desc = StringField('Description', validators=[InputRequired()])
    ven = StringField('Vendor')
    loc = StringField('Location')
    submit = SubmitField('Update Item')