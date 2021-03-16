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
    if not platform_system:
        platform_system = platform.system()
    if platform_system == "Windows":
        pathstart = "C:/EnergyPlusV"
    elif platform_system == "Linux":
        pathstart = "/usr/local/EnergyPlus-"
    else:
        pathstart = "/Applications/EnergyPlus-"
    return f"{pathstart}{version2folder(version)}"


def schemapath(version, platform_system=None):
    """return the schema path for the Energyplus version"""
    installfolderpath = installfolder(version, platform_system)
    return f"{installfolderpath}/Energy+.schema.epJSON"
