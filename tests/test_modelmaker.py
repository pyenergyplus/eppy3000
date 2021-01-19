# Copyright (c) 2019-2020 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""py.test for modelmaker"""


from io import StringIO
import json
import pytest

from eppy3000 import modelmaker
from tests import schemafortesting


@pytest.fixture
def version_txt():
    """txt of version"""
    txt = """{
    "Version": {
        "Version 1": {
            "version_identifier": "9.3",
            "idf_order": 1
        }
    },
    "SimulationControl": {},
    "Building": {},
    "Site:Location": {}
}

    """
    return txt


@pytest.fixture
def epj_txt1():
    """fixture for first epj"""
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
    return txt


def test_EPJ(epj_txt1):
    """py.test for EPJ"""
    # test without epschema
    txt = epj_txt1
    expected = 15.24
    result = modelmaker.EPJ(epjname=StringIO(txt))
    surfs = result.epobjects["BuildingSurface:Detailed"]
    surf = surfs[0]
    assert expected == surf.vertices[0].vertex_x_coordinate

    # test with epschema
    expected = 15.24
    result = modelmaker.EPJ(
        epjname=StringIO(txt), epschemaname=schemafortesting.schema_file
    )
    surfs = result.epobjects["BuildingSurface:Detailed"]
    surf = surfs[0]
    assert expected == surf.vertices[0].vertex_x_coordinate

    # test jsonstr()
    expected = json.loads(txt)
    epj = modelmaker.EPJ(epjname=StringIO(txt))
    jsonstr = epj.jsonstr()
    result = json.loads(jsonstr)
    assert result == expected


def test_EPJ_repr_(version_txt):
    """pytest for __repr__ in EPJ"""
    expected = """
Version                                          !-  EP_KEY         # use .eppykey
            Version 1                            !-  EPJOBJECT_NAME # use .eppyname
            9.3                                  !-  version_identifier
            1                                    !-  idf_order"""
    epj = modelmaker.EPJ(epjname=StringIO(version_txt))
    assert expected == epj.__repr__()
