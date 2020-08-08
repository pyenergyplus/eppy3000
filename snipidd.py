"""make a subset of the idd for easy testing"""

from eppy3000 import readidd

iddfname = "/Applications/EnergyPlus-8-9-0/Energy+.schema.epJSON"
idd = readidd.readiddasmunch(iddfname)

props = idd["properties"]
selectedkeys = ["Building", "OutdoorAir:NodeList", "BuildingSurface:Detailed"]
keys = [key for key in props.keys() if key not in selectedkeys]
for key in keys:
    props.pop(key)
outname = "b.json"
readidd.writeiddjson(idd, outname)
