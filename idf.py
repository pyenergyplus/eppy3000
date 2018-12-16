"""use the class IDF"""

from eppy3000.modelmaker import IDF
from pprint import pprint

iddfname = "/Applications/EnergyPlus-8-9-0/Energy+.schema.epJSON"
fname = "./eppy3000/resources/snippets/V8_9/a.epJSON"
idf = IDF(idfname=fname, iddname=iddfname)

# pprint(idf.idd.iddobjects['AirLoopHVAC'].fieldproperty('branch_list_name'))
# print(idf.idfobjects['AirLoopHVAC'][0])
# for fname in idf.idd.iddobjects['AirLoopHVAC'].fieldnames():
#     print(fname)
pprint(idf.idd.iddobjects['AirLoopHVAC'].fieldnames())
# print(idf)

# idf.saveas('karamba.txt')
# idfobjects = {key:[val1 for val1 in val.values()] for key, val in idf.idf.items()}