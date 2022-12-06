# from tkinter.filedialog import askopenfile, askopenfilename

# from app import app, db, InventoryModel
# import pandas as pd
# import os
from project_files.init import db, app
from project_files.models import Inventory214Model, InventoryRfidModel
# file = askopenfilename()
# df = pd.read_csv(file, header=None, index_col=False)
#
# for i in range(len(df)):
#     row = df.loc[i]
#     name = row[0]
#     desc = row[1]
#     loc = row[2]
# #     print(name, desc, loc)

# with app.app_context():
#     db.create_all()

#     item = InventoryRfidModel('AN0001', 'Wifi Ant', 'Molex', 'Devcon')
#     db.session.add(item)
#     db.session.commit()


#######Single DELETE############
# with app.app_context():
#     db.create_all()

#     for i in range(11,55):
#         item = Inventory214Model.query.get(i)
#         db.session.delete(item)
#         db.session.commit()
# #########################


# ####BULK UPLOAD TO DB##########

# with app.app_context():
#     db.create_all()
#     item = InventoryModel.query.get(5)
#     # print(item)
#     item.desc = '4G/3G/2G MONOPOLE TERMINAL ANTENNA'
#     db.session.commit()
#     print(item)
#     file = askopenfilename()
#     df = pd.read_csv(file, header=None, index_col=False)
#
#     for i in range(1,755):
#         row = df.loc[i]
#         name = row[0]
#         desc = row[1]
#         loc = row[2]
#         item = Inventorydb(name, desc, loc)
#         db.session.add(item)
#         db.session.commit()
#
# ###############################