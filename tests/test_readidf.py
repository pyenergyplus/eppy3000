# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""py.test for readidf.py"""

import json
from io import StringIO
import eppy3000.readidf as readidf
from eppy3000.epMunch import EPMunch


def test_readidfjson():
    """py.test for readidfjson"""
    dct = dict(
            a=dict(aa=dict(z=-1, y=-2), bb=dict(zz=-11, yy=-22)),
            b=dict(cc=dict(ab=12, bc=23), dd=dict(cd=34, de=45)))
    dctstr = json.dumps(dct)
    fhandle = StringIO(dctstr)
    result = readidf.readidfjson(fhandle)
    assert isinstance(result, EPMunch)


def test_addeppykeys():
    """py.test for addeppykeys"""
    dct = dict(
            a=dict(aa=dict(z=-1, y=-2), bb=dict(zz=-11, yy=-22)),
            b=dict(cc=dict(ab=12, bc=23), dd=dict(cd=34, de=45)))
    dctstr = json.dumps(dct)
    fhandle = StringIO(dctstr)
    idfmunch = readidf.readidfjson(fhandle)
    epobject = idfmunch.a.aa
    assert 'eppykey' in epobject
    assert 'eppyname' in epobject


def test_removeeppykeys():
    """py.test for removeeppykeys"""
    dct = dict(
            a=dict(aa=dict(z=-1, y=-2), bb=dict(zz=-11, yy=-22)),
            b=dict(cc=dict(ab=12, bc=23), dd=dict(cd=34, de=45)))
    dctstr = json.dumps(dct)
    # test for rkeys=None
    fhandle = StringIO(dctstr)
    idfmunch = readidf.readidfjson(fhandle)
    readidf.removeeppykeys(idfmunch)
    epobject = idfmunch.a.aa
    assert 'eppykey' not in epobject
    assert 'eppyname' not in epobject
    # test for rkeys=['eppykey']
    fhandle = StringIO(dctstr)
    idfmunch = readidf.readidfjson(fhandle)
    readidf.removeeppykeys(idfmunch, rkeys=['eppykey'])
    epobject = idfmunch.a.aa
    assert 'eppykey' not in epobject
    assert 'eppyname' in epobject
