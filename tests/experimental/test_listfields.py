"""py.test for listfields"""

import pytest
from io import StringIO

from eppy3000.experimental import listfields
from eppy3000.modelmaker import EPJ


@pytest.mark.parametrize(
    "surfobjecttxt, expected",
    [
        (
            """{ "BuildingSurface:Detailed": {
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
                    "vertex_x_coordinate": 1,
                    "vertex_y_coordinate": 2,
                    "vertex_z_coordinate": 3
                }
            ],
            "view_factor_to_ground": 0.5,
            "wind_exposure": "WindExposed",
            "zone_name": "SPACE3-1"
        }
}
}""",
            [(30.5, 15.2, 2.4), (1, 2, 3)],
        ),  # surfobjecttxt, expected
    ],
)
def test_surf2list(surfobjecttxt, expected):
    """py.test for surf2list"""
    epj = EPJ(StringIO(surfobjecttxt))
    surfs = epj.epobjects["BuildingSurface:Detailed"]
    surfobject = surfs[0]
    result = listfields.surf2list(surfobject)
    assert result == expected
