"""print epj with IP units"""

import eppy3000.experimental.openidf as openidf
import eppy3000.experimental.unitsconv as unitsconv
import eppy3000.experimental.conversiondata as conversiondata
import eppy3000.experimental.epconversions as epconversions

SPACE4 = "    "

fname = "/Applications/EnergyPlus-22-1-0/ExampleFiles/5ZoneAirCooled.idf"
wfile = "/Applications/EnergyPlus-8-9-0/WeatherData/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw "

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
                    array_convs.append((afield, conv))
                for item in bld[fname]:
                    for afield, conv in array_convs:
                        val = item[afield]
                        newval, ustr = unitsconv.do_conversions(val, conv)
                        print(f"{SPACE4 * 2}{newval} ! - {afield} {ustr}")
                continue
            ipunits = unitsconv.getfield_ipunits(bld, fname)
            siunits = unitsconv.getfieldunits(bld, fname)

            #             result = unitsconv.getconvert_factors(bld, fname)
            #             units, conv = result
            val = bld[fname]
            newval, ustr = epconversions.convert2ip(
                val, siunits, ipunits, unitstr=True, wrapin="[X]"
            )
            #             newval, ustr = unitsconv.do_conversions(bld[fname], conv)
            print(f"{SPACE4}{newval} ! - {fname} {ustr}")

#         break
