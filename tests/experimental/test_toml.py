# Copyright (c) 2023 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""py.test for toml.py"""
import pytest
from io import StringIO
import eppy3000.experimental.toml as toml
from eppy3000.modelmaker import EPJ

class TestData:
    tomlstr = """[Version."Version 1"]
version_identifier = "9.3"
idf_order = 1

[SimulationControl."SimulationControl 1"]
do_zone_sizing_calculation = "Yes"
do_system_sizing_calculation = "Yes"
do_plant_sizing_calculation = "Yes"
run_simulation_for_sizing_periods = "No"
run_simulation_for_weather_file_run_periods = "Yes"
idf_order = 2

[Building."Empire State Building"]
north_axis = 30
terrain = "City"
loads_convergence_tolerance_value = 0.04
temperature_convergence_tolerance_value = 0.4
solar_distribution = "FullExterior"
maximum_number_of_warmup_days = 25
minimum_number_of_warmup_days = 6
idf_order = 3

["Site:Location"."CHICAGO_IL_USA TMY2-94846"]
latitude = 41.78
longitude = -87.75
time_zone = -6
elevation = 190
idf_order = 4
"""
    jsonstr = """{
    "Version": {
        "Version 1": {
            "version_identifier": "9.3",
            "idf_order": 1
        }
    },
    "SimulationControl": {
        "SimulationControl 1": {
            "do_zone_sizing_calculation": "Yes",
            "do_system_sizing_calculation": "Yes",
            "do_plant_sizing_calculation": "Yes",
            "run_simulation_for_sizing_periods": "No",
            "run_simulation_for_weather_file_run_periods": "Yes",
            "idf_order": 2
        }
    },
    "Building": {
        "Empire State Building": {
            "north_axis": 30,
            "terrain": "City",
            "loads_convergence_tolerance_value": 0.04,
            "temperature_convergence_tolerance_value": 0.4,
            "solar_distribution": "FullExterior",
            "maximum_number_of_warmup_days": 25,
            "minimum_number_of_warmup_days": 6,
            "idf_order": 3
        }
    },
    "Site:Location": {
        "CHICAGO_IL_USA TMY2-94846": {
            "latitude": 41.78,
            "longitude": -87.75,
            "time_zone": -6,
            "elevation": 190,
            "idf_order": 4
        }
    }
}"""

@pytest.mark.parametrize(
    "tomlstr, expected",
    [
    (
    TestData.tomlstr,
    TestData.jsonstr,
    ), # tomlstr, expected
    ]
)
def test_toml2epj(tomlstr, expected):
    """py.test for toml2epj"""
    result = toml.toml2epj(tomlstr)
    assert result.jsonstr() == expected


@pytest.mark.parametrize(
    "jsonstr, expected",
    [
    (
    TestData.jsonstr,
    TestData.tomlstr,
    ), # jsonstr, expected
    ]
)
def test_epj2toml(jsonstr, expected):
    """py.test for epj2toml"""
    epj = EPJ(StringIO(jsonstr))
    result = toml.epj2toml(epj)
    assert result == expected

def test_readtoml(tmp_path):
    """py.test for readtoml"""
    fname = tmp_path / "test_readtoml.toml"
    fname.write_text(TestData.tomlstr)
    epj  = toml.readtoml(fname)
    result = epj.jsonstr()
    assert result == TestData.jsonstr

def test_writetoml(tmp_path):
    """py.test for writetoml"""
    expected = TestData.tomlstr
    fname = tmp_path / "test_writetoml"
    epj = EPJ(StringIO(TestData.jsonstr))
    toml.writetoml(epj, fname)
    result = fname.read_text()
    assert result == expected

