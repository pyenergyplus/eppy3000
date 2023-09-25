"""print epj with no change in units (so SI units)"""

import eppy3000.experimental.openidf as openidf
import eppy3000.experimental.unitsconv as unitsconv
import eppy3000.experimental.conversiondata as conversiondata

SPACE4 = "    "

fname = "/Applications/EnergyPlus-22-1-0/ExampleFiles/5ZoneAirCooled.idf"
wfile = "/Applications/EnergyPlus-8-9-0/WeatherData/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw "

epj = openidf.openidf(fname, wfile)
si, ip = conversiondata.getconversions()

eppykey = 'Building'
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
                    # conv = unitsconv.getconversiondata(siunits, ipunits)
                    array_convs.append((afield, siunits))
                for item in bld[fname]:
                    for afield, siunits in array_convs:
                        val = item[afield]
                        newval, ustr = unitsconv.do_noconversions(val, siunits)
                        print(f"{SPACE4 * 2}{newval} ! - {afield} {ustr}")
                continue
            ipunits = unitsconv.getfield_ipunits(bld, fname)
            siunits = unitsconv.getfieldunits(bld, fname)

            # result = unitsconv.getconvert_factors(bld, fname)
            # units, conv = result
            newval, ustr = unitsconv.do_noconversions(bld[fname], siunits)
            print(f"{SPACE4}{newval} ! - {fname} {ustr}")
                
        # break
