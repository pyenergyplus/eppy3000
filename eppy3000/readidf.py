# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""read idf json file and have eppy like functionality"""

from io import StringIO
import json
from munch import DefaultMunch


def readidfjson(fname):
    """read an json idf"""
    if isinstance(fname, StringIO):
        as_json = json.load(fname)
    else:
        as_json = json.load(open(fname, 'r'))
    as_munch = DefaultMunch.fromDict(as_json)
    return as_munch


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
