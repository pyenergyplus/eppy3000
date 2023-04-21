# Copyright (c) 2022 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""explore the schema in the dbm"""

import dbm
import json
import dbm.dumb


def db_in_memory(fname=None):
    """creates the dbm in memory

    Loads the schema file (fname) as a dict. The dict is structured identical to the dbm. Use this when you want fast operations and don't want to use the dbm. right now it is used to creat the index for the dbm
    
    Parameters
    ----------
    fname: string, StringIO
        filename of the E+Schema file OR the contents of the E+Schema file in a StringIO

    Returns
    -------
    dict
        key:value (str:str) where key=EPJOject, value=str from schema file
    """
    if not fname:
        fname = "./eppy3000/resources/schema/V9_3/Energy+.schema.epJSON"
    try:
        d = json.load(open(fname, "r"))
    except TypeError as e:
        d = json.load(fname)
    db = dict()
    for key in d["properties"]:
        db[key] = json.dumps(d["properties"][key])
    return db


def get_schemakeys(fname=None):
    """get all the schema keys
    
    Opens the dbm as D and returns D.keys() -> a set-like object providing a view on D's keys
    
    Parameters
    ----------
    fname: string, StringIO
        filename of the E+Schema file OR the contents of the E+Schema file in a StringIO

    Returns
    -------
    list
        D.keys() -> a set-like object providing a view on D's keys, where D is the dbm
    """
    if fname:
        with dbm.dumb.open(fname, "r") as db:
            return db.keys()
    else:
        with dbm.dumb.open("./schema", "r") as db:
            return db.keys()


def get_schemaversion(fname=None):
    """get the schema version / E+ version
    
    Returns the energyplus version, that is stored in the schema
    
    Parameters
    ----------
    fname: string, StringIO
        filename of the E+Schema file OR the contents of the E+Schema file in a StringIO

    Returns
    -------
    bytes
        returns the version. example: b'9.6.0'
    """
    key = "epJSON_schema_version".encode()
    if fname:
        with dbm.dumb.open(fname, "r") as db:
            # dt = json.loads(db[key])
            return db[key]
    else:
        with dbm.dumb.open("./schema", "r") as db:
            # dt = json.loads(db[key])
            return db[key]


def get_aschema(key, fname=None):
    """gets a schema
    
    Returns the schema of an EPJObject, when key=EPJObject name
    
    Parameters
    ----------
    key: string
        The name of the EPJObject
    fname: string, StringIO
        filename of the E+Schema file OR the contents of the E+Schema file in a StringIO. Default value is './schema'

    Returns
    -------
    dict
        schema of the EPJObject as a dict
    """
    try:
        key = key.encode()
    except AttributeError as e:
        pass
    if fname:
        with dbm.dumb.open(fname, "r") as db:
            dt = json.loads(db[key])
            return dt
    else:
        with dbm.dumb.open("./schema", "r") as db:
            dt = json.loads(db[key])
            return dt


def get_name(key, aschema=None, fname=None):
    """get the attributes of `name` field of the schema
    
    Returns the attributes of the `name` field of the schema as a dict. Returns None if there is no `name` field. Extracts it from the `aschema`, or from `fname`. Using `aschema` if you already have it avoids disk access, by not using fname.
    
    Parameters
    ----------
    key: string
        The name of the EPJObject
    aschema: dict
        this is the schema of EPJObject, extracted using the function `get_aschema`
    fname: string, StringIO
        filename of the E+Schema file OR the contents of the E+Schema file in a StringIO. Default value is './schema'

    Returns
    -------
    dict
        attributes of the `name` field of aschema
    """
    if aschema:
        dt = aschema
    else:
        dt = get_aschema(key, fname=fname)
    try:
        return dt["name"]
    except KeyError as e:
        return None


