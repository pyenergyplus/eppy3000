# Copyright (c) 2021 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""py.test for epjviewer"""

import pytest
from eppy3000.modelmaker import EPJ
from eppy3000 import epjviewer

try:
    from IPython.display import IFrame

    JUPYTER = True
except ModuleNotFoundError as e:
    JUPYTER = False

# schema_file = "./eppy3000/resources/schema/V9_3/Energy+.schema.epJSON"
ep_file = "./eppy3000/resources/epJSON/V9_3/smallfile.epJSON"
epj = EPJ(epjname=ep_file)
ep_file_big = (
    "./eppy3000/resources/snippets/V9_0/5Zone_Unitary_HXAssistedCoil.epJSONout"
)
epj_big = EPJ(epjname=ep_file_big)


def test_epj2html():
    """py.test for epj2html"""
    expected = '<table border="1"><tr><th>Version</th><td><table border="1"><tr><th>Version 1</th><td><table border="1"><tr><th>version_identifier</th><td>9.3</td></tr><tr><th>idf_order</th><td>1</td></tr></table></td></tr></table></td></tr><tr><th>SimulationControl</th><td><table border="1"><tr><th>SimulationControl 1</th><td><table border="1"><tr><th>do_zone_sizing_calculation</th><td>Yes</td></tr><tr><th>do_system_sizing_calculation</th><td>Yes</td></tr><tr><th>do_plant_sizing_calculation</th><td>Yes</td></tr><tr><th>run_simulation_for_sizing_periods</th><td>No</td></tr><tr><th>run_simulation_for_weather_file_run_periods</th><td>Yes</td></tr><tr><th>idf_order</th><td>2</td></tr></table></td></tr></table></td></tr><tr><th>Building</th><td><table border="1"><tr><th>Empire State Building</th><td><table border="1"><tr><th>north_axis</th><td>30</td></tr><tr><th>terrain</th><td>City</td></tr><tr><th>loads_convergence_tolerance_value</th><td>0.04</td></tr><tr><th>temperature_convergence_tolerance_value</th><td>0.4</td></tr><tr><th>solar_distribution</th><td>FullExterior</td></tr><tr><th>maximum_number_of_warmup_days</th><td>25</td></tr><tr><th>minimum_number_of_warmup_days</th><td>6</td></tr><tr><th>idf_order</th><td>3</td></tr></table></td></tr></table></td></tr><tr><th>Site:Location</th><td><table border="1"><tr><th>CHICAGO_IL_USA TMY2-94846</th><td><table border="1"><tr><th>latitude</th><td>41.78</td></tr><tr><th>longitude</th><td>-87.75</td></tr><tr><th>time_zone</th><td>-6</td></tr><tr><th>elevation</th><td>190</td></tr><tr><th>idf_order</th><td>4</td></tr></table></td></tr></table></td></tr></table>'
    result = epjviewer.epj2html(epj)
    assert result == expected


def test_epmunch2dct():
    """py.test for epmunch2dct"""
    expected = {"Version": {"Version 1": {"idf_order": 1, "version_identifier": "9.3"}}}
    versions = epj.epobjects["Version"]
    version = versions[0]
    result = epjviewer.epmunch2dct(version)
    assert result == expected


def test_epmunch2html():
    """py.test for epmunch2html"""
    expected = '<table border="1"><tr><th>Version</th><td><table border="1"><tr><th>Version 1</th><td><table border="1"><tr><th>version_identifier</th><td>9.3</td></tr><tr><th>idf_order</th><td>1</td></tr></table></td></tr></table></td></tr></table>'
    versions = epj.epobjects["Version"]
    version = versions[0]
    result = epjviewer.epmunch2html(version)
    assert result == expected


def test_epmunch2ipythonhtml():
    """py.test for epmunch2ipythonhtml"""
    versions = epj.epobjects["Version"]
    version = versions[0]
    if JUPYTER:
        expected = IFrame
        result = epjviewer.epmunch2ipythonhtml(version)
        assert type(result) == expected
    else:
        with pytest.raises(epjviewer.JupyterNotInstalled):
            result = epjviewer.epmunch2ipythonhtml(version)


def test_epmuchhtmllines():
    """py.test for epmuchhtmllines"""
    surfaces = epj_big.epobjects["BuildingSurface:Detailed"]
    surface = surfaces[0]
    result = epjviewer.epmuchhtmllines(surface)
    expected = 15
    assert result == expected


def test_epjhtmllines():
    """py.test for epjhtmllines"""
    result = epjviewer.epjhtmllines(epj)
    expected = 21
    assert result == expected


def test_epobjectslines():
    """py.test for epobjectslines"""
    surfs = epj_big.epobjects["BuildingSurface:Detailed"]
    roofs = [surf for surf in surfs if surf.surface_type == "Roof"]
    version = [ver for ver in epj_big.epobjects["Version"]]
    epobjects = version + roofs
    result = epjviewer.epobjectslines(epobjects)
    expected = 19
    assert result == expected


def test_epj2ipythonhtml():
    """py.test for epj2ipythonhtml"""
    if JUPYTER:
        result = epjviewer.epj2ipythonhtml(epj)
        expected = IFrame
        assert type(result) == expected  # just ensure that it runs
    else:
        with pytest.raises(epjviewer.JupyterNotInstalled):
            result = epjviewer.epj2ipythonhtml(epj)


def test_epobjects2dct():
    """py.test for epobjects2dct"""
    epobjects = epj_big.epobjects["Version"]
    result = epjviewer.epobjects2dct(epobjects)
    expected = {
        "Version": {
            "Version 1": {
                "idf_max_extensible_fields": 0,
                "idf_max_fields": 1,
                "idf_order": 1,
                "version_identifier": "9.0",
            }
        }
    }
    assert result == expected


def test_epobjects2html():
    """py.test for epobjects2html"""
    epobjects = epj_big.epobjects["Version"]
    result = epjviewer.epobjects2html(epobjects)
    expected = '<table border="1"><tr><th>Version</th><td><table border="1"><tr><th>Version 1</th><td><table border="1"><tr><th>idf_max_extensible_fields</th><td>0</td></tr><tr><th>idf_max_fields</th><td>1</td></tr><tr><th>idf_order</th><td>1</td></tr><tr><th>version_identifier</th><td>9.0</td></tr></table></td></tr></table></td></tr></table>'
    assert result == expected


def test_epobjects2ipythonhtml():
    """py.test for epobjects2ipythonhtml"""
    epobjects = epj_big.epobjects["Version"]
    if JUPYTER:
        expected = IFrame
        result = epjviewer.epobjects2ipythonhtml(epobjects)
        assert type(result) == expected  # just ensure that it runs
    else:
        with pytest.raises(epjviewer.JupyterNotInstalled):
            result = epjviewer.epobjects2ipythonhtml(epobjects)
