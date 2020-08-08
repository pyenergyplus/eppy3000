from eppy3000.readidf import readidfjson
from io import StringIO

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
}
"""


idf = readidfjson(StringIO(txt))
surf = idf["BuildingSurface:Detailed"]["Zn001:Flr001"]
# for key, val in surf.items():
#     try:
#         print("{0: <16} !-  {1}".format(val, key))
#     except TypeError as e:
#         print("    {0: <16} !-  {1}".format("", '-'*8))
#         print("    {0: <16} !-  {1}".format("", key))
#         for i, item in enumerate(surf[key]):
#             for key1, val1 in item.items():
#                 print("    {0: <16} !-  {1} #{2}".format(val1, key1, i + 1))
#         # print('    !- {}'.format('-'*8))
#         print("    {0: <16} !-  {1}".format("", '-'*8))
#
# print('-' * 35)

print(idf)