def get_props(key, aschema=None, fname=None):
    """gets the properties of a schema
    
    Returns fields of the schema as a dict. In the schema file , it is called `properties`. Hence the name `get_props()`. Some of the fileds may have array inside with array fieldnames. The fieldname within the arrays can be extracted using `get_arrayfieldnames()`. 
    
    Extracts the results from the `aschema`, or from `fname`. Using `aschema` if you already have it, avoids disk access, by not using fname.
    
    Parameters
    ----------
    key: string
        The name of the EPJObject
    aschema: dict
        this is the schema of EPJObject, extracted using the function `get_aschema`
    fname: string, StringIO
        filename of the E+Schema file OR the contents of the E+Schema file in a StringIO. Default value is './schema'

    Returns
    -------
    dict
        {fieldname1:dict(), fieldname2:dict()}
    """
    if aschema:
        dt = aschema
    else:
        dt = get_aschema(key, fname=fname)
    # props = dt['patternProperties']['^.*\\S.*$']['properties']
    for pkey in dt["patternProperties"]:
        props = dt["patternProperties"][pkey]["properties"]
        break
    return props


def get_field(key, fieldname, aschema=None, fname=None):
    """get the field of a schema
    if already have aschema, it avoids disk access"""
    dt = get_props(key, aschema=aschema, fname=fname)
    return dt[fieldname]


def get_arrayfieldnames(key, fieldname, aschema=None, fname=None):
    """get the array fieldnames of a field"""
    field = get_field(key, fieldname, aschema=aschema, fname=fname)
    try:
        return [arrayfield for arrayfield in field["items"]["properties"]]
    except KeyError as e:
        return list()


def get_arrayfield(key, fieldname, arrayfieldname, aschema=None, fname=None):
    """get the array field of a field"""
    field = get_field(key, fieldname, aschema=aschema, fname=fname)
    return field["items"]["properties"][arrayfieldname]


def get_a_refschema(key, fname=None):
    """get a reference key from the reference schema"""
    try:
        key = key.encode()
    except AttributeError as e:
        pass
    if fname:
        with dbm.dumb.open(fname, "r") as db:
            dt = json.loads(db[key])
            return dt
    else:
        with dbm.dumb.open("./schema_ref_index", "r") as db:
            dt = json.loads(db[key])
            return dt


def get_refschemakeys(fname=None):
    """get all the ref schema keys"""
    if fname:
        with dbm.dumb.open(fname, "r") as db:
            return db.keys()
    else:
        with dbm.dumb.open("./schema_ref_index", "r") as db:
            return db.keys()

def get_groups(fname=None):
    """get the entire groups index"""
    def inner_get_groups(db):
        return {key:json.loads(db[key]) for key in db}
    if fname:
        with dbm.dumb.open(fname, "r") as db:
            return inner_get_groups(db)
    else:
        with dbm.dumb.open("./schema_group_index", "r") as db:
            return inner_get_groups(db)

if __name__ == "__main__":
    fname = "../eppy3000viewer/schema"

    # epjkey = 'Coil:Cooling:DX:TwoSpeed'
    epjkey = "SimulationControl"
    epjkey = "Building"

    fieldnames = get_props(epjkey, fname=fname).keys()
    aschema = get_aschema(epjkey, fname=fname)
    aschema_keys = list(aschema.keys())

    refschemakeys = get_refschemakeys(fname=f"{fname}_ref_index")
    arefschema = get_a_refschema("SurfaceNames", fname=f"{fname}_ref_index")
    print(arefschema["objlist"])
    print("-" * 8)
    print(arefschema)

    # bkey = key.encode()
    # print(get_aschema(key))
    # fieldname = 'availability_schedule_name'
    # fieldname = 'high_speed_gross_rated_total_cooling_capacity'
    # # print(get_field(key, fieldname))
    # # for fieldname in get_props(key, aschema).keys():
    # #     field = get_field(key, fieldname, aschema)
    # #     try:
    # #         units = field['units']
    # #         print(f'{fieldname} [{units}]')
    # #     except KeyError as e:
    # #         print(f'{fieldname}')
    # # main(bkey)
    # for fieldname in get_props(key, aschema).keys():
    #     field = get_field(key, fieldname)
    #     print('----')
    #     print(key)
    #     pprint.pprint(field)
    # # print(get_schemakeys())
