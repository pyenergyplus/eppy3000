# Copyright (c) 2018-2019 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""class for the epschema file"""

import json
from munch import Munch


def read_epschema_asmunch(fhandle):
    """read the epschema json as a munch"""
    try:
        epjs = json.load(fhandle)
        as_munch = EPSchemaMunch.fromDict(epjs)
    except AttributeError as e:
        try:
            fhandle = open(fhandle, "r")
            epjs = json.load(fhandle)
            as_munch = EPSchemaMunch.fromDict(epjs)
        except TypeError as e:
            if isinstance(fhandle, EPSchemaMunch):
                return fhandle
            else:
                raise TypeError(
                    f"expected str, bytes, os.PathLike object or Munch, not {type(fhandle)}"
                )  # noqa: E501
    return as_munch


class EPSchemaMunch(Munch):
    """Munch subcalssed to for the EPSchema json"""

    def __init__(self, *args, **kwargs):
        super(EPSchemaMunch, self).__init__(*args, **kwargs)

    def fieldnames(self):
        """field names of the EPSchema object"""
        return [key for key in self.keys()]

    def fieldnames_list(self):
        """fieldnames that contain lists"""
        pass

    def fieldproperty(self, fieldname):
        """field names of the EPSchema object"""
        return self[fieldname]


class EPSchema(object):
    """hold the data from the json epschema file"""

    def __init__(self, epschemaname):
        super(EPSchema, self).__init__()
        self.epschemaname = epschemaname
        self.read()

    def read(self):
        """read the json file"""

        def prop_in_patternProp(val):
            """return the property in patternProperty"""
            # assume that val['patternProperties'] has a single key, val
            # key is either ".*" or "^.*\\S.*$"
            for key in val["patternProperties"].keys():
                return val["patternProperties"][key]

        self.epschema = read_epschema_asmunch(self.epschemaname)
        self.version = self.epschema["epJSON_schema_version"]
        self.required = self.epschema["required"]
        # self.epschemaobjects = {key: val['patternProperties']['.*']['properties']
        #                    for key, val in self.epschema['properties'].items()}
        # the above line stopped working in E+ V9.3. ".*" stopped being the only key
        # workaround is below
        self.epschemaobjects = {
            key: prop_in_patternProp(val)["properties"]
            for key, val in self.epschema["properties"].items()
        }
