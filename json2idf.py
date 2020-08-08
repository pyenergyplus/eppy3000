"""convert a json file to idf"""

import json
from io import StringIO

from eppy3000.modelmaker import IDF
from munch import Munch


def readiddasmunch(fhandle):
    """read the idd json as a munch"""
    epjs = json.load(fhandle)
    as_munch = Munch.fromDict(epjs)
    return as_munch


idfjson = """

{

    "BuildingSurface:Detailed": {
        "BACK-1": {
            "construction_name": "WALL-1",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 101,
            "number_of_vertices": 4,
            "outside_boundary_condition": "Outdoors",
            "sun_exposure": "SunExposed",
            "surface_type": "Wall",
            "vertices": [
                {
                    "vertex_x_coordinate": 30.5,
                    "vertex_y_coordinate": 15.2,
                    "vertex_z_coordinate": 2.4
                },
                {
                    "vertex_x_coordinate": 30.5,
                    "vertex_y_coordinate": 15.2,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 15.2,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 15.2,
                    "vertex_z_coordinate": 2.4
                }
            ],
            "view_factor_to_ground": 0.5,
            "wind_exposure": "WindExposed",
            "zone_name": "SPACE3-1"
        }
    },

    "AirLoopHVAC": {
        "VAV Sys 1": {
            "availability_manager_list_name": "VAV Sys 1 Avail List",
            "branch_list_name": "VAV Sys 1 Branches",
            "demand_side_inlet_node_names": "Zone Eq In Node",
            "demand_side_outlet_node_name": "PLENUM-1 Out Node",
            "design_supply_air_flow_rate": "Autosize",
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 10,
            "idf_order": 204,
            "supply_side_inlet_node_name": "VAV Sys 1 Inlet Node",
            "supply_side_outlet_node_names": "VAV Sys 1 Outlet Node"
        }
    },

    "Zone": {
        "Main Zone": {
            "ceiling_height": "Autocalculate",
            "direction_of_relative_north": 0,
            "idf_max_extensible_fields": 0,
            "idf_max_fields": 9,
            "idf_order": 20,
            "multiplier": 1,
            "type": 1,
            "volume": "Autocalculate",
            "x_origin": 0,
            "y_origin": 0,
            "z_origin": 0
        },
        
    "PLENUM-1": {
        "ceiling_height": 0.609600067,
        "direction_of_relative_north": 0,
        "idf_max_extensible_fields": 0,
        "idf_max_fields": 9,
        "idf_order": 58,
        "multiplier": 1,
        "type": 1,
        "volume": 283.2,
        "x_origin": 0,
        "y_origin": 0,
        "z_origin": 0
    }
    
    }
}

"""
# idfjson = """
# {
#     "BuildingSurface:Detailed": {
#         "Zn001:Flr001": {
#             "construction_name": "FLOOR",
#             "idf_max_extensible_fields": 12,
#             "idf_max_fields": 22,
#             "idf_order": 27,
#             "number_of_vertices": 4,
#             "outside_boundary_condition": "Surface",
#             "outside_boundary_condition_object": "Zn001:Flr001",
#             "sun_exposure": "NoSun",
#             "surface_type": "Floor",
#             "vertices": [
#                 {
#                     "vertex_x_coordinate": 15.24,
#                     "vertex_y_coordinate": 0.0,
#                     "vertex_z_coordinate": 0.0
#                 },
#                 {
#                     "vertex_x_coordinate": 0.0,
#                     "vertex_y_coordinate": 0.0,
#                     "vertex_z_coordinate": 0.0
#                 },
#                 {
#                     "vertex_x_coordinate": 0.0,
#                     "vertex_y_coordinate": 15.24,
#                     "vertex_z_coordinate": 0.0
#                 },
#                 {
#                     "vertex_x_coordinate": 15.24,
#                     "vertex_y_coordinate": 15.24,
#                     "vertex_z_coordinate": 0.0
#                 }
#             ],
#             "view_factor_to_ground": 1.0,
#             "wind_exposure": "NoWind",
#             "zone_name": "Main Zone"
#         }
#     }
# }
# """

# fhandle = StringIO(txt)
iddpath = "/Applications/EnergyPlus-9-0-1/Energy+.schema.epJSON"
# fname = "./eppy3000/resources/snippets/V8_9/a.epJSON"
js = readiddasmunch(open(iddpath, "r"))

idfhandle = StringIO(idfjson)
fname = "./eppy3000/resources/snippets/V9_0/5Zone_Unitary_HXAssistedCoil.epJSONout"
idfhandle = open(fname, "r")
idfjs = readiddasmunch(idfhandle)

# idfhandle = StringIO(idfjson)
# idf = IDF(idfname=idfhandle, iddname=iddpath)

# for key in idfjs.keys():
#     print(f"{key},")
#     for name in idfjs[key].keys():
#         fieldnames = js.properties[key].legacy_idd.fields
#         lastfield = len(fieldnames) - 1
#         comma = ","
#         semicolon = ";"
#         sep = comma
#         for i, fieldname in enumerate(fieldnames):
#             if i == lastfield:
#                 sep = semicolon
#             try:
#                 value = idfjs[key][name][fieldname]
#                 print(f"    {value}{sep} !- {fieldname}")
#             except KeyError as e:
#                 if fieldname == 'name':
#                     print(f"    {name}{sep} !- {fieldname}")
#                 else:
#                     value = ""
#                     print(f"    {value}{sep} !- {fieldname}")
#         print()


for key in idfjs.keys():
    # print(f"{key},")
    for name in idfjs[key].keys():
        fieldval = []
        fieldnames = js.properties[key].legacy_idd.fields
        lastfield = len(fieldnames) - 1
        comma = ","
        semicolon = ";"
        sep = comma
        for i, fieldname in enumerate(fieldnames):
            if i == lastfield:
                sep = semicolon
            try:
                value = idfjs[key][name][fieldname]
                # print(f"    {value}{sep} !- {fieldname}")
                fieldval.append((fieldname, value))
            except KeyError as e:
                if fieldname == "name":
                    # print(f"    {name}{sep} !- {fieldname}")
                    fieldval.append((fieldname, name))
                else:
                    value = None
                    # print(f"    {value}{sep} !- {fieldname}")
                    fieldval.append((fieldname, value))

        try:
            extension = js.properties[key].legacy_idd.extension
            extensibles = js.properties[key].legacy_idd.extensibles
            for i, tup in enumerate(idfjs[key][name][extension]):
                for fld in extensibles:
                    fieldval.append((f"{fld} {i + 1}", tup[fld]))
        except AttributeError as e:
            pass
        fieldval = [(fld, val) for fld, val in fieldval if val != None]
        lastfield = len(fieldval) - 1
        sep = comma
        print(f"{key},")
        for i, (fld, val) in enumerate(fieldval):
            if i == lastfield:
                sep = semicolon
            valsep = f"{val}{sep}"
            print(f"    {valsep:<25} !- {fld}")
        print()
