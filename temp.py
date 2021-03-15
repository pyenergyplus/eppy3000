import eppy3000.idfjsonconverter as idfjsonconverter
import eppy3000.installlocation as installlocation
# from eppy3000 import idfjsonconverter, installlocation

flist = "example1.txt"
fnames = open(flist, 'r')

fname = "a.idf"
fname = "/Applications/EnergyPlus-9-3-0/ExampleFiles/Generators.idf"
fname = "Generators.idf"
fnames = [fname, ]

for line in fnames:
    fname = line.strip()
    # print(line.strip())

    # fname = "/Applications/EnergyPlus-9-3-0/ExampleFiles/1ZoneDataCenterCRAC_wApproachTemp.idf"
    with open(fname, 'r') as idfhandle:
        version = idfjsonconverter.getidfversion(idfhandle)

    # print(version)
    schemapath = installlocation.schemapath(version)
    # schemapath =
    # print(schemapath)
    # print(fname)
    # epjtxt = idfjsonconverter.idf2json(open(fname, 'r'), open(schemapath, 'r'))
    # print(epjtxt)



    # fname = "./eppy3000/resources/snippets/V9_3/smallfile.idf"
    # schemapath = "./eppy3000/resources/schema/V9_3/Energy+.schema.epJSON"
    # schemapath = "/Applications/EnergyPlus-9-1-0/Energy+.schema.epJSON"

    idfhandle = open(fname, 'r')
    jsonstr = idfjsonconverter.idf2json(idfhandle, open(schemapath, 'r'))
    print(jsonstr)
