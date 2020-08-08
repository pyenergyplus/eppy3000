"""these test have to be run manually since eppy may not be installed"""

from io import StringIO
from pathlib import Path
import os

# from eppy3000 import idfjsonconverter
from tests import schemafortesting
from eppy3000.modelmaker import EPJ

# import eppy3000.oldeppy.idfjsonconverter as idfjsonconverter
import eppy3000.oldeppy as oldeppy
import eppy

SCHEMA_FILE = schemafortesting.schema_file

# path for iddfile -> clean this later
THIS_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
IDDFILE = THIS_DIR / os.pardir / "eppy3000/resources/snippets/V9_1/iddV9_1_snippet.idd"
iddfile = IDDFILE


def test_idf2idj_epj2idf():
    """py.test for idf2idj and epj2idf"""
    # rearranged the order of so that it matches the order in the idd file.
    # So the tests can pass
    data = (
        (
            """
  Version,9.1;

Building,
    Bldg one,                !- Name
    30,                     !- North Axis {deg}
    City,                    !- Terrain
    0.04,                    !- Loads Convergence Tolerance Value
    0.4,                     !- Temperature Convergence Tolerance Value {deltaC}
    FullExterior,            !- Solar Distribution
    25,                      !- Maximum Number of Warmup Days
    6;                       !- Minimum Number of Warmup Days

Timestep,4;

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
    0,0,3,  !- X,Y,Z ==> Vertex 1 {m}
    0,0,2.4,  !- X,Y,Z ==> Vertex 2 {m}
    30.5,0,2.4,  !- X,Y,Z ==> Vertex 3 {m}
    30.5,0,3;  !- X,Y,Z ==> Vertex 4 {m}


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

OutdoorAir:NodeList,
    OutsideAirInletNodes;    !- Node or NodeList Name 1

""",  # noqa: E501
        ),  # idftxt
    )
    for (idftxt,) in data:
        iddhandle = open(iddfile, "r")
        iddtxt = iddhandle.read()
        iddstringio = StringIO(iddtxt)

        # convert idf to epj, then epj to idf and lastly idf to epj
        # compare the first epj.json and last epj.json
        idfhandle = StringIO(idftxt)
        idf = eppy.openidf(idfhandle, idd=iddstringio)
        epsjsonschema = schemafortesting.schema

        # idf to epj
        epj1 = oldeppy.idf2epj(idf, epsjsonschema)

        # epj to idf
        idf1 = oldeppy.epj2idf(epj1, epsjsonschema, iddhandle=iddstringio)

        # idf to epj
        epj2 = oldeppy.idf2epj(idf1, epsjsonschema)

        # compare epj1 and epj2
        assert epj1.jsonstr() == epj2.jsonstr()
