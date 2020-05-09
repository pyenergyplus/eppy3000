# Copyright (c) 2020 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""convertion functions - to convert from JSON to IDF and in reverse.
These functions return a epyy.IDF or eppy300.IDF structure"""

from io import StringIO
import eppy3000
import eppy3000.idfjsonconverter
# - 
import eppy
from eppy import modeleditor
from eppy.modeleditor import IDF


def idf2json(idfhandle, epjsonhandle):
    """convert iidf to json. return a eppy3000.IDF structure"""
    return eppy3000.idfjsonconverter.idf2json(idfhandle, epjsonhandle)
    
    
def json2idf(jsonhandle, epjsonhandle, iddhandle=None):
    """convert json to idf"""
    print('in function:', iddhandle)
    idfstr =  eppy3000.idfjsonconverter.json2idf(jsonhandle, epjsonhandle) 
    if iddhandle:
        return eppy.openidf(StringIO(idfstr), idd=iddhandle)
        # IDF.setiddname(iddhandle)
        # return IDF(StringIO(idfstr))
    return eppy.openidf(StringIO(idfstr))
