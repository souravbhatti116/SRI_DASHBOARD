from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import InputRequired, DataRequired


class RFIDSearchForm(FlaskForm):
    keyword = StringField('Keyword')
    datafilter = RadioField('Search From', choices=[('Name', 'Name'), ('Description', 'Description')])
    submit = SubmitField('Search')


class RFIDAddForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired()])
    desc = StringField('Description', validators=[InputRequired()])
    ven = StringField('Vendor')
    loc = StringField('Location')
    submit = SubmitField('Add Item')


class RFIDUpdateForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired()])
    desc = StringField('Description', validators=[InputRequired()])
    ven = StringField('Vendor')
    loc = StringField('Location')
    submit = SubmitField('Add Item')