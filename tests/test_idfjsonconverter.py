"""py.test for idfjsonconverter"""

from io import StringIO

from munch import Munch

from eppy3000 import idfjsonconverter
from tests import schemafortesting

SCHEMA_FILE = schemafortesting.schema_file

def test_keymapping():
    """py.test for keymapping"""
    data = (
    (
    ('Gumby', 'Softy'),
    ('gumby', 'so', 'softy', 'Kamby'),
    {'Gumby': 'gumby', 'Softy': 'softy'}), # somekeys, allkeys, expected
    )
    for somekeys, allkeys, expected in data:
        result = idfjsonconverter.keymapping(somekeys, allkeys)
        assert result == expected


def test_idf2json_json2idf():
    """py.test for idf2json and json2idf"""
    data = (("""
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

""",
),  # idftxt
    )
    for idftxt, in data:
        # convert idf to json, then json to idf and lastly idf to json
        # compare the first json and last json
        idfhandle = StringIO(idftxt)
        epjsonhandle = open(SCHEMA_FILE)
        jsonresult1 = idfjsonconverter.idf2json(idfhandle, epjsonhandle)
        jsonhandle = StringIO(jsonresult1)
        epjsonhandle = open(SCHEMA_FILE)
        idfresult1 = idfjsonconverter.json2idf(jsonhandle, epjsonhandle)

        idfhandle = StringIO(idfresult1)
        epjsonhandle = open(SCHEMA_FILE)
        jsonresult2 = idfjsonconverter.idf2json(idfhandle, epjsonhandle)
        assert jsonresult1 == jsonresult2

def test_readiddasmunch():
    """py.test for readiddasmunch"""
    schemahandle = open(SCHEMA_FILE, 'r')
    result = idfjsonconverter.readiddasmunch(schemahandle)
    assert isinstance(result, Munch)

    result = idfjsonconverter.readiddasmunch(SCHEMA_FILE)
    assert isinstance(result, Munch)

    schemahandle = Munch.fromDict(dict(a=1, b=2))
    result = idfjsonconverter.readiddasmunch(schemahandle)
    assert isinstance(result, Munch)

    schemahandle = list()
    result = idfjsonconverter.readiddasmunch(schemahandle)
    assert isinstance(result, Munch)
