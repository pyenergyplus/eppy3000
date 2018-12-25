# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""read idf json file and have eppy like functionality"""

from io import StringIO
import json
import eppy3000
try:
    from eppy3000.epMunch import EPMunch
except ModuleNotFoundError as e:
    from epMunch import EPMunch
from munch import Munch


def readidfjson(fhandle):
    """read an json idf
    
    Parameters
    ----------
    fhandle: io.String, io.TextIOWrapper
        can be a file open for read or a io.StringIO object

    Returns
    -------
    eppy.EPMunch
    """
    try:
        fhandle = open(fhandle, 'r')
    except TypeError as e:
        pass
    as_json = json.load(fhandle)
    as_munch = EPMunch.fromDict(as_json)
    addeppykeys(as_munch)
    return as_munch
    
def addeppykeys(idfmunch):
    """adds eppykeys needed by eppy3000"""
    for key, val in idfmunch.items():
        for key1, val1 in val.items():
            val1['eppykey'] = key
            val1['eppyname'] = key1
        
def removeeppykeys(idfmunch, rkeys=None):
    """remove the eppykeys"""
    if not rkeys:
        rkeys = ['eppykey', 'eppyname', 'eppy_objidd']
    for key, val in idfmunch.items():
        for key1, val1 in val.items():
            for rkey in rkeys:
                val1.pop(rkey, None)
    

if __name__ == "__main__":
    fname = "./eppy3000/resources/snippets/V8_9/a.epJSON"
    idf = readidfjson(fname)
    crac = idf.AirLoopHVAC["CRAC system"]
    print(crac.branch_list_name)
    txt = """
    {
        "Building": {
            "Bldg": {
                "idf_max_extensible_fields": 0,
                "idf_max_fields": 8,
                "idf_order": 3,
                "loads_convergence_tolerance_value": 0.05,
                "maximum_number_of_warmup_days": 30,
                "minimum_number_of_warmup_days": 6,
                "north_axis": 0.0,
                "solar_distribution": "MinimalShadowing",
                "temperature_convergence_tolerance_value": 0.05,
                "terrain": "Suburbs"
            }
        }
    }
    """
    sio = StringIO(txt)
    idf = readidfjson(sio)
    abuilding = idf.Building.Bldg
    print(abuilding.solar_distribution)
    print(abuilding.terrain)
    print(abuilding)
