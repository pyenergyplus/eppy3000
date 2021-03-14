# Copyright (c) 2021 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""functions to find the installation folder of a Energyplus version"""

import platform

def version2folder(version):
    """foldername from version"""
    verlst = version.split(".")
    while len(verlst) < 3:
        verlst.append("0")
    return "-".join(verlst)

def installfolder(version, platform_system=None):
    """return the install folder of this EnergyPlus version"""
    pass