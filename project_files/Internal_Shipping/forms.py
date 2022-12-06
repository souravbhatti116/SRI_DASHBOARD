from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, DataRequired


class IntShipForm(FlaskForm):

    intShip_Customer = StringField('Customer')
    intShip_Location = StringField('Location')
    intShip_Product = StringField('Product')
    intShip_QrCode =  StringField('QR Code', validators=[InputRequired(), DataRequired()])
    intShip_Submit = SubmitField('Upload')