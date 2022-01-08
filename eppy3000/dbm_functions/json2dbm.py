# Copyright (c) 2022 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""create the dbm file for EPJ schema"""

import json
import dbm
import dbm.dumb
import sys

try:
    import schemaindbm
except ModuleNotFoundError as e:
    import eppy3000.dbm_functions.schemaindbm as schemaindbm
    

def create_index(fname, dbmname):
    """create the indices for reference and object_list"""
    db = schemaindbm.db_in_memory(fname)
    dt = dict()
    for key in db.keys():
        aschema = json.loads(db[key])
        try:
            name = schemaindbm.get_name(key, aschema=aschema)
            refs = name['reference']
            for ref in refs:
                objlist = dt.setdefault(ref, {'objlist':list()})['objlist']
                objlist.append(key)
        except (TypeError, KeyError) as e:
            pass

    for key in db.keys():
        aschema = json.loads(db[key])
        name = schemaindbm.get_name(key, aschema=aschema)
        # get object_list from name
        try:
            object_list = name['object_list']
            for object_item in object_list:
                for object_item in object_list:
                    dt[object_item].setdefault('reflist', list()).append(f'{key}.name')
        except (TypeError, KeyError) as e:
            pass
        fieldnames = schemaindbm.get_props(key, aschema=aschema).keys()
        for fieldname in fieldnames:
            # get object_list from fieldname
            field = schemaindbm.get_field(key, fieldname, aschema=aschema)
            try:
                object_list = field['object_list']
                for object_item in object_list:
                    dt[object_item].setdefault('reflist', list()).append(f'{key}.{fieldname}')
            except KeyError as e:
                pass
            # get object_list from field array
            for arrayfieldname in schemaindbm.get_arrayfieldnames(key, fieldname, aschema=aschema):
                arrayfield = schemaindbm.get_arrayfield(key, fieldname, arrayfieldname, aschema=aschema)
                try:
                    object_list = arrayfield['object_list']
                    for object_item in object_list:
                        dt[object_item].setdefault('reflist', list()).append(f'{key}.{fieldname}.{arrayfieldname}')
                except KeyError as e:
                    object_list = list()
    with dbm.dumb.open(dbmname, 'c') as thedb:
        for key in dt:
            thedb[key] = json.dumps(dt[key])

def create_schemadbm(fname, dbmname):
    """create the schema dbm

    Python has a huilt-in key-value database called dbm. This function is used to save the E+Schema in a key:value format in dbm. The key is the name of the EPJObject. The value is a string representation of json value of that EPJObject from the schema file
    
    dbm.dumb format is used to save the file, since it has greatest cross-platform compatability. The dbm.dumb generates three files (*.dir, *.dat, *.bak). So if dbmname='schema', it will generate schema.dir, schema.dat, schema.bak
    
    Parameters
    ----------
    fname: string, StringIO
        filename of the E+Schema file OR the contents of the E+Schema file in a StringIO
    dbmname: str
        Name of the dbm file

    Returns
    -------
    None
    """    try:
        d = json.load(open(fname, 'r'))
    except TypeError as e:
        d = json.load(fname)
    with dbm.dumb.open(dbmname, 'c') as db:
        db['epJSON_schema_version'] = d['epJSON_schema_version']
        for key in d['properties']:
            db[key] = json.dumps(d['properties'][key])
            
            
if __name__ == '__main__':
    sys.argv[1:]
    fname = sys.argv[1]
    dbmname = sys.argv[2]
    create_schemadbm(fname, dbmname)
    create_index(fname, f'{dbmname}_ref_index')            
