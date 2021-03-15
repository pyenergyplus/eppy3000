"""convert epjson to idf for eplus 9.3"""

import eppy3000.idfjsonconverter as idfjsonconverter
import eppy3000.installlocation as installlocation

schemapath = "/Applications/EnergyPlus-9-3-0/Energy+.schema.epJSON"
fname = "g_eppy3000.epJSON"
# fname = "Generators.epJSON"


jsonhandle = open(fname, 'r')
epjsonhandle = open(schemapath, 'r')
idfstr = idfjsonconverter.json2idf(jsonhandle, epjsonhandle)
print(idfstr)