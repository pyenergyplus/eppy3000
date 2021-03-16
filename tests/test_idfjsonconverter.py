# Copyright (c) 2019-2021 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""py.test for idfjsonconverter"""

from io import StringIO

from eppy3000 import idfjsonconverter
from eppy3000 import installlocation
from tests import schemafortesting

import pytest

SCHEMA_FILE = schemafortesting.schema_file


class IDFtxt:
    """an IDF txt"""
    idftxt = """
  Version,9.1;

  ZoneHVAC:EquipmentList,
    SPACE1-1 Eq,             !- Name
    SequentialLoad,          !- Load Distribution Scheme
    ZoneHVAC:AirDistributionUnit,  !- Zone Equipment 1 Object Type
    SPACE1-1 ATU,            !- Zone Equipment 1 Name
    1,                       !- Zone Equipment 1 Cooling Sequence
    1;                       !- Zone Equipment 1 Heating or No-Load Sequence


NodeList,
    SPACE1-1 In Nodes,       !- Name
    SPACE1-1 In Node;        !- Node 1 Name

NodeList,
    Supply Air Temp Nodes 1, !- Name
    Main Cooling Coil 1 Inlet Node,  !- Node 1 Name
    Heat Recovery Supply Outlet,  !- Node 2 Name
    Main Heating Coil 1 Inlet Node,  !- Node 3 Name
    Reheat Coil Air Inlet Node,  !- Node 4 Name
    VAV Sys 1 Outlet Node;   !- Node 5 Name

BuildingSurface:Detailed,
    WALL-1PF,                !- Name
    WALL,                    !- Surface Type
    WALL-1,                  !- Construction Name
    PLENUM-1,                !- Zone Name
    Outdoors,                !- Outside Boundary Condition
    ,                        !- Outside Boundary Condition Object
    SunExposed,              !- Sun Exposure
    WindExposed,             !- Wind Exposure
    0.50000,                 !- View Factor to Ground
    4,                       !- Number of Vertices
    0.0,0.0,3.0,  !- X,Y,Z ==> Vertex 1 {m}
    0.0,0.0,2.4,  !- X,Y,Z ==> Vertex 2 {m}
    30.5,0.0,2.4,  !- X,Y,Z ==> Vertex 3 {m}
    30.5,0.0,3.0;  !- X,Y,Z ==> Vertex 4 {m}

Timestep,4;

Building,
    Bldg one,                !- Name
    30.,                     !- North Axis {deg}
    City,                    !- Terrain
    0.04,                    !- Loads Convergence Tolerance Value
    0.4,                     !- Temperature Convergence Tolerance Value {deltaC}
    FullExterior,            !- Solar Distribution
    25,                      !- Maximum Number of Warmup Days
    6;                       !- Minimum Number of Warmup Days

Zone,
    Main Zone,               !- Name
    0,                       !- Direction of Relative North {deg}
    0,                       !- X Origin {m}
    0,                       !- Y Origin {m}
    0,                       !- Z Origin {m}
    1,                       !- Type
    1,                       !- Multiplier
    autocalculate,           !- Ceiling Height {m}
    autocalculate;           !- Volume {m3}

Zone,
    Another Zone,               !- Name
    90,                       !- Direction of Relative North {deg}
    11,                       !- X Origin {m}
    22,                       !- Y Origin {m}
    33,                       !- Z Origin {m}
    1,                       !- Type
    1,                       !- Multiplier
    autocalculate,           !- Ceiling Height {m}
    autocalculate;           !- Volume {m3}

OutdoorAir:NodeList,
    OutsideAirInletNodes;    !- Node or NodeList Name 1

"""
        

def test_keymapping():
    """py.test for keymapping"""
    data = (
        (
            ("Gumby", "Softy"),
            ("gumby", "so", "softy", "Kamby"),
            {"Gumby": "gumby", "Softy": "softy"},
        ),
        # somekeys, allkeys, expected
    )
    for somekeys, allkeys, expected in data:
        result = idfjsonconverter.keymapping(somekeys, allkeys)
        assert result == expected


