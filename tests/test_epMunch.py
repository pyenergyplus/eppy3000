# Copyright (c) 2019-2020 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""py.test for epMunch"""

import json
from io import StringIO
import pytest

import eppy3000.readepj as readepj
from eppy3000 import epMunch
from eppy3000.epschema import EPSchemaMunch
from munch import Munch
from eppy3000.readepj import removeeppykeys


def test_printkey():
    """py.test for printkey"""
    data = (
        ("Gumby", None, None, ["", "", "Gumby"]),  # key, indent, formatstr, expected
        ("Gumby", 1, None, ["", "    Gumby"]),  # key, indent, formatstr, expected
        ("Gumby", None, "{}{}", ["", "", "Gumby"]),  # key, indent, formatstr, expected
        (
            "Gumby",
            None,
            "{}{},",
            ["", "", "Gumby,"],
        ),  # key, indent, formatstr, expected
    )
    for key, indent, formatstr, expected in data:
        result = []
        epMunch.printkey(key, indent, formatstr, func=result.append)
        assert result == expected


def test_printkey_withprint(capsys):
    """py.est for printkey when func=None"""
    key, indent, formatstr, expected = ("Gumby", None, None, "\n\nGumby\n")
    epMunch.printkey(key, indent, formatstr)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_printmunch():
    """py.test for printmunch"""
    data = (
        (
            dict(a=dict(aa=dict(z=-1, y=-2))),
            0,
            None,
            [
                "",
                "a                                                !-  EP_KEY         # use .eppykey",
                "            aa                                   !-  EPJOBJECT_NAME # use .eppyname",
                "            -1                                   !-  z",
                "            -2                                   !-  y",
            ],
        ),  # dct, indent, index, expected
        (
            dict(a=dict(aa=dict(z=-1, y=[dict(zz=1), dict(zz=2)]))),
            0,
            None,
            [
                "",
                "a                                                !-  EP_KEY         # use .eppykey",
                "            aa                                   !-  EPJOBJECT_NAME # use .eppyname",
                "            -1                                   !-  z",
                "                                                 !-  y",
                "                1                                    !-  zz #1",
                "                2                                    !-  zz #2",
            ],
        ),  # dct, indent, index, expected
        (
            dict(a=dict(aa=dict(z=-1, y=-2))),
            0,
            3,
            [
                "",
                "a                                                !-  EP_KEY         # use .eppykey",
                "            aa                                   !-  EPJOBJECT_NAME # use .eppyname",
                "            -1                                   !-  z #3",
                "            -2                                   !-  y #3",
            ],
        ),  # dct, indent, index, expected
        (
            dict(a=dict(aa=dict(z=-1, y=-2))),
            0,
            None,
            [
                "",
                "a                                                !-  EP_KEY         # use .eppykey",
                "            aa                                   !-  EPJOBJECT_NAME # use .eppyname",
                "            -1                                   !-  z",
                "            -2                                   !-  y",
            ],
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
        0,
        None,
        "\n".join(
            [
                "",
                "a                                                !-  EP_KEY         # use .eppykey",
                "            aa                                   !-  EPJOBJECT_NAME # use .eppyname",  # noqa: E501
                "            -1                                   !-  z",
                "            -2                                   !-  y",
            ]
        ),
    )
    dctstr = json.dumps(dct)
    fhandle = StringIO(dctstr)
    amunch = readepj.readepjjson(fhandle)
    epMunch.printmunch(amunch, indent, index)
    captured = capsys.readouterr()
    assert captured.out == expected + "\n"


def test_printmunch_ofEPSchema():
    """py.test for printmunch id you try to print EPSchemaMunch"""
    amunch = EPSchemaMunch(dict(a=1))
    expected = []
    result = []
    epMunch.printmunch(amunch)
    assert result == expected


@pytest.mark.usefixtures("simplemunch")
class TestEPMunch_simple(object):
    """py.test for EPMunch"""


    def test_repr(self):
        """py.test for EPMunch.__repr__"""
        lst = [
            "",
            "a                                                !-  EP_KEY         # use .eppykey",
            "            aa                                   !-  EPJOBJECT_NAME # use .eppyname",  # noqa: E501
            "            -1                                   !-  z",
            "            -2                                   !-  y",
        ]
        expected = "\n".join(lst)
        result = self.amunch.__repr__()
        assert result == expected

    def test_str(self):
        """py.test for EPMunch.__str__"""
        lst = [
            "",
            "a                                                !-  EP_KEY         # use .eppykey",
            # should self.epobjects be updated here
            "            aa                                   !-  EPJOBJECT_NAME # use .eppyname",  # noqa: E501
            "            -1                                   !-  z",
            "            -2                                   !-  y",
        ]
        expected = "\n".join(lst)
        result = self.amunch.__str__()
        assert result == expected


@pytest.fixture
def simplemunch(request):
    """simple epmuch for tests"""
    dct = dict(a=dict(aa=dict(z=-1, y=-2)))
    dctstr = json.dumps(dct)
    fhandle = StringIO(dctstr)
    amunch = readepj.readepjjson(fhandle)
    # print('\n-----------------')
    # print('fixturename : %s' % request.fixturename)
    # print('scope       : %s' % request.scope)
    # print('function    : %s' % request.function.__name__)
    # print('cls         : %s' % request.cls)
    # print('module      : %s' % request.module.__name__)
    # print('fspath      : %s' % request.fspath)
    # print('-----------------')

    request.cls.amunch = amunch
    # see this link for more on how request works
    # https://docs.pytest.org/en/stable/fixture.html#request-context
    # still not clear to me right now
    #
    # You can pick up amunch in the test as self.amunch

    # print('\n-----------------')
    # print('fixturename : %s' % request.fixturename)
    # print('scope       : %s' % request.scope)
    # print('function    : %s' % request.function.__name__)
    # print('cls         : %s' % request.cls)
    # print('module      : %s' % request.module.__name__)
    # print('fspath      : %s' % request.fspath)
    # print('-----------------')
    yield


@pytest.mark.usefixtures("simplemunch")
class TestEPMunch_simple1(object):
    """py.test for EPMunch"""

    # add an eppy_ field
    # change and eppy_field
    # test to see if it works
    @pytest.mark.parametrize(
        "fname, fvalue, expected",
        [
            ("eppy_field", 52, 52),
        ],  # fname, fvalue, expected
    )
    def test_add_eppy_field(self, fname, fvalue, expected):
        """test adding a field that starts with 'eppy'"""
        # start with epMunch objects that are not epobjects
        # add a key, value
        self.amunch[fname] = fvalue
        assert self.amunch[fname] == expected
        self.amunch.eppy_hardcoded = fvalue
        assert self.amunch["eppy_hardcoded"] == expected
        # change a value
        newvalue = "new value"
        self.amunch[fname] = newvalue
        assert self.amunch[fname] == newvalue  # since it is not an epobject
        # it should change
        self.amunch.eppy_hardcoded = newvalue
        assert self.amunch.eppy_hardcoded == newvalue  # value should not change
        #
        # Now test epMunch objects that are epobjects
        # add a key, value
        #
        self.amunch.a.aa[fname] = fvalue
        assert self.amunch.a.aa[fname] == expected
        self.amunch.a.aa.eppy_hardcoded = fvalue
        assert self.amunch.a.aa["eppy_hardcoded"] == expected
        # change a value
        newvalue = "new value"
        self.amunch.a.aa[fname] = newvalue
        assert self.amunch.a.aa[fname] == expected  # since it is an epobject
        # it should not change
        self.amunch.a.aa.eppy_hardcoded = newvalue
        assert self.amunch.a.aa.eppy_hardcoded == expected  # since it is an epobject
        # it should not change


def test_change_eppyname():
    """pytest for changing eppyname"""
    # make the epmunch
    dct = dict(a=dict(aa=dict(z=-1, y=-2), bb=dict(z=1, y=2)))
    dctstr = json.dumps(dct)
    fhandle = StringIO(dctstr)
    amunch = readepj.readepjjson(fhandle)
    aa = amunch.a.aa
    aa["eppyname"] = "cc"
    # aa.eppyname = 'cc'
    assert aa == amunch.a.cc
    cc = amunch.a.cc
    # cc['eppyname'] = 'dd'
    cc.eppyname = "dd"
    assert cc == amunch.a.dd
    amunch.a.dd.z = 55
    dct = dict(a=dict(dd=dict(z=55, y=-2), bb=dict(z=1, y=2)))
    dctstr = json.dumps(dct)
    fhandle = StringIO(dctstr)
    bmunch = readepj.readepjjson(fhandle)
    # assert amunch == bmunch

    # remove eppykeys beflore comparison.
    # otherwise it go into a recursive loop because of 'eppy_epobjects'
    amunchd = amunch.toDict()
    amunchd = Munch.fromDict(amunchd)
    removeeppykeys(amunchd)
    bmunchd = bmunch.toDict()
    bmunchd = Munch.fromDict(bmunchd)
    removeeppykeys(bmunchd)

    assert amunchd == bmunchd


def test_delete():
    """py.test for EPMunch.delete"""
    # make the epmunch
    dct = dict(a=dict(aa=dict(z=-1, y=-2), bb=dict(z=1, y=2)))
    dctstr = json.dumps(dct)
    fhandle = StringIO(dctstr)
    amunch = readepj.readepjjson(fhandle)
    amunch.a.aa.delete()
    assert list(amunch.a.bb.eppy_epobjects.keys()) == ["bb"]
    # test when it not an epobject
    with pytest.raises(epMunch.NotEPObject):
        amunch.a.delete()
    amunch["a"]["bb"].delete()  # test when bb is not an attribute
    assert list(amunch.a.keys()) == []
