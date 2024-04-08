"""Sce the schema in dbm"""


from eppy3000.dbm_functions import json2dbm

fname = "/Applications/EnergyPlus-9-6-0/Energy+.schema.epJSON"
dbmname = "../EplusSchema/schema"
json2dbm.createall(fname, dbmname)
