"""try out epschema functions for dbm"""

from munch import Munch
from eppy3000 import epschema
from eppy3000.modelmaker import EPJ


fname = "./eppy3000/resources/snippets/V9_6/Minimal.epJSON"
dbmname = "../EplusSchema/schema"
epj = EPJ(epjname=fname, schemadbmname=dbmname)

bldg = epj.epobjects['Building'][0]
print(type(bldg))


epjkey = 'Building'
eps = epschema.EPS_FromDBM(epjkey, dbmname)
print(eps.fieldnames())
print(eps.version)
print(eps.fieldproperty('north_axis').toDict())
print(eps.fieldproperty('north_axis').note)

