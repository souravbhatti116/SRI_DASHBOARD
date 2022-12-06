from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import InputRequired


class QRSearchForm(FlaskForm):

    qrCode = StringField('QR Code', validators=[InputRequired()])
    submit = SubmitField('Search')



