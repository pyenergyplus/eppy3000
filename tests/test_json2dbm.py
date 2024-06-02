# Copyright (c) 2022, 2024 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""py.test for json2dbm.py"""


import json
import tempfile
from pathlib import Path
import shutil
import os
from io import StringIO
from eppy3000.dbm_functions import json2dbm
from eppy3000.dbm_functions import schemaindbm
import pytest


class JSONData(object):
    # schematxt1 =
    schematxt2 = """{
        "$schema": "https://json-schema.org/draft-07/schema#",
        "properties": {
            "Version": {
                "patternProperties": {
                    ".*": {
                        "type": "object",
                        "properties": {
                            "version_identifier": {
                                "type": "string",
                                "default": "22.1"
                            }
                        }
                    }
                },
                "group": "Simulation Parameters",
                "type": "object",
                "maxProperties": 1,
                "memo": "Specifies the EnergyPlus version of the IDF file.",
                "format": "singleLine"
            }
        }
    }"""
    schema4version = """{"$schema":"https://json-schema.org/draft-07/schema#", 
        "properties":{"Version":{"patternProperties":{".*":{"type":"object",
        "properties":{"version_identifier":{"type":"string",
        "default": "notversion"}}}},
        "group":"SimulationParameters",
        "legacy_idd":{"field_info":{"version_identifier":{
        "field_name":"VersionIdentifier",
        "field_type":"a"}},
        "fields":["version_identifier"],
        "alphas":{"fields":["version_identifier"]},
        "numerics":{"fields":[]}},
        "type":"object",
        "maxProperties":1,
        "memo":"SpecifiestheEnergyPlusversionoftheIDFfile.",
        "format":"singleLine"}},
        "required":["Building","GlobalGeometryRules"]}"""


@pytest.fixture
def epschema_version(scope="function"):
    """gets the path name of the dbm folder in ~/.epschema/versionnumber
    made for the test. Deletes the versionnumber part of the folder at the
    end of the test"""
    # get the dir name here
    outerfolder = json2dbm.outerfolder_in_home()
    vernum = json2dbm.getversionnumber(StringIO(JSONData.schema4version))
    tempdir = f"{outerfolder}/{vernum}"
    yield vernum

    # delete it here
    shutil.rmtree(tempdir)


@pytest.fixture
def dbmfiles(scope="function"):
    """creates a temporary folder in which I can keep the json and dbm files
    The folder is removed after the test function is run"""
    tempdir = Path(tempfile.mkdtemp())
    yield tempdir

    shutil.rmtree(tempdir)


def test_create_schemadbm_fromStringIO(dbmfiles):
    """py.test for create_schemadbm"""
    # setup
    tempdir = dbmfiles
    schema = dict(properties=dict(version="53", building="44"))
    jsonstr = json.dumps(schema)
    fhandle = StringIO(jsonstr)
    dbmname = str(tempdir / "schema")
    # test
    json2dbm.create_schemadbm(fhandle, dbmname)
    result = schemaindbm.get_schemakeys(fname=dbmname)
    expected = [b"version", b"building"]
    assert result == expected


def test_create_schemadbm_fromfname(dbmfiles):
    """py.test for create_schemadbm"""
    # setup
    tempdir = dbmfiles
    schema = dict(properties=dict(version="53", building="44"))
    jsonstr = json.dumps(schema)
    jsonname = str(tempdir / "schema.json")
    with open(jsonname, "w") as fhandle:
        fhandle.write(jsonstr)
    dbmname = str(tempdir / "schema")
    # test
    json2dbm.create_schemadbm(jsonname, dbmname)
    result = schemaindbm.get_schemakeys(fname=dbmname)
    expected = [b"version", b"building"]
    assert result == expected


def test_create_index(dbmfiles):
    """py.test for create_index"""
    data = (
        (
            "constructionnames",
            {
                "epJSON_schema_version": "3.2",
                "properties": {
                    "construction": {
                        "name": {"reference": ["CNames", "ConstrNames"]},
                        "patternProperties": {
                            ".*": {"properties": {"surface_type": {"type": "string"}}}
                        },
                    },
                },
            },
            [b"CNames", b"ConstrNames"],
            "CNames",
            {"objlist": ["construction"]},
        ),  # refname, schemadct, expected1, akey, expected2
        (
            "constructionnames",
            {
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
                            ".*": {"properties": {"surface_type": {"type": "string"}}}
                        },
                    },
                },
            },
            [b"CNames", b"ConstrNames", b"SNames", b"SurfNames"],
            "SNames",
            {"objlist": ["surface"]},
        ),  # refname, schemadct, expected1, akey, expected2
        (
            "constructionnames",
            {
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
            },
            [b"CNames", b"ConstrNames", b"SNames", b"SurfNames"],
            "ConstrNames",
            {"objlist": ["construction"], "reflist": ["surface.surface_type"]},
        ),  # refname, schemadct, expected1, akey, expected2
    )
    for refname, schemadct, expected1, akey, expected2 in data:
        # setup
        tempdir = dbmfiles
        jsonstr = json.dumps(schemadct)
        jsonname = str(tempdir / "schema.json")
        with open(jsonname, "w") as fhandle:
            fhandle.write(jsonstr)
        dbmname = str(tempdir / "schema")
        # test
        json2dbm.create_index(jsonname, dbmname)
        result1 = schemaindbm.get_refschemakeys(fname=dbmname)
        assert result1 == expected1
        result2 = schemaindbm.get_a_refschema(akey, fname=dbmname)
        assert result2 == expected2


def test_getversionnumber(dbmfiles):
    """pytest for getversionnumber"""
    tempdir = dbmfiles
    txt = """{"$schema":"https://json-schema.org/draft-07/schema#","properties":
    {"Version":{"patternProperties":{".*":{"type":"object","properties":
    {"version_identifier":{"type":"string","default":"22.1"}}}}}}}"""
    expected = "22.1"
    schemajsonname = f"{tempdir}/schema.json"
    open(schemajsonname, "w").write(txt)
    result = json2dbm.getversionnumber(open(schemajsonname, "rb"))
    assert result == expected


def test_createall_in_verfolder(dbmfiles):
    """pytest for createall_in_verfolder"""
    tempdir = dbmfiles
    txt = JSONData.schematxt2
    fname = f"{tempdir}/schem.json"
    outer_folder = f"{tempdir}/allschemas"
    just_dbmname = "schema"
    expected = f"{outer_folder}/22.1/{just_dbmname}"
    open(fname, "w").write(txt)
    result = json2dbm.createall_in_verfolder(fname, outer_folder, just_dbmname)
    assert result == expected


def test_createall_in_home(epschema_version):
    """pytest for createall_in_home"""
    #  unit test with a wierd version number won't clash with real versions
    expected = epschema_version  # yielded the version number
    # fixture also cleans up the tdir
    tdir = json2dbm.createall_in_home(StringIO(JSONData.schema4version))
    result = schemaindbm.get_schemaversion(tdir)
    assert result == expected
