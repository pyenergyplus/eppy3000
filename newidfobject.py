"""make a new idf ofject"""

from io import StringIO
from pprint import pprint

from eppy3000.modelmaker import IDF
from munch import Munch


iddfname = "/Applications/EnergyPlus-8-9-0/Energy+.schema.epJSON"
fname = "./eppy3000/resources/snippets/V8_9/a.epJSON"

idf = IDF(idfname=StringIO("{}"), iddname=iddfname)


# def newidfobject(idf, key, objname):
#     """create a new idf object"""
#     # TODO test for dup name
#     objidd = idf.idd.iddobjects[key]
#     try:
#         idf.idf[key][objname]
#     except KeyError as e:
#         idf.idf[key] = Munch()
#         nobj = idf.idf[key][objname] = Munch()
#     for fieldname in objidd.fieldnames():
#         try:
#             nobj[fieldname] = objidd.fieldproperty(fieldname)['default']
#         except AttributeError as e:
#             nobj[fieldname] = "gumby"
#
#make a newidfobject
key = "Building"
# key = "AirLoopHVAC"
key = "Schedule:Compact"
key = "BuildingSurface:Detailed"
objname = "wall1"
idf.newidfobject(key, objname, defaultvalues=False)

objname = "wall2"
idf.newidfobject(key, objname, defaultvalues=True)
objname = "wall3"
idf.newidfobject(key, objname, defaultvalues=True,
                outside_boundary_condition="Surface",
                vertices=[{'vertex_x_coordinate': 15.24,
                            'vertex_y_coordinate': 0.0,
                            'vertex_z_coordinate': 0.0}])

idf.saveas("n.json")
