# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""read the idd json as a json"""

import json
from munch import DefaultMunch

# data = json.loads('{"foo":1, "bar": 2}', object_pairs_hook=OrderedDict)
fname = "/Applications/EnergyPlus-8-9-0/Energy+.schema.epJSON"
epjs = json.load(open(fname, 'r')) # 0.079 seconds
# epjs = json.load(open(fname, 'r'), object_pairs_hook=OrderedDict)
prop = epjs[u'properties']

as_munch = DefaultMunch.fromDict(epjs) # 0.410 seconds

# ran profiler on this script
# python -m cProfile eppy3000/readidd.py
# Total time on this script = 0.526 seconds


