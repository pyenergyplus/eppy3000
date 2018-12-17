"""explore the json arrays in epyy3000"""

from io import StringIO
from eppy3000.modelmaker import IDF
from pprint import pprint


txt = """
{
    "BuildingSurface:Detailed": {
        "Zn001:Flr001": {
            "construction_name": "FLOOR",
            "idf_max_extensible_fields": 12,
            "idf_max_fields": 22,
            "idf_order": 27,
            "number_of_vertices": 4,
            "outside_boundary_condition": "Surface",
            "outside_boundary_condition_object": "Zn001:Flr001",
            "sun_exposure": "NoSun",
            "surface_type": "Floor",
            "vertices": [
                {
                    "vertex_x_coordinate": 15.24,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 0.0,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 0.0,
                    "vertex_y_coordinate": 15.24,
                    "vertex_z_coordinate": 0.0
                },
                {
                    "vertex_x_coordinate": 15.24,
                    "vertex_y_coordinate": 15.24,
                    "vertex_z_coordinate": 0.0
                }
            ],
            "view_factor_to_ground": 1.0,
            "wind_exposure": "NoWind",
            "zone_name": "Main Zone"
        }
    }
}"""

fhandle = StringIO(txt)
iddfname = "/Applications/EnergyPlus-8-9-0/Energy+.schema.epJSON"
idf = IDF(idfname=fhandle, iddname=iddfname)
print(idf)


surfs = idf.idfobjects["BuildingSurface:Detailed"]
surf = surfs[0]
print(surf.eppy_objidd.fieldnames())
print(surf.vertices)
print(surf.vertices[0])
print(surf.vertices[0].vertex_x_coordinate)
surf.vertices[0].vertex_x_coordinate = 88
surf.vertices.append(dict(vertex_x_coordinate=1.2,
                        vertex_y_coordinate=2.3,
                        vertex_z_coordinate=3.4))
print(idf)
