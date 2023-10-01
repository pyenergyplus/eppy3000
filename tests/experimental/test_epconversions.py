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


@pytest.mark.parametrize(
    "expected",
    [
        (
            [
                "$/(W/K)",
                "$/(m3/s)",
                "$/kW",
                "$/m2",
                "$/m3",
                "(kg/s)/W",
                "1/K",
                "1/hr",
                "1/m",
                "A",
                "A/K",
                "A/V",
                "Ah",
                "Availability",
                "C",
                "Control",
                "GJ",
                "J",
                "J/J",
                "J/K",
                "J/kg",
                "J/kg-K",
                "J/kg-K2",
                "J/kg-K3",
                "J/m2-K",
                "J/m3",
                "J/m3-K",
                "K",
                "K/m",
                "L/GJ",
                "L/MJ",
                "L/day",
                "L/kWh",
                "Mode",
                "N-m",
                "N-s/m2",
                "Pa",
                "V",
                "V/K",
                "VA",
                "W",
                "W/((m3/s)-Pa)",
                "W/(m3/s)",
                "W/K",
                "W/W",
                "W/m",
                "W/m-K",
                "W/m-K2",
                "W/m-K3",
                "W/m2",
                "W/m2-K",
                "W/m2-K2",
                "W/person",
                "W/s",
                "cm",
                "cm2",
                "cycles/hr",
                "days",
                "deg",
                "deltaC",
                "deltaC/hr",
                "deltaJ/kg",
                "dimensionless",
                "eV",
                "g/GJ",
                "g/MJ",
                "g/kg",
                "g/m-s",
                "g/m-s-K",
                "g/mol",
                "hr",
                "kJ/kg",
                "kPa",
                "kg",
                "kg-H2O/kg-air",
                "kg/J",
                "kg/Pa-s-m2",
                "kg/kg",
                "kg/kg-K",
                "kg/m",
                "kg/m-s",
                "kg/m-s-K",
                "kg/m-s-K2",
                "kg/m2",
                "kg/m3",
                "kg/s",
                "kg/s-m",
                "kg/s2",
                "kmol",
                "kmol/s",
                "lux",
                "m",
                "m/hr",
                "m/s",
                "m/yr",
                "m2",
                "m2-K/W",
                "m2/m",
                "m2/person",
                "m2/s",
                "m3",
                "m3/GJ",
                "m3/MJ",
                "m3/hr",
                "m3/hr-m2",
                "m3/hr-person",
                "m3/kg",
                "m3/m2",
                "m3/m3",
                "m3/person",
                "m3/s",
                "m3/s-W",
                "m3/s-m",
                "m3/s-m2",
                "m3/s-person",
                "micron",
                "minutes",
                "ms",
                "ohms",
                "percent",
                "percent/K",
                "person/m2",
                "ppm",
                "rev/min",
                "s",
                "s/m",
                "years",
            ]
        ),  # expected
    ],
)
def tAest_allsiunits(expected):
    """pytest for allsiunits"""
    result = epconversions.allsiunits()
    assert result == expected


@pytest.mark.parametrize(
    "expected",
    [
        (
            [
                "$",
                "$/(Btu/h-F)",
                "$/(ft3/min)",
                "$/(kBtuh/h)",
                "$/ft2",
                "$/ft3",
                "(ft3/min)/(Btu/h)",
                "(gal/min)/(Btu/h)",
                "(lbm/sec)/(Btu/hr)",
                "1/F",
                "1/ft",
                "1/hr",
                "A",
                "A/F",
                "A/V",
                "Ah",
                "Availability",
                "Btu-in/h-ft2-F",
                "Btu/F",
                "Btu/ft2-F",
                "Btu/ft3",
                "Btu/ft3-F",
                "Btu/h",
                "Btu/h-F",
                "Btu/h-F2-ft",
                "Btu/h-F3-ft",
                "Btu/h-ft",
                "Btu/h-ft-F",
                "Btu/h-ft2",
                "Btu/h-ft2-F",
                "Btu/h-ft2-F2",
                "Btu/h-person",
                "Btu/lb",
                "Btu/lb-F",
                "Btu/lb-F2",
                "Btu/lb-F3",
                "C",
                "Control",
                "F",
                "F/ft",
                "J/J",
                "Mode",
                "Pa",
                "R",
                "V",
                "V/F",
                "VA",
                "W",
                "W/((ft3/min)-inH2O)",
                "W/((gal/min)-ftH20)",
                "W/(ft3/min)",
                "W/(gal/min)",
                "W/W",
                "W/ft2",
                "W/m2",
                "W/person",
                "W/s",
                "Wh",
                "cycles/hr",
                "days",
                "deg",
                "deltaBtu/lb",
                "deltaF",
                "deltaF/hr",
                "dimensionless",
                "eV",
                "foot-candles",
                "ft",
                "ft/hr",
                "ft/min",
                "ft2",
                "ft2-F-hr/Btu",
                "ft2/ft",
                "ft2/person",
                "ft2/s",
                "ft3",
                "ft3/MWh",
                "ft3/ft2",
                "ft3/hr",
                "ft3/hr-ft2",
                "ft3/hr-person",
                "ft3/kWh",
                "ft3/lb",
                "ft3/min",
                "ft3/min-ft",
                "ft3/min-ft2",
                "ft3/min-person",
                "ft3/person",
                "ftH2O",
                "gal",
                "gal/ft2",
                "gal/hr",
                "gal/hr-ft2",
                "gal/hr-person",
                "gal/kWh",
                "gal/min",
                "gal/min-ft",
                "gal/person",
                "grains/lb",
                "hr",
                "in",
                "inH2O",
                "inHg",
                "inch/yr",
                "inch2",
                "kg-H2O/kg-air",
                "kg/kg",
                "kmol",
                "kmol/s",
                "lb",
                "lb/Btu",
                "lb/MWh",
                "lb/ft",
                "lb/ft-s",
                "lb/ft-s-F",
                "lb/ft-s-F2",
                "lb/ft2",
                "lb/ft3",
                "lb/lb-F",
                "lb/mol",
                "lb/psi-s-ft2",
                "lb/s",
                "lb/s-ft",
                "lb/s2",
                "lbf-in",
                "lbf-s/ft2",
                "m3/m3",
                "micron",
                "miles/hr",
                "minutes",
                "ms",
                "ohms",
                "percent",
                "percent/F",
                "person/ft2",
                "pint/day",
                "pint/kWh",
                "ppm",
                "psi",
                "rev/min",
                "s",
                "s/ft",
                "ton-hrs",
                "years",
            ]
        ),  # expected
    ],
)
def tAest_allipunits(expected):
    """pytest for allipunits"""
    result = epconversions.allipunits()
    assert result == expected


@pytest.mark.parametrize(
    "siunits, expected",
    [
        ("m", ["ft", "in"]),  # siunits, expected
    ],
)
def test_getipunits(siunits, expected):
    """py.test for getipunits"""
    result = epconversions.getipunits(siunits)
    assert set(result) == set(expected)  # using set since order is undefined
