# Copyright (c) 2020 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""convertion functions - to convert from JSON to IDF and in reverse.
These functions return a eppy.IDF or eppy3000.EPJ structure"""


class NeedsEppyError(Exception):
    pass


try:
    import eppy
except ModuleNotFoundError as e:
    raise NeedsEppyError("you need to install eppy to run these functions")


from io import StringIO
import eppy3000
from eppy3000.modelmaker import EPJ
import eppy3000.idfjsonconverter

# -
from eppy import modeleditor
from eppy.modeleditor import IDF


def idf2epj(idf, epjsonhandle):
    """convert idf to json. return a eppy3000.IDF structure"""
    idfhandle = StringIO(idf.idfstr())
    epjstr = eppy3000.idfjsonconverter.idf2json(idfhandle, epjsonhandle)
    epjsonhandle.seek(0)  # need to reset, since we are reading it again
    return EPJ(StringIO(epjstr), epw=idf.epw, epschemaname=epjsonhandle)


def epj2idf(epj, epjsonhandle, iddhandle=None):
    """convert json to idf"""
    jsonhandle = epj.savecopy()
    idfstr = eppy3000.idfjsonconverter.json2idf(jsonhandle, epjsonhandle)
    return eppy.openidf(StringIO(idfstr), idd=iddhandle, epw=epj.epw)
