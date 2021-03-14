# Copyright (c) 2021 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""Run functions for EnergyPlus.
"""

import eppy3000.idfjsonconverter
import eppy
from io import StringIO


def epj2idf(epj, epjsonhandle, iddhandle=None):
    """convert json to idf"""
    jsonhandle = epj.savecopy()
    idfstr = eppy3000.idfjsonconverter.json2idf(jsonhandle, epjsonhandle)
    return eppy.openidf(StringIO(idfstr), idd=iddhandle, epw=epj.epw)


def run(epj, **runoptions):
    """docstring for run"""
    idf = epj2idf(epj, open(epj.epschemaname, "r"))
    idf.run(**runoptions)
