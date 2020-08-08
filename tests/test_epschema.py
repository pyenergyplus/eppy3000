# Copyright (c) 2019 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""py.test for epschema.py"""

from io import StringIO
from eppy3000 import epschema
import pytest

from tests import schemafortesting


def test_read_epschema_asmunch():
    """py.test for read_epschema_asmunch"""
    SCHEMA_FILE = schemafortesting.schema_file
    schemahandle = open(SCHEMA_FILE, "r")
    result = epschema.read_epschema_asmunch(schemahandle)
    assert isinstance(result, epschema.EPSchemaMunch)

    result = epschema.read_epschema_asmunch(SCHEMA_FILE)
    assert isinstance(result, epschema.EPSchemaMunch)

    schemahandle = schemafortesting.schema
    result = epschema.read_epschema_asmunch(schemahandle)
    assert isinstance(result, epschema.EPSchemaMunch)

    schemahandle = list()
    with pytest.raises(TypeError):
        result = epschema.read_epschema_asmunch(schemahandle)


def test_EPSchema():
    """py.test for EPSchema"""
    txt = """{
    "epJSON_schema_version": "8.9.0",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "required": [
        "Building",
        "GlobalGeometryRules"
    ],
    "properties": {
        "Building": {
            "name": {
                "default": "NONE",
                "retaincase": true,
                "type": "string"
            },
            "memo": "Describes parameters that are used during the simulation of the building. There are necessary correlations between the entries for this object and some entries in the Site:WeatherStation and Site:HeightVariation objects, specifically the Terrain field.",
            "patternProperties": {
                ".*": {
                    "type": "object",
                    "properties": {
                        "solar_distribution": {
                            "note": "MinimalShadowing | FullExterior | FullInteriorAndExterior | FullExteriorWithReflections | FullInteriorAndExteriorWithReflections",
                            "default": "FullExterior",
                            "enum": [
                                "",
                                "FullExterior",
                                "FullExteriorWithReflections",
                                "FullInteriorAndExterior",
                                "FullInteriorAndExteriorWithReflections",
                                "MinimalShadowing"
                            ],
                            "type": "string"
                        },
                        "terrain": {
                            "note": "Country=FlatOpenCountry | Suburbs=CountryTownsSuburbs | City=CityCenter | Ocean=body of water (5km) | Urban=Urban-Industrial-Forest",
                            "default": "Suburbs",
                            "enum": [
                                "",
                                "City",
                                "Country",
                                "Ocean",
                                "Suburbs",
                                "Urban"
                            ],
                            "type": "string"
                        },
                        "north_axis": {
                            "note": "degrees from true North",
                            "units": "deg",
                            "default": 0.0,
                            "type": "number"
                        },
                        "maximum_number_of_warmup_days": {
                            "note": "EnergyPlus will only use as many warmup days as needed to reach convergence tolerance. This field's value should NOT be set less than 25.",
                            "exclusiveMinimum": true,
                            "default": 25.0,
                            "minimum": 0.0,
                            "type": "number"
                        },
                        "loads_convergence_tolerance_value": {
                            "default": 0.04,
                            "type": "number",
                            "maximum": 0.5,
                            "note": "Loads Convergence Tolerance Value is a fraction of load",
                            "minimum": 0.0,
                            "exclusiveMinimum": true
                        },
                        "temperature_convergence_tolerance_value": {
                            "default": 0.4,
                            "type": "number",
                            "maximum": 0.5,
                            "minimum": 0.0,
                            "units": "deltaC",
                            "exclusiveMinimum": true
                        },
                        "minimum_number_of_warmup_days": {
                            "note": "The minimum number of warmup days that produce enough temperature and flux history to start EnergyPlus simulation for all reference buildings was suggested to be 6. When this field is greater than the maximum warmup days defined previous field the maximum number of warmup days will be reset to the minimum value entered here. Warmup days will be set to be the value you entered when it is less than the default 6.",
                            "exclusiveMinimum": true,
                            "default": 6.0,
                            "minimum": 0.0,
                            "type": "number"
                        }
                    }
                }
            },
            "legacy_idd": {
                "numerics": {
                    "fields": [
                        "north_axis",
                        "loads_convergence_tolerance_value",
                        "temperature_convergence_tolerance_value",
                        "maximum_number_of_warmup_days",
                        "minimum_number_of_warmup_days"
                    ]
                },
                "field_info": {
                    "name": {
                        "field_type": "a",
                        "field_name": "Name"
                    },
                    "solar_distribution": {
                        "field_type": "a",
                        "field_name": "Solar Distribution"
                    },
                    "terrain": {
                        "field_type": "a",
                        "field_name": "Terrain"
                    },
                    "north_axis": {
                        "field_type": "n",
                        "field_name": "North Axis"
                    },
                    "maximum_number_of_warmup_days": {
                        "field_type": "n",
                        "field_name": "Maximum Number of Warmup Days"
                    },
                    "loads_convergence_tolerance_value": {
                        "field_type": "n",
                        "field_name": "Loads Convergence Tolerance Value"
                    },
                    "temperature_convergence_tolerance_value": {
                        "field_type": "n",
                        "field_name": "Temperature Convergence Tolerance Value"
                    },
                    "minimum_number_of_warmup_days": {
                        "field_type": "n",
                        "field_name": "Minimum Number of Warmup Days"
                    }
                },
                "alphas": {
                    "fields": [
                        "name",
                        "terrain",
                        "solar_distribution"
                    ]
                },
                "fields": [
                    "name",
                    "north_axis",
                    "terrain",
                    "loads_convergence_tolerance_value",
                    "temperature_convergence_tolerance_value",
                    "solar_distribution",
                    "maximum_number_of_warmup_days",
                    "minimum_number_of_warmup_days"
                ]
            },
            "maxProperties": 1,
            "minProperties": 1,
            "type": "object",
            "min_fields": 8.0
        },
        "OutdoorAir:NodeList": {
            "type": "object",
            "memo": "This object sets the temperature and humidity conditions for an outdoor air node using the weather data values. to vary outdoor air node conditions with height above ground use OutdoorAir:Node instead of this object. This object may be used more than once. The same node name may not appear in both an OutdoorAir:Node object and an OutdoorAir:NodeList object.",
            "legacy_idd": {
                "numerics": {
                    "fields": []
                },
                "field_info": {
                    "node_or_nodelist_name": {
                        "field_type": "a",
                        "field_name": "Node or NodeList Name"
                    }
                },
                "extensibles": [
                    "node_or_nodelist_name"
                ],
                "extension": "nodes",
                "alphas": {
                    "fields": [],
                    "extensions": [
                        "node_or_nodelist_name"
                    ]
                },
                "fields": []
            },
            "patternProperties": {
                ".*": {
                    "type": "object",
                    "properties": {
                        "nodes": {
                            "items": {
                                "required": [
                                    "node_or_nodelist_name"
                                ],
                                "type": "object",
                                "properties": {
                                    "node_or_nodelist_name": {
                                        "type": "string"
                                    }
                                }
                            },
                            "type": "array"
                        }
                    }
                }
            },
            "extensible_size": 1.0
        }
    },
    "epJSON_schema_build": "40101eaafd"
}"""  # noqa: E501

    # expected
    version = "8.9.0"
    required = ["Building", "GlobalGeometryRules"]
    epschemaobjectskeys = ["Building", "OutdoorAir:NodeList"]
    buildingkeys = [
        "solar_distribution",
        "terrain",
        "north_axis",
        "maximum_number_of_warmup_days",
        "loads_convergence_tolerance_value",
        "temperature_convergence_tolerance_value",
        "minimum_number_of_warmup_days",
    ]
    buildingterraintype = "string"
    bfieldnames = [
        "solar_distribution",
        "terrain",
        "north_axis",
        "maximum_number_of_warmup_days",
        "loads_convergence_tolerance_value",
        "temperature_convergence_tolerance_value",
        "minimum_number_of_warmup_days",
    ]
    fieldnameslist = None  # not yet coded
    #
    # tests
    fhandle = StringIO(txt)
    result = epschema.EPSchema(fhandle)

    assert version == result.version
    assert required == result.required
    assert epschemaobjectskeys == list(result.epschemaobjects.keys())
    assert buildingkeys == list(result.epschemaobjects["Building"].keys())
    #
    bldg = result.epschemaobjects["Building"]
    assert buildingterraintype == bldg.fieldproperty("terrain")["type"]
    assert bfieldnames == result.epschemaobjects["Building"].fieldnames()
    oairnode = result.epschemaobjects["OutdoorAir:NodeList"]
    assert fieldnameslist == oairnode.fieldnames_list()
