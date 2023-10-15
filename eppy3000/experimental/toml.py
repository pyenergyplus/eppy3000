# Copyright (c) 2023 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""read and write rpj->toml and toml->epj"""
import tomli
import tomli_w
import json
from eppy3000.modelmaker import EPJ
from io import StringIO


def toml2epj(tomlstr):
    """convert a toml string to epj"""
    dct = tomli.load(open("a.toml", "rb"))
    jsonstr = json.dumps(dct, indent=4)
    return EPJ(StringIO(jsonstr))

def epj2toml(epj):
    """output a formated toml string"""
    epjjson  = epj.jsonstr()
    dct = json.loads(epjjson)
    return tomli_w.dumps(dct)

def readtoml(fname):
    """read a toml fil into epj"""
    dct = tomli.load(open(fname, 'rb'))
    jsonstr = json.dumps(dct, indent=4)
    return EPJ(StringIO(jsonstr))

def writetoml(epj, fname):
    """write an epj file to toml"""
    epjjson  = epj.jsonstr()
    dct = json.loads(epjjson)
    tomli_w.dump(dct, open(fname, 'wb'))

