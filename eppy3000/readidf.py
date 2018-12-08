# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""read idf json file and have eppy like functionality"""

import json
from munch import DefaultMunch


def readidfjson(fname):
    """read an json idf"""
    as_json = json.load(open(fname, 'r'))
    as_munch = DefaultMunch.fromDict(as_json)
    return as_munch


fname = "./eppy3000/resources/snippets/V8_9/a.epJSON"
idf = readidfjson(fname)
crac = mch.AirLoopHVAC["CRAC system"]
print(crac.branch_list_name)