def test_idf2json_json2idf():
    """py.test for idf2json and json2idf"""
    data = (
        (IDFtxt.idftxt,  
        ),  # idftxt
    )
    for (idftxt,) in data:
        # convert idf to json, then json to idf and lastly idf to json
        # compare the first json and last json
        idfhandle = StringIO(idftxt)
        epsjsonschema = schemafortesting.schema
        jsonresult1 = idfjsonconverter.idf2json(idfhandle, epsjsonschema)
        jsonhandle = StringIO(jsonresult1)
        epsjsonschema = schemafortesting.schema
        idfresult1 = idfjsonconverter.json2idf(jsonhandle, epsjsonschema)

        idfhandle = StringIO(idfresult1)
        epsjsonschema = schemafortesting.schema
        jsonresult2 = idfjsonconverter.idf2json(idfhandle, epsjsonschema)
        assert jsonresult1 == jsonresult2

@pytest.mark.parametrize("idftxt, expected", 
[
    ("""
    ! Floor Area:              232.25 m2
    ! Number of Stories:       1

    Version,9.1;

    Timestep,6;

    Building,
        Bldg,                    !- Name
        0.0,                     !- North Axis {deg}
        Suburbs,                 !- Terrain
        0.05,                    !- Loads Convergence Tolerance Value
        0.05,                    !- Temperature Convergence Tolerance Value {deltaC}
        MinimalShadowing,        !- Solar Distribution
        30,                      !- Maximum Number of Warmup Days
        6;                       !- Minimum Number of Warmup Days
    """,
    "9.1"), # idftxt, expected
    ("""
    !- Darwin Line endings 

    VERSION,
        9.0;                      !- Version Identifier

    """,
    "9.0"), # idftxt, expected
    ("""
    !- Darwin Line endings 

    VERSION,
        9.0
        ;                      !- Version Identifier

    """,
    "9.0"), # idftxt, expected
    # --
    # single line version 1
    ("""
    !- Darwin Line endings 

    Timestep,6;    VERSION,
      9.0
        ;                      !- Version Identifier

    """,
    "9.0"), # idftxt, expected
    # --
    # single line version 2
    ("""
    !- Darwin Line endings 

    Timestep,6;    VERSION, 9.0
        ;                      !- Version Identifier

    """,
    "9.0"), # idftxt, expected
    # --
    # single line version 3
    ("""
    !- Darwin Line endings 

    Timestep,6;    VERSION, 9.0 ;  !- Version Identifier

    """,
    "9.0"), # idftxt, expected
    # ---
    # no version in file
    ("""
    !- Darwin Line endings 

    XERSION,
        9.0
        ;                      !- Version Identifier

    """,
    None), # idftxt, expected

])
def test_getidfversion(idftxt, expected):
    """py.test for getidfversion"""
    fhandle = StringIO(idftxt)
    result = idfjsonconverter.getidfversion(fhandle)
    assert result == expected
    
