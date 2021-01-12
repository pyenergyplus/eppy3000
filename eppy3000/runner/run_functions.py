# Copyright (c) 2021 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""Run functions for EnergyPlus.
"""

import eppy3000.oldeppy as oldeppy

def run(epj, **runoptions):
    """docstring for run"""
    idf = oldeppy.epj2idf(epj, open(epj.epschemaname, 'r'))
    idf.run(**runoptions)
    