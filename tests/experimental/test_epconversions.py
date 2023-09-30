# Copyright (c) 2023 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""pytest for epconversions"""
import pytest
import eppy3000.experimental.epconversions as epconversions


@pytest.mark.parametrize(
    "val, siunits, ipunits, unitstr, wrapin, expected",
    [
        # unitstr=False
        (
            3,
            "m",
            None,
            False,
            None,
            3 * 3.28083989501312,
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            "autocalculate",
            "m",
            None,
            False,
            None,
            "autocalculate",
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            3,
            "m",
            "in",
            False,
            None,
            3 * 39.3700787401575,
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            3,
            None,
            None,
            False,
            None,
            3,
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            30,
            "deg",
            None,
            False,
            None,
            30,
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            30,
            "unknown",
            None,
            False,
            None,
            30,
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            30,
            "C",
            None,
            False,
            None,
            30 * 1.8 + 32,
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        # unitstr=True
        (
            3,
            "m",
            None,
            True,
            None,
            (3 * 3.28083989501312, "ft"),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            "autocalculate",
            "m",
            None,
            True,
            None,
            ("autocalculate", "ft"),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            3,
            "m",
            "in",
            True,
            None,
            (3 * 39.3700787401575, "in"),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            3,
            None,
            None,
            True,
            None,
            (3, ""),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            30,
            "deg",
            None,
            True,
            None,
            (30, "deg"),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            30,
            "unknown",
            None,
            True,
            None,
            (30, "unknown"),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        # unitstr=True, wrapin='[X]'
        (
            3,
            "m",
            None,
            True,
            "[X]",
            (3 * 3.28083989501312, "[ft]"),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            "autocalculate",
            "m",
            None,
            True,
            "[X]",
            ("autocalculate", "[ft]"),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            3,
            "m",
            "in",
            True,
            "[X]",
            (3 * 39.3700787401575, "[in]"),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            3,
            None,
            None,
            True,
            "[X]",
            (3, ""),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            30,
            "deg",
            None,
            True,
            "[X]",
            (30, "[deg]"),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            30,
            "unknown",
            None,
            True,
            None,
            (30, "unknown"),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
        (
            30,
            "dimensionless",
            None,
            True,
            None,
            (30, "dimensionless"),
        ),  # val, siunits, ipunits, unitstr, wrapin, expected
    ],
)
def test_add(val, siunits, ipunits, unitstr, wrapin, expected):
    result = epconversions.convert2ip(val, siunits, ipunits, unitstr, wrapin)
    assert result == expected


@pytest.mark.parametrize(
    "val, ipunits, isunits, unitstr, wrapin, expected",
    [
        # unitstr=False
        (
            3,
            "lb/MWh",
            None,
            False,
            None,
            3 / 0.00793664091373665,
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        (
            "autocalculate",
            "ft",
            None,
            False,
            None,
            "autocalculate",
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        (
            3,
            "lb/MWh",
            "g/MJ",
            False,
            None,
            3 / 7.93664091373665,
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        (
            3,
            None,
            None,
            False,
            None,
            3,
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        (
            30,
            "deg",
            None,
            False,
            None,
            30,
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        (
            30,
            "unknown",
            None,
            False,
            None,
            30,
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        (
            80,
            "F",
            None,
            False,
            None,
            (80 - 32) / 1.8,
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        # unitstr=True
        (
            3,
            "ft",
            None,
            True,
            None,
            (3 / 3.28083989501312, "m"),
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        (
            "autocalculate",
            "ft",
            None,
            True,
            "[X]",
            ("autocalculate", "[m]"),
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        (
            3,
            "lb/MWh",
            "g/MJ",
            True,
            "[X]",
            (3 / 7.93664091373665, "[g/MJ]"),
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        (
            3,
            None,
            None,
            True,
            "[X]",
            (3, ""),
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        (
            30,
            "deg",
            None,
            True,
            "[X]",
            (30, "[deg]"),
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        (
            30,
            "unknown",
            None,
            True,
            None,
            (30, "unknown"),
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
        (
            30,
            "dimensionless",
            None,
            True,
            None,
            (30, "dimensionless"),
        ),  # val, ipunits, isunits, unitstr, wrapin, expected
    ],
)
def test_convert2si(val, ipunits, isunits, unitstr, wrapin, expected):
    """pytest for convert2si"""
    result = epconversions.convert2si(val, ipunits, isunits, unitstr, wrapin)
    assert result == expected
