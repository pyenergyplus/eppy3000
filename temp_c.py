"""try out epschema functions for dbm"""

from munch import Munch
from eppy3000 import epschema
from eppy3000.dbm_functions import schemaindbm

fname = "../EplusSchema/schema"
epjkey = 'Building'
dct = schemaindbm.get_aschema(epjkey, fname)
eps = epschema.EPS_FromDBM(epjkey, fname)
# print(eps)
print(eps.fieldnames())
print(eps.version)
print(eps.fieldproperty('north_axis').toDict())
print(eps.fieldproperty('north_axis').note)

