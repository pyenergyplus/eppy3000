"""testing print E+ Munch"""

from munch import Munch
from eppy3000.readidf import readidfjson


def printkey(key, indent=0, format=None, func=None):
    if not func:
        func = print
    if not indent:
        func("")
        func("")
    elif indent == 1:
        func("")
    if not format:
        format = '{}{}'
        func(format.format(' '*4*indent, key))
    else:
        func(format.format(' '*4*indent, key))
        

def printmunch(amunch, indent=0, index=None, func=None):
    if not func:
        func = print
    for key, val in amunch.items():
        if isinstance(val, Munch):
            printkey(key, indent, func=func)
            printmunch(val, indent=indent+1, index=index, func=func)
        elif isinstance(val, list):
            printkey(key, indent=3, format= "{0}" + " " * 36 + " !-  {1}", func=func)
            for i, aval in enumerate(val):
                printmunch(aval, indent=indent+1, index=i+1, func=func)
        else:
            if index:
                astr = '{0}{1: <36} !-  {2} #{3}'
                func(astr.format(' '*4*indent, val, key, index))
            else:
                astr = '{0}{1: <36} !-  {2}'
                func(astr.format(' '*4*indent, val, key))


fname = "./eppy3000/resources/snippets/V8_9/a.epJSON"
idf = readidfjson(fname)

alh = idf.AirLoopHVAC
crac = idf.AirLoopHVAC['CRAC system']
surfs = idf['BuildingSurface:Detailed']
surf = surfs['Zn001:Flr001']

# print(idf)
# print(surf)
# print(alh)
print(surfs)