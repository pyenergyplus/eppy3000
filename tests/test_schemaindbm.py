# Copyright (c) 2022 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""py.test for schemaindbm"""

import tempfile
from pathlib import Path
import shutil
from io import StringIO
import json

import pytest

from eppy3000.dbm_functions import json2dbm
from eppy3000.dbm_functions import schemaindbm

@pytest.fixture
def make_refdbm(scope="module"):
    """creates a temporary folder in which I can keep the json and dbm files
    The folder is removed after the test function is run
    This fuxture makes is used to test the index dbm"""
    tempdir = Path(tempfile.mkdtemp())
    schema =             {
                "epJSON_schema_version": "3.2",
                "properties": {
                    "construction": {
                        "name": {"reference": ["CNames", "ConstrNames"]},
                        "patternProperties": {
                            ".*": {"properties": {"surface_type": {"type": "string"}}}
                        },
                    },
                    "surface": {
                        "name": {"reference": ["SNames", "SurfNames"]},
                        "patternProperties": {
                            ".*": {
                                "properties": {
                                    "surface_type": {
                                        "type": "string",
                                        "object_list": ["ConstrNames"],
                                    }
                                }
                            }
                        },
                    },
                },
            }
    jsonstr = json.dumps(schema)
    jsonname = str(tempdir / "schema.json")
    with open(jsonname, "w") as fhandle:
        fhandle.write(jsonstr)
    dbmname = str(tempdir / "schema_ref_index")
    json2dbm.create_index(jsonname, dbmname)
    yield dbmname

    shutil.rmtree(tempdir)


@pytest.fixture
def make_dbm(scope="module"):
    """creates a temporary folder in which I can keep the json and dbm files
    The folder is removed after the test function is run"""
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
    yield dbmname

    shutil.rmtree(tempdir)


def test_db_in_memory():
    """py.test for db_in_memory"""
    objkey = "Version"
    # default location read
    db = schemaindbm.db_in_memory()  # reads from default location
    assert objkey in db
    # read from StringIO
    dt_in = dict(properties=dict(Version="33"))
    dt_in_str = json.dumps(dt_in)
    fhandle = StringIO(dt_in_str)
    db = schemaindbm.db_in_memory(fhandle)
    assert objkey in db


def test_get_schemakeys(make_dbm):
    """py.test for get_schemakeys"""
    # test
    result = schemaindbm.get_schemakeys(fname=make_dbm)
    expected = {b"building", b"version", b"epJSON_schema_version"}
    assert set(result) == expected


def test_get_aschema(make_dbm):
    """py.test for get_aschema"""
    objkey = "version"
    result = schemaindbm.get_aschema(objkey, fname=make_dbm)
    assert result == {"a": 1}


def test_get_name(make_dbm):
    """py.test for get_name"""
    objkey = "version"
    result = schemaindbm.get_name(objkey, fname=make_dbm)
    assert result == None
    objkey = "building"
    result = schemaindbm.get_name(objkey, fname=make_dbm)
    assert result == {"c": 3}
    # test with aschema
    aschema = schemaindbm.get_aschema(objkey, fname=make_dbm)
    result = schemaindbm.get_name(objkey, aschema=aschema)
    assert result == {"c": 3}


def test_get_props(make_dbm):
    """py.test for get_props"""
    objkey = "building"
    expected = {
        "field1": {"f1": 1},
        "field2": {"items": {"properties": {"a1": {"aa1": 1}, "a2": {"aa2": 2}}}},
    }
    result = schemaindbm.get_props(objkey, fname=make_dbm)
    assert result == expected
    # test with aschema
    aschema = schemaindbm.get_aschema(objkey, fname=make_dbm)
    result = schemaindbm.get_props(objkey, aschema=aschema)
    assert result == expected


def test_get_field(make_dbm):
    """py.test for get_field"""
    objkey = "building"
    expected = {"f1": 1}
    result = schemaindbm.get_field(objkey, "field1", fname=make_dbm)
    assert result == expected
    # test with aschema
    aschema = schemaindbm.get_aschema(objkey, fname=make_dbm)
    result = schemaindbm.get_field(objkey, "field1", aschema=aschema)
    assert result == expected


def test_get_arrayfieldnames(make_dbm):
    """py.test for get_arrayfieldnames"""
    objkey = "building"
    result = schemaindbm.get_arrayfieldnames(objkey, "field1", fname=make_dbm)
    assert result == list()
    result = schemaindbm.get_arrayfieldnames(objkey, "field2", fname=make_dbm)
    assert result == ["a1", "a2"]
    # test with aschema
    aschema = schemaindbm.get_aschema(objkey, fname=make_dbm)
    result = schemaindbm.get_arrayfieldnames(objkey, "field2", aschema=aschema)
    assert result == ["a1", "a2"]


def test_get_arrayfield(make_dbm):
    """py.test for get_arrayfield"""
    objkey = "building"
    result = schemaindbm.get_arrayfield(objkey, "field2", "a1", fname=make_dbm)
    assert result == {"aa1": 1}
    # test with aschema
    aschema = schemaindbm.get_aschema(objkey, fname=make_dbm)
    result = schemaindbm.get_arrayfield(objkey, "field2", "a1", aschema=aschema)
    assert result == {"aa1": 1}


def test_get_refschemakeys(make_refdbm):
    """py.test for get_refschemakeys"""
    result = schemaindbm.get_refschemakeys(fname=make_refdbm)
    expected = [b'CNames', b'ConstrNames', b'SNames', b'SurfNames']
    assert set(result) == set(expected)
    
def test_get_a_refschema(make_refdbm):
    """py.test for get_a_refschema"""
    result = schemaindbm.get_a_refschema("ConstrNames", fname=make_refdbm) 
    expected = {'objlist': ['construction'], 'reflist': ['surface.surface_type']}   
    assert result == expected