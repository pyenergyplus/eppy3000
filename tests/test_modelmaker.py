# Copyright (c) 2019 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""py.test for modelmaker"""


from io import StringIO
import json

from eppy3000 import modelmaker
from tests import schemafortesting


def test_EPJ():
    """py.test for EPJ"""
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
    expected = 15.24
    result = modelmaker.EPJ(epjname=StringIO(txt))
    surfs = result.epobjects["BuildingSurface:Detailed"]
    surf = surfs[0]
    assert expected == surf.vertices[0].vertex_x_coordinate

    expected = 15.24
    result = modelmaker.EPJ(epjname=StringIO(txt),
                            epschemaname=schemafortesting.schema_file)
    surfs = result.epobjects["BuildingSurface:Detailed"]
    surf = surfs[0]
    assert expected == surf.vertices[0].vertex_x_coordinate
    # - 
    expected = json.loads(txt)
    epj =  modelmaker.EPJ(epjname=StringIO(txt))
    jsonstr = epj.jsonstr()
    result = json.loads(jsonstr)
    assert result == expected
