# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""read the idd json as a json"""

import json
from munch import Munch

# fname = "/Applications/EnergyPlus-8-9-0/Energy+.schema.epJSON"
# epjs = json.load(open(fname, 'r')) # 0.079 seconds
# as_munch = Munch.fromDict(epjs) # 0.410 seconds
#
# # ran profiler on this script
# # python -m cProfile eppy3000/readidd.py
# # Total time on this script = 0.526 seconds

def readiddasmunch(fname):
    """read the idd json as a munch"""
    epjs = json.load(open(fname, 'r')) # 0.079 seconds
    as_munch = Munch.fromDict(epjs) # 0.410 seconds
    return as_munch

def writeiddjson(amunch, filename):
    """write the idd as json"""
    with open(filename, 'w') as fhandle:
        tosave = amunch.toDict()
        tosave = Munch.fromDict(tosave)
        fhandle.write(tosave.toJSON(indent=4))
    

