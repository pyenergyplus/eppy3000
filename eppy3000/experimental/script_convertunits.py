# Copyright (c) 2023 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""print epj with IP units"""
# run this script from the root folder of eppy3000

import sys

# pathnameto_eppy = 'c:/eppy'
pathnameto_eppy = "./"
sys.path.append(pathnameto_eppy)


import eppy3000.experimental.openidf as openidf
import eppy3000.experimental.unitsconv as unitsconv
import eppy3000.experimental.conversiondata as conversiondata
import eppy3000.experimental.epconversions as epconversions

SPACE4 = "    "

fname = "./eppy3000/resources/epJSON/V9_6/ShopWithPVandBattery.idf"
wfile = "./eppy3000/resources/weatherfiles/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw"

epj = openidf.openidf(fname, wfile)
si, ip = conversiondata.getconversions()

eppykey = "Building"
eppykey = "SizingPeriod:DesignDay"
eppykey = "Fan:VariableVolume"
allkeys = epj.epobjects.keys()
# allkeys = ['Building']
# allkeys = ['Coil:Heating:Water']
# allkeys = ['BuildingSurface:Detailed']
# allkeys = ['SizingPeriod:DesignDay']
# allkeys = ['Schedule:Compact']


for eppykey in allkeys:
    for bld in epj.epobjects[eppykey]:
        print(eppykey)
        print(f"{SPACE4}{bld.eppyname}")

        for fname in bld.epjfieldnames():
            if unitsconv.fieldisarray(bld, fname):
                afields = unitsconv.getarraykeys(bld, fname)
                array_convs = []
                for afield in afields:
                    ipunits = unitsconv.getarrayfield_ipunits(bld, fname, afield)
                    siunits = unitsconv.getarrayfieldunits(bld, fname, afield)
                    conv = unitsconv.getconversiondata(siunits, ipunits)
                    array_convs.append((afield, siunits, ipunits))
                for item in bld[fname]:
                    for afield, siunits, ipunits in array_convs:
                        val = item[afield]
                        newval, ustr = epconversions.convert2ip(
                            val, siunits, ipunits, unitstr=True, wrapin="<X>"
                        )
                        print(f"{SPACE4 * 2}{newval} ! - {afield} {ustr}")
                continue
            ipunits = unitsconv.getfield_ipunits(bld, fname)
            siunits = unitsconv.getfieldunits(bld, fname)

            val = bld[fname]
            newval, ustr = epconversions.convert2ip(
                val, siunits, ipunits, unitstr=True, wrapin="[X]"
            )
            print(f"{SPACE4}{newval} ! - {fname} {ustr}")
        print()
