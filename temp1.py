"""print epj with SI units"""

import eppy3000.experimental.openidf as openidf
import eppy3000.experimental.unitsconv as unitsconv
import eppy3000.experimental.conversiondata as conversiondata

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
allkeys = ['Connector:Mixer']
allkeys = ['BuildingSurface:Detailed']


for eppykey in allkeys:
    bld = epj.epobjects[eppykey][0]
    for bld in epj.epobjects[eppykey][:1]:
        print(eppykey)
        print("\t", bld.eppyname)




        fnames = [key for key in bld.keys() if not key.startswith('eppy')]
        for fname in fnames:
            ipunits = unitsconv.getfield_ipunits(bld, fname)
            siunits = unitsconv.getfieldunits(bld, fname)

            result = unitsconv.getconvert_factors(bld, fname)
            units, conv = result
            if units:
                ustr = units
                val = bld[fname]
                if isinstance(val, list):
                    for item in val:
                        print(f"\t\t {item} {type(item)}")
                else:
                    print(f"\t {val} [{ustr}] {type(val)}")
            else:
                ustr = ""
                val = bld[fname]
                if isinstance(val, list):
                    for item in val:
                        print(f"\t\t {item} {type(item)}")
                else:
                    print(f"\t {val} {type(val)}")
