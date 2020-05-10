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


def idf2idj(idf, epjsonhandle):
    """convert idf to json. return a eppy3000.IDF structure"""
    idfhandle = StringIO(idf.idfstr())
    return eppy3000.idfjsonconverter.idf2json(idfhandle, epjsonhandle)
    
    
def epj2idf(epj, epjsonhandle, iddhandle=None):
    """convert json to idf"""
    jsonhandle = epj.savecopy()
    idfstr =  eppy3000.idfjsonconverter.json2idf(jsonhandle, epjsonhandle) 
    return eppy.openidf(StringIO(idfstr), idd=iddhandle)