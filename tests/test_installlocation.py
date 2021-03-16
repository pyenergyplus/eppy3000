# Copyright (c) 2021 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""py.test for installlocation"""

import pytest
from eppy3000 import installlocation


@pytest.mark.parametrize(
    "version, expected",
    [
        ("9.0.0", "9-0-0"),  # version, expected
        ("9.0.1", "9-0-1"),  # version, expected
        ("9.2.3", "9-2-3"),  # version, expected
        ("9.2", "9-2-0"),  # version, expected
        ("9", "9-0-0"),  # version, expected
    ],
)
def test_version2folder(version, expected):
    """py.test for version2folder"""
    result = installlocation.version2folder(version)
    assert result == expected


@pytest.mark.parametrize(
    "version, platform_system, expected",
    [
        (
            "9.3",
            "Darwin",
            "/Applications/EnergyPlus-9-3-0",
        ),  # version, platform_system, expected
        ("9.3", "Windows", "C:/EnergyPlusV9-3-0"),  # version, platform_system, expected
        (
            "9.3",
            "Linux",
            "/usr/local/EnergyPlus-9-3-0",
        ),  # version, platform_system, expected
    ],
)
def test_installfolder(version, platform_system, expected):
    """py.test for installfolder"""
    result = installlocation.installfolder(version, platform_system)
    assert result == expected


@pytest.mark.parametrize(
    "version, platform_system, expected",
    [
        (
            "9.3",
            "Darwin",
            "/Applications/EnergyPlus-9-3-0/Energy+.schema.epJSON",
        ),  # version, platform_system, expected
        (
            "9.3",
            "Windows",
            "C:/EnergyPlusV9-3-0/Energy+.schema.epJSON",
        ),  # version, platform_system, expected
        (
            "9.3",
            "Linux",
            "/usr/local/EnergyPlus-9-3-0/Energy+.schema.epJSON",
        ),  # version, platform_system, expected
    ],
)
def test_schemapath(version, platform_system, expected):
    """py.test for schemapath"""
    result = installlocation.schemapath(version, platform_system)
    assert result == expected
