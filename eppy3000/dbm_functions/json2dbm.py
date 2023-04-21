# Copyright (c) 2022 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""Functions to create the dbm file for EPJ schema

:Question: Why Store the EPJ Schema in a database (the database is dbm here)
:Response: The EPJ Schema is a large file. The file is about 10 megabytes and only parts of it are used with an EPJ file (a specific model). Storing this in a databse opens up the option of loading only the needed parts of the EPJ schema into memory. With the EPJ schema being less memory intensive, it may be possible to open multple versions of EPJ files and it's corresponding EPJ schema.
"""

import json
import dbm
import dbm.dumb
import sys

try:
    import schemaindbm
except ModuleNotFoundError as e:
    import eppy3000.dbm_functions.schemaindbm as schemaindbm


def create_index(fname, dbmname):
    """create the indices for reference and object_list in the schema dbm

    It creates an index for the dbm created by the ``function create_schemadbm()``. Many EPJObjects in the E+ schema have reference names (apart from their key word name). Fields in other EPJObjects can refer to another EPJObjects using the reference names. Without an index, one would have to search through the entire database to find the EPJObjects being pointed to. The index allows you to quickly find the EPJObject.

    The index is stored as a seperate dbm (from the dbm for the EPJ schema). If the main dbm is named `schema`, by convention, the index dbm is called `schema_ref_index`, although it can be called anything.

    The index is structured in the following way:

    - The keys are the reference names (called reference in the EPJObjects [and in the schema file])
    - So a key:value in the dbm will look like:
    - example for `SurfaceNames`::

        {'SurfaceNames':{'objlist': ['BuildingSurface:Detailed',
                        'Wall:Detailed',
                        'RoofCeiling:Detailed', .... ],
            'reflist': ['FenestrationSurface:Detailed.building_surface_name',
                        'Window.building_surface_name',
                        'Door.building_surface_name',
                        'GlazedDoor.building_surface_name',  .... ]}}

        # 'objlist' -> will give the list of EPJObjects that that are also called 'SurfaceNames'
        # 'reflist' -> list of EPJObjects.Fieldname that refer to 'SurfaceNames'

    Parameters
    ----------
    fname: string, StringIO
        filename of the E+Schema file OR the contents of the E+Schema file in a StringIO
    dbmname: str
        Name of the dbm file. If ``dbmname='schema'``, it will generate ``schema.dir, schema.dat, schema.bak``

    Returns
    -------
    None
    """
    db = schemaindbm.db_in_memory(fname)
    dt = dict()
    for key in db.keys():
        aschema = json.loads(db[key])
        try:
            name = schemaindbm.get_name(key, aschema=aschema)
            refs = name["reference"]
            for ref in refs:
                objlist = dt.setdefault(ref, {"objlist": list()})["objlist"]
                objlist.append(key)
        except (TypeError, KeyError) as e:
            pass

    for key in db.keys():
        aschema = json.loads(db[key])
        name = schemaindbm.get_name(key, aschema=aschema)
        # get object_list from name
        try:
            object_list = name["object_list"]
            for object_item in object_list:
                for object_item in object_list:
                    dt[object_item].setdefault("reflist", list()).append(f"{key}.name")
        except (TypeError, KeyError) as e:
            pass
        fieldnames = schemaindbm.get_props(key, aschema=aschema).keys()
        for fieldname in fieldnames:
            # get object_list from fieldname
            field = schemaindbm.get_field(key, fieldname, aschema=aschema)
            try:
                object_list = field["object_list"]
                for object_item in object_list:
                    dt[object_item].setdefault("reflist", list()).append(
                        f"{key}.{fieldname}"
                    )
            except KeyError as e:
                pass
            # get object_list from field array
            for arrayfieldname in schemaindbm.get_arrayfieldnames(
                key, fieldname, aschema=aschema
            ):
                arrayfield = schemaindbm.get_arrayfield(
                    key, fieldname, arrayfieldname, aschema=aschema
                )
                try:
                    object_list = arrayfield["object_list"]
                    for object_item in object_list:
                        dt[object_item].setdefault("reflist", list()).append(
                            f"{key}.{fieldname}.{arrayfieldname}"
                        )
                except KeyError as e:
                    object_list = list()
    with dbm.dumb.open(dbmname, "c") as thedb:
        for key in dt:
            thedb[key] = json.dumps(dt[key])


def create_schemadbm(fname, dbmname):
    """create the schema dbm

    Python has a built-in key-value database called ``dbm``. This function is used to save the E+Schema in a ``key:value`` format in ``dbm``. The ``key`` is the name of the EPJObject. The ``value`` is a string representation of json value of that EPJObject from the schema file

    dbm.dumb format is used to save the file, since it has greatest cross-platform compatability. The dbm.dumb generates three files (``*.dir, *.dat, *.bak``). So if ``dbmname='schema'``, it will generate ``schema.dir, schema.dat, schema.bak``

    Parameters
    ----------
    fname: string, StringIO
        filename of the E+Schema file OR the contents of the E+Schema file in a StringIO
    dbmname: str
        Name of the dbm file. If ``dbmname='schema'``, it will generate ``schema.dir, schema.dat, schema.bak``

    Returns
    -------
    None
    """
    try:
        d = json.load(open(fname, "r"))
    except TypeError as e:
        d = json.load(fname)
    with dbm.dumb.open(dbmname, "c") as db:
        db["epJSON_schema_version"] = d["epJSON_schema_version"]
        for key in d["properties"]:
            db[key] = json.dumps(d["properties"][key])

def create_groupsindex(fname, dbmname):
    """create the groupindex for the schema"""
    db = schemaindbm.db_in_memory(fname)
    dt = dict()
    for key in db.keys():
        aschema = json.loads(db[key])
        group = aschema["group"]
        dt.setdefault(group, list()).append(key)
    with dbm.dumb.open(dbmname, "c") as db:
        for key in dt:
            db[key] = json.dumps(dt[key])

if __name__ == "__main__":
    sys.argv[1:]
    fname = sys.argv[1]
    dbmname = sys.argv[2]
    create_schemadbm(fname, dbmname)
    create_index(fname, f'{dbmname}_ref_index')
    create_groupsindex(fname, f'{dbmname}_group_index')