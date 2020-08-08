# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""py.test for readepj.py"""

import json
from io import StringIO
import eppy3000.readepj as readepj
from eppy3000.epMunch import EPMunch


def test_readepjjson():
    """py.test for readepjjson"""
    dct = dict(
        a=dict(aa=dict(z=-1, y=-2), bb=dict(zz=-11, yy=-22)),
        b=dict(cc=dict(ab=12, bc=23), dd=dict(cd=34, de=45)),
    )
    dctstr = json.dumps(dct)
    fhandle = StringIO(dctstr)
    result = readepj.readepjjson(fhandle)
    assert isinstance(result, EPMunch)


def test_addeppykeys():
    """py.test for addeppykeys"""
    dct = dict(
        a=dict(aa=dict(z=-1, y=-2), bb=dict(zz=-11, yy=-22)),
        b=dict(cc=dict(ab=12, bc=23), dd=dict(cd=34, de=45)),
    )
    dctstr = json.dumps(dct)
    fhandle = StringIO(dctstr)
    epmunch = readepj.readepjjson(fhandle)
    epobject = epmunch.a.aa
    assert "eppykey" in epobject
    assert "eppyname" in epobject


def test_removeeppykeys():
    """py.test for removeeppykeys"""
    dct = dict(
        a=dict(aa=dict(z=-1, y=-2), bb=dict(zz=-11, yy=-22)),
        b=dict(cc=dict(ab=12, bc=23), dd=dict(cd=34, de=45)),
    )
    dctstr = json.dumps(dct)
    # test for rkeys=None
    fhandle = StringIO(dctstr)
    epmunch = readepj.readepjjson(fhandle)
    readepj.removeeppykeys(epmunch)
    epobject = epmunch.a.aa
    assert "eppykey" not in epobject
    assert "eppyname" not in epobject
    # test for rkeys=['eppykey']
    fhandle = StringIO(dctstr)
    epmunch = readepj.readepjjson(fhandle)
    readepj.removeeppykeys(epmunch, rkeys=["eppykey"])
    epobject = epmunch.a.aa
    assert "eppykey" not in epobject
    assert "eppyname" in epobject
