"""explore eppy3000.idd"""

from eppy3000.idd import IDD

# iddfname = "/Applications/EnergyPlus-8-9-0/Energy+.schema.epJSON"
iddfname = "a.json"




idd = IDD(iddfname)
# print(idd.version)
# print(idd.required)
# print(idd.iddobjects)

# print(idd.iddobjects['Building'].keys())
# print()
# print(idd.iddobjects['Building'].fieldproperty('terrain')['type'])

# print(idd.idd['properties'][].fieldnames())