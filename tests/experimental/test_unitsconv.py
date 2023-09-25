# Copyright (c) 2023 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""pytest for unitsconv.py"""

import pytest
import eppy3000.experimental.unitsconv as unitsconv

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5), # a, b, expected
    ]
)
def test_add(a, b, expected):
    result = unitsconv.add(a, b)
    assert result == expected
    
@pytest.mark.parametrize(
    "units, ipunits, expected",
    [
    ('m', None, ('ft', 3.28083989501312)), # units, ipunits, expected
    ('m', 'ft', ('ft', 3.28083989501312)), # units, ipunits, expected
    ('m', 'in', ('in', 39.3700787401575)), # units, ipunits, expected
    ('$', None, ('$', None)), # units, ipunits, expected
    (None, None, None), # units, ipunits, expected
    ]
)
def test_getconversiondata(units, ipunits, expected):
    """py.test for getconversiondata"""
    result = unitsconv.getconversiondata(units, ipunits)
    assert result == expected

@pytest.mark.parametrize(
    "val, conv, expected",
    [
#     (3, ('ft', 3.28083989501312), (3 * 3.28083989501312, '[ft]')), # val, conv, expected
#     (3, None, (3, '')), # val, conv, expected
#     ('autocalculate', ('ft', 3.28083989501312), ('autocalculate', '[ft]')), # val, conv, expected
    (3, ('F', ['1.8', '(plus', '32)']), (3 * 1.8 + 32, '[F]')), # val, conv, expected
    ]
)
def test_do_conversions(val, conv, expected):
    """pytest for do_conversions"""
    result = unitsconv.do_conversions(val,  conv)
    assert result == expected