@pytest.mark.parametrize("idftxt, idffilename, epjfilename, epschemapath, expected",
[
    # the first two commented out tests will work only if you installed EnergyPlus
    # (IDFtxt.idftxt, "aa.idf", "bb.epj", None, None), # idftxt, idffilename, epjfilename, epschemapath, expected
    # (IDFtxt.idftxt, "aa.idf", None, None, None), # idftxt, idffilename, epjfilename, epschemapath, expected
    (IDFtxt.idftxt, "aa.idf", "bb.epj", SCHEMA_FILE, None), # idftxt, idffilename, epjfilename, epschemapath, expected
    (IDFtxt.idftxt, "aa.idf", None, SCHEMA_FILE, None), # idftxt, idffilename, epjfilename, epschemapath, expected
])
def test_idffile2epjfile(tmp_path, idftxt, idffilename, epjfilename, epschemapath, expected):
    """py.test for idffile2epjfile"""
    # 1. write idf to idffile
    # 2. convert idffile to epjfile -> the function we are testing
    # 3. convert idf to epj (expected)
    # 4. read epjfile and compare to epj in 3.
    # - 
    # 1. write idf to idffile
    tmpdir = tmp_path
    tmpidffile = tmpdir / idffilename
    tmpidffile.write_text(idftxt)
    idffilepath = tmpidffile.resolve()
    # - 
    if epjfilename:
        tmpepjfile = tmpdir / epjfilename
        epjfilepath = tmpepjfile.resolve()
    else: 
        epjfilepath = None
        newepjname = f'{idffilename.split(".")[0]}.epj'
        tmpepjfile = tmpdir / newepjname
        newepjfilepath = tmpepjfile.resolve()
    # 2. convert idffile to epjfile -> the function we are testing
    idfjsonconverter.idffile2epjfile(idffilepath, epjfilepath, epschemapath)
    # 3. convert idf to epj (expected)
    if epschemapath:
        new_epschemapath = epschemapath
    else:
        with open(idffilepath, 'r') as idfhandle:
            version = idfjsonconverter.getidfversion(idfhandle)
        new_epschemapath = installlocation.schemapath(version)
        
    idfhandle = StringIO(idftxt)
    with open(new_epschemapath, 'r') as epschemahandle:
        expected = idfjsonconverter.idf2json(idfhandle, epschemahandle)
    # 4. read epjfile and compare to epj in 3.
    if epjfilepath:
        result = open(epjfilepath, 'r').read()
    else:
        result = open(newepjfilepath, 'r').read()
    assert result == expected

@pytest.mark.parametrize("idftxt, epjname, idfname, schemapath, expected",
[
    (IDFtxt.idftxt, "aa.epj", "bb.idf", SCHEMA_FILE, None), # idftxt, epjname, idfname, schemapath, expected
])
def test_epjfile2idffile(tmp_path, idftxt, epjname, idfname, schemapath, expected):
    """py.test for epjfile2idffile"""
    # 1. convert idf to epj
    # 2. write epj to epjfile
    # 3. convert epjfile to idffile -> the function we are testing
    # 4. read the spj file and comvert it to idf
    # 5. read idffile and compare to idf in 4.
    # -
    # 1. convert idf to epj
    idfhandle = StringIO(idftxt)
    with open(schemapath, 'r') as schemahandle:
        epjstr = idfjsonconverter.idf2json(idfhandle, schemahandle)
    # 2. write epj to epjfile
    tmpdir = tmp_path
    tmpepjfile = tmpdir / epjname
    tmpepjfile.write_text(epjstr)
    epjfilepath = tmpepjfile.resolve()
    # - 
    if idfname:
        tmpidffile = tmpdir / idfname
        idffilepath = tmpidffile.resolve()
    else: 
        idffilepath = None
        newidfname = f'{idfname.split(".")[0]}.epj'
        tmpidffile = tmpdir / newidfname
        newidffilepath = tmpidffile.resolve()
    # 3. convert epjfile to idffile -> the function we are testing
    idfjsonconverter.epjfile2idffile(epjfilepath, idffilepath, schemapath)
    # 4. read the spj file and comvert it to idf
    with open(epjfilepath, 'r') as epjhandle:
        expected = idfjsonconverter.json2idf(epjhandle, open(schemapath, 'r'))
    # 5. read idffile and compare to idf in 4.
    if idffilepath:
        result = open(idffilepath, 'r').read()
    else:
        result = open(newidffilepath, 'r').read()
    print(result)
    print("-" * 8)
    print(expected)
    assert result == expected
    
        
@pytest.mark.parametrize("lst, expected", 
[
    ([(1, 2), (3, 0), (4, '')],
    [(1, 2), (3, 0)]), # lst, expected
    ([(1, 2), (33, ''), (3, 0), (4, ''), (5, '')],
    [(1, 2), (33, ''),  (3, 0)]), # lst, expected
])
def test_removetrailingblanks(lst, expected):
    """py.test for removetrailingblanks"""
    result = idfjsonconverter.removetrailingblanks(lst)
    assert result == expected