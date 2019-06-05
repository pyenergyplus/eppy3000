"""try the idf2json functions"""

from eppy3000 import idfjsonconverter

fname = "eppy3000/resources/snippets/V9_0/5Zone_Unitary_HXAssistedCoil.idf"
jsonname = "eppy3000/resources/snippets/V9_0/5Zone_Unitary_HXAssistedCoil.epJSONout"
iddpath = "/Applications/EnergyPlus-9-0-1/Energy+.schema.epJSON"

idfhandle = open(fname, 'r')
jsonhandle = open(jsonname, 'r')
iddhandle = open(iddpath, 'r')

# astr = idfjsonconverter.idf2json(idfhandle, iddhandle)
outfile = "eppy3000/resources/snippets/V9_0/copy.json"
# open(outfile, 'w').write(astr)

jsonhandle = open(outfile, 'r')
astr = idfjsonconverter.json2idf(jsonhandle, iddhandle)
outfile = "eppy3000/resources/snippets/V9_0/copy.idf"
open(outfile, 'w').write(astr)

# print(astr)

