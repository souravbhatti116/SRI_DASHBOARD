#MODELS.PY
from project_files.init import app
from project_files.init import db  # db will be set up in __Init__.py  file 

class Inventory214Model(db.Model):

    __tablename__ = 'inventory214'

    item_id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String)
    item_desc = db.Column(db.String)
    item_ven = db.Column(db.String)
    item_loc = db.Column(db.String)

    def __init__(self, item_name, item_desc, item_ven, item_loc) -> None:

        self.item_name = item_name
        self.item_desc = item_desc
        self.item_ven = item_ven
        self.item_loc = item_loc
        
    def __repr__(self) -> str:
        return f"{self.item_id}, {self.item_name}, {self.item_desc}, {self.item_ven}, {self.item_loc} "


class InventoryRfidModel(db.Model):

    __tablename__ = 'inventoryRFID'

    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String)
    item_desc = db.Column(db.String)
    item_ven = db.Column(db.String)
    item_loc = db.Column(db.String)

    def __init__(self, item_name, item_desc, item_ven, item_loc) -> None:

        self.item_name = item_name
        self.item_desc = item_desc
        self.item_ven = item_ven
        self.item_loc = item_loc
        
    def __repr__(self) -> str:
        return f"{self.item_name}, {self.item_desc}, {self.item_ven}, {self.item_loc} "


class IntShipLogModel(db.Model):

    __tablename__ = 'IntShipLogModel'


    id = db.Column(db.Integer, primary_key=True)
    tstamp = db.Column(db.Text)
    customer = db.Column(db.Text)
    location = db.Column(db.Text)
    productName = db.Column(db.Text)
    qrCode = db.Column(db.Text)

    def __init__(self, tstamp, customer, location, productName, qrCode):
        self.tstamp = tstamp
        self.customer = customer
        self.location = location
        self.productName = productName
        self.qrCode = qrCode

    def __repr__(self):
        return f'{self.qrCode} '
