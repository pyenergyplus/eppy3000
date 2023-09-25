"""start working with units"""

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
allkeys = ['Building']



for eppykey in allkeys:
    print(eppykey)
    bld = epj.epobjects[eppykey][0]
    # print(bld)




    fnames = [key for key in bld.keys() if not key.startswith('eppy')]
    # fnames = ['loads_convergence_tolerance_value']
    for fname in fnames:
        ipunits = unitsconv.getfield_ipunits(bld, fname)
        siunits = unitsconv.getfieldunits(bld, fname)
        print(fname, siunits)
        # if ipunits:
        #     print(eppykey, fname, siunits, ipunits)

        result = unitsconv.getconvert_factors(bld, fname)
        # if ipunits:
        if result[0] and (not result[-1]):
            print('\t', fname, result)
            if siunits:
                print("\t\t", siunits, ipunits)



