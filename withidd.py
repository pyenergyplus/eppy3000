"""explore eppy3000.idd"""

from io import StringIO
from eppy3000.idd import IDD

# iddfname = "/Applications/EnergyPlus-8-9-0/Energy+.schema.epJSON"
iddfname = "a.json"
txt = """"""


fhandle = StringIO(txt)
fhandle = open("b.json", 'r')
idd = IDD(fhandle)


# print(idd.version)
# print(idd.required)
# print(idd.iddobjects.keys())
#
# print(idd.iddobjects['Building'].keys())
# print()
# print(idd.iddobjects['Building'].fieldproperty('terrain')['type'])
#
# print(idd.idd['properties'][].fieldnames())
# print(idd.idd['properties']['Building'])
# print(idd.iddobjects['Building'].fieldnames())
