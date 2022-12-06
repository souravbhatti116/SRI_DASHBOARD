#__init__.py


import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)   # Initiating flask App

app.config['SECRET_KEY'] = 'shipping'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'trackonomoyData.sqlite')  # Set up the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)
Migrate(app, db)



from project_files.inventory_214.views import inventor214_blueprints 
from project_files.QR_Code_Lookup.views import QrCodeData_blueprints
from project_files.Inventory_RFID.views import inventoryRFID_blueprints
from project_files.Internal_Shipping.views import intShip_blueprints

app.register_blueprint(inventor214_blueprints, url_prefix ='/inventory214')
app.register_blueprint(QrCodeData_blueprints, url_prefix='/QrCodeData')
app.register_blueprint(inventoryRFID_blueprints, url_prefix='/inventoryRFID')
app.register_blueprint(intShip_blueprints, url_prefix= '/intShip')