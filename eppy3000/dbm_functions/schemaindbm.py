"""explore the schema in the dbm"""

import dbm
import json
import dbm.dumb


def db_in_memory(fname=None):
    """get the dbm in memory"""
    if not fname:
        fname = '../eppy3000/eppy3000/resources/schema/V9_3/Energy+.schema.epJSON'
    d = json.load(open(fname, 'r'))
    db = dict()
    for key in d['properties']:
        db[key] = json.dumps(d['properties'][key])
    return db
    


def main(key):
    try:
        key = key.encode()
    except AttributeError as e:
        pass
    with dbm.dumb.open('schema', 'r') as db:
        print(db[key])
                
        
def get_schemakeys(fname=None):
    """get all the schema keys"""
    if fname:
        with dbm.dumb.open(fname, 'r') as db:
            return db.keys()
    else:
        with dbm.dumb.open('./schema', 'r') as db:
            return db.keys()

def get_aschema(key, fname=None):
    """gets a schema"""
    try:
        key = key.encode()
    except AttributeError as e:
        pass
    if fname:
        with dbm.dumb.open(fname, 'r') as db:
            dt = json.loads(db[key])
            return dt
    else:
        with dbm.dumb.open('./schema', 'r') as db:
            dt = json.loads(db[key])
            return dt
        
def get_name(key, aschema=None):
    """get the name field of the schema"""
    if aschema:
        dt = aschema
    else:
        dt = get_aschema(key)
    try:
        return dt['name']
    except KeyError as e:
        return None
    
def get_props(key, aschema=None, fname=None):
    """gets the properties of a schema
    if already have aschema, it avoids disk access"""
    if aschema:
        dt = aschema
    else:
        dt = get_aschema(key, fname=fname)
    # props = dt['patternProperties']['^.*\\S.*$']['properties']
    for pkey in dt['patternProperties']:
        props = dt['patternProperties'][pkey]['properties'] 
        break
    return props

def get_field(key, fieldname, aschema=None):
    """get the field of a schema
    if already have aschema, it avoids disk access"""
    dt = get_props(key, aschema)
    return dt[fieldname]
    
def get_arrayfieldnames(key, fieldname, aschema=None):
    """get the array fieldnames of a field"""
    field = get_field(key, fieldname, aschema=aschema)
    try:
        return [arrayfield for arrayfield in field['items']['properties']]
    except KeyError as e:
        return list()
        
def get_arrayfield(key, fieldname, arrayfieldname, aschema=None):
    """get the array field of a field"""
    field = get_field(key, fieldname, aschema=aschema)
    return field['items']['properties'][arrayfieldname]
    
def get_a_refschema(key, fname=None):
    """get a reference key from the reference schema"""
    try:
        key = key.encode()
    except AttributeError as e:
        pass
    if fname:
        with dbm.dumb.open(fname, 'r') as db:
            dt = json.loads(db[key])
            return dt
    else:
        with dbm.dumb.open('./schema_ref_index', 'r') as db:
            dt = json.loads(db[key])
            return dt

def get_refschemakeys(fname=None):
    """get all the ref schema keys"""
    if fname:
        with dbm.dumb.open(fname, 'r') as db:
            return db.keys()
    else:
        with dbm.dumb.open('./schema_ref_index', 'r') as db:
            return db.keys()

        

if __name__ == '__main__':
    fname = '../eppy3000viewer/schema'
    
    # epjkey = 'Coil:Cooling:DX:TwoSpeed'
    epjkey = 'SimulationControl'
    epjkey = 'Building'

    fieldnames = get_props(epjkey, fname=fname).keys()
    aschema = get_aschema(epjkey, fname=fname)
    aschema_keys = list(aschema.keys())
    
    refschemakeys = get_refschemakeys(fname=f'{fname}_ref_index')
    arefschema = get_a_refschema('ConstructionNames', fname=f'{fname}_ref_index')
    print(arefschema['objlist'])
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
    
    
    
