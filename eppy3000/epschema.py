# Copyright (c) 2018-2019, 2024 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""class for the epschema file"""

import json
from munch import Munch
from eppy3000.dbm_functions import schemaindbm


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


def prop_in_patternProp(val):
    """return the property in patternProperty"""
    # assume that val['patternProperties'] has a single key, val
    # key is either ".*" or "^.*\\S.*$"
    for key in val["patternProperties"].keys():
        return val["patternProperties"][key]

class EPSchema(object):
    """hold the data from the json epschema file"""

    def __init__(self, epschemaname):
        super(EPSchema, self).__init__()
        self.epschemaname = epschemaname
        self.read()

    def read(self):
        """read the json file from self.epschemaname

        Initailizes the following:

            - self.epschema
            - self.version
            - self.required
            - self.epschemaobjects  
        """

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

# ===============================================================
# functions below are to deal with schema in dbm (using json2dbm)
# ===============================================================

class EPSchema_FromDBM(Munch):
    def __init__(self, epjkey, dbmname):
        super(EPSchema_FromDBM, self).__init__(
            Munch.fromDict(schemaindbm.get_aschema(epjkey, dbmname))
        )
        self.dbmname = dbmname
        self.epjkey = epjkey
        self.version = schemaindbm.get_schemaversion(dbmname)

    def fieldnames(self):
        return list(schemaindbm.get_props(self.epjkey, aschema=self).keys())

    def fieldproperty(self, fieldname):
        return schemaindbm.get_field(self.epjkey, fieldname, aschema=self)
