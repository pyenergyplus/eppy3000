"""scratch code to test out schemaindbm.dbmval2dict"""

import json
import shutil
from pathlib import Path
import tempfile
from eppy3000.dbm_functions import json2dbm
from eppy3000.dbm_functions import schemaindbm


# create a temp schema dbm
tempdir = Path(tempfile.mkdtemp())
schema = dict(
    epJSON_schema_version="3.2",
    properties=dict(
        version=dict(a=1),
        building=dict(
            b=2,
            name=dict(c=3),
            patternProperties=dict(
                something=dict(
                    properties=dict(
                        field1=dict(f1=1),
                        field2=dict(
                            items=dict(
                                properties=dict(a1=dict(aa1=1), a2=dict(aa2=2))
                            )
                        ),
                    )
                )
            ),
        ),
    ),
)
jsonstr = json.dumps(schema)
jsonname = str(tempdir / "schema.json")
with open(jsonname, "w") as fhandle:
    fhandle.write(jsonstr)
dbmname = str(tempdir / "schema")
json2dbm.create_schemadbm(jsonname, dbmname)

schemanfname = f"{tempdir}/schema"
keys = schemaindbm.get_schemakeys(fname=schemanfname)
print(f"{keys=}")
key = 'building'
# key = 'nothing'
aschema = schemaindbm.get_aschema(key, fname=schemanfname)
print(f"{aschema=}")

dct = dict(building=1, c=3)

key = 'building'
result = schemaindbm.dbmval2dict(dct, key, dbmname=schemanfname)
print(f"{result=}")

key = 'version'
result = schemaindbm.dbmval2dict(dct, key, dbmname=schemanfname)
print(f"{result=}")
print(f"{key=}, {dct[key]=}")

# TODO: make all these as test for dbmval2dict - including commented ones below

# key = 'nothing'
# result = schemaindbm.dbmval2dict(dct, key, dbmname=schemanfname)
# print(f"{result=}")
# print(f"{dct[key]}")



shutil.rmtree(tempdir)
