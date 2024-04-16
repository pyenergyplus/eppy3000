"""try out epschema functions for dbm"""

from munch import Munch
from eppy3000 import epschema
from eppy3000.modelmaker import EPJ


fname = "./eppy3000/resources/snippets/V9_6/Minimal.epJSON"
dbmname = "../EplusSchema/schema"
epj = EPJ(epjname=fname, schemadbmname=dbmname)

bldg = epj.epobjects['Building'][0]
print(type(bldg))


bldg.eppydbm()
