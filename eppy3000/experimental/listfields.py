# Copyright (c) 2020 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""functions to work with list fields"""


def surf2list(surfobject):
    """return a list of xyz coords from the epobject"""
    vertices = surfobject["vertices"]
    return [
        (
            vrt["vertex_x_coordinate"],
            vrt["vertex_y_coordinate"],
            vrt["vertex_z_coordinate"],
        )
        for vrt in vertices
    ]
