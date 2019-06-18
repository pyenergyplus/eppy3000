# Copyright (c) 2019 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""py.test for epMunch"""

import json
from io import StringIO

import eppy3000.readepj as readepj
from eppy3000 import epMunch
from eppy3000.epschema import EPSchemaMunch


def test_printkey():
    """py.test for printkey"""
    data = (
        ("Gumby", None, None,
            ["", "", "Gumby"]),  # key, indent, formatstr, expected
        ("Gumby", 1, None,
            ["", "    Gumby"]),  # key, indent, formatstr, expected
        ("Gumby", None, "{}{}",
            ["", "", "Gumby"]),  # key, indent, formatstr, expected
        ("Gumby", None, "{}{},",
            ["", "", "Gumby,"]),  # key, indent, formatstr, expected
    )
    for key, indent, formatstr, expected in data:
        result = []
        epMunch.printkey(key, indent, formatstr, func=result.append)
        assert result == expected


def test_printkey_withprint(capsys):
    """py.est for printkey when func=None"""
    key, indent, formatstr, expected = ("Gumby", None, None,
                                        '\n\nGumby\n')
    epMunch.printkey(key, indent, formatstr)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_printmunch():
    """py.test for printmunch"""
    data = (
        (dict(a=dict(aa=dict(z=-1, y=-2))), 0, None,
        ['',
         'a                                                !-  EP_KEY',
         '            aa                                   !-  EPJOBJECT_NAME',
         '            -1                                   !-  z',
         '            -2                                   !-  y']
        ),  # dct, indent, index, expected
        (dict(a=dict(aa=dict(z=-1, y=[dict(zz=1), dict(zz=2)]))),
        0, None,
        ['',
         'a                                                !-  EP_KEY',
         '            aa                                   !-  EPJOBJECT_NAME',
         '            -1                                   !-  z',
         '                                                 !-  y',
         '                1                                    !-  zz #1',
         '                2                                    !-  zz #2']
        ),  # dct, indent, index, expected
        (dict(a=dict(aa=dict(z=-1, y=-2))),
        0, 3,
        ['',
         'a                                                !-  EP_KEY',
         '            aa                                   !-  EPJOBJECT_NAME',
         '            -1                                   !-  z #3',
         '            -2                                   !-  y #3']
        ),  # dct, indent, index, expected
        (dict(a=dict(aa=dict(z=-1, y=-2))),
        0, None,
        ['',
         'a                                                !-  EP_KEY',
         '            aa                                   !-  EPJOBJECT_NAME',
         '            -1                                   !-  z',
         '            -2                                   !-  y']
        ),  # dct, indent, index, expected
    )  # noqa: E501
    for dct, indent, index, expected in data:
        dctstr = json.dumps(dct)
        fhandle = StringIO(dctstr)
        amunch = readepj.readepjjson(fhandle)
        result = []
        epMunch.printmunch(amunch, indent, index, result.append)
        assert result == expected


def test_printmunch_withprint(capsys):
    """py.test for printmunch with print"""
    (dct, indent, index, expected) = (
        dict(a=dict(aa=dict(z=-1, y=-2))),
        0, None,
        '\n'.join(
            ['',
             'a                                                !-  EP_KEY',
             '            aa                                   !-  EPJOBJECT_NAME',  # noqa: E501
             '            -1                                   !-  z',
             '            -2                                   !-  y'])
        )
    dctstr = json.dumps(dct)
    fhandle = StringIO(dctstr)
    amunch = readepj.readepjjson(fhandle)
    epMunch.printmunch(amunch, indent, index)
    captured = capsys.readouterr()
    assert captured.out == expected + '\n'


def test_printmunch_ofEPSchema():
    """py.test for printmunch id you try to print EPSchemaMunch"""
    amunch = EPSchemaMunch(dict(a=1))
    expected = []
    result = []
    epMunch.printmunch(amunch)
    assert result == expected


class TestEPMunch(object):
    """py.test for EPMunch"""
    def setup(self):
        dct = dict(a=dict(aa=dict(z=-1, y=-2)))
        dctstr = json.dumps(dct)
        fhandle = StringIO(dctstr)
        self.amunch = readepj.readepjjson(fhandle)

    def test_repr(self):
        """py.test for EPMunch.__repr__"""
        lst = [
            '',
            'a                                                !-  EP_KEY',
            '            aa                                   !-  EPJOBJECT_NAME',  # noqa: E501
            '            -1                                   !-  z',
            '            -2                                   !-  y'
        ]
        expected = "\n".join(lst)
        result = self.amunch.__repr__()
        assert result == expected

    def test_str(self):
        """py.test for EPMunch.__str__"""
        lst = [
            '',
            'a                                                !-  EP_KEY',
            '            aa                                   !-  EPJOBJECT_NAME',  # noqa: E501
            '            -1                                   !-  z',
            '            -2                                   !-  y'
        ]
        expected = "\n".join(lst)
        result = self.amunch.__str__()
        assert result == expected
