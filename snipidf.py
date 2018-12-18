"""snip a single object in the idf"""


from io import StringIO
from eppy3000.modelmaker import IDF
from pprint import pprint

iddfname = "/Applications/EnergyPlus-8-9-0/Energy+.schema.epJSON"
fname = "./eppy3000/resources/snippets/V8_9/a.epJSON"

idf = IDF(idfname=fname, iddname=iddfname)

selectedkey = "BuildingSurface:Detailed"
objname = "Zn001:Flr001"
keys = [key for key in idf.idf.keys() if key != selectedkey]
for key in keys:
    idf.idf.pop(key)
surfs = idf.idf[selectedkey]
keys = [key for key in surfs.keys() if key != objname]
for key in keys:
    surfs.pop(key)
print(idf)    
outname = "a.json"
idf.saveas(outname, indent=4)
