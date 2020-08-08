# Copyright (c) 2018-2019 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""read epj json file and have eppy like functionality"""

import json

# one works from ipython, the other from the script
# try:
#     from eppy3000.epMunch import EPMunch
# except ModuleNotFoundError as e:
#     from epMunch import EPMunch
from eppy3000.epMunch import EPMunch


def readepjjson(fhandle):
    """read an json epj

    Parameters
    ----------
    fhandle: io.String, io.TextIOWrapper
        can be a file open for read or a io.StringIO object

    Returns
    -------
    eppy.EPMunch
    """
    try:
        fhandle = open(fhandle, "r")
    except TypeError as e:
        pass
    as_json = json.load(fhandle)
    as_munch = EPMunch.fromDict(as_json)
    addeppykeys(as_munch)
    return as_munch


def addeppykeys(epmunch):
    """adds eppykeys needed by eppy3000

    The way E+ json is structured:

    - the lowest branch on the json tree is the epobject
    - once you are in the epobject:
        - the epobject will not know:
            1. Its own name
            2. the type of object it is
        - it will know only its own fields

    We add two new keys to the epobject that will
    let it store its name and object type
    These names start with `eppy` to make it clear that
    eppy300 has added them

    - eppykey -> stores the E+ object type (epkey)
    - eppyname -> stores the name of the object. its key in E+ json

    Parameters
    ----------
    epmunch: eppy3000.epMunch.EPMunch
        This is the E+ file as seen by eppy3000

    Returns
    -------
    None

    """
    for key, epobjects in epmunch.items():
        for name, epobject in epobjects.items():
            epobject["eppykey"] = key
            epobject["eppyname"] = name
            epobject["eppy_epobjects"] = epobjects


def removeeppykeys(epmunch, rkeys=None):
    """remove the eppykeys

    This will remove all the additional keys that eppy added
    in addeppykeys(). This is usually called before saving

    Parameters
    ----------
    epmunch: eppy3000.epMunch.EPMunch
        This is the E+ file as seen by eppy3000
    rkeys: list
        These are the keys to be removed. if rkeys is None then
        rkeys is set to ['eppykey', 'eppyname', 'eppy_objepschema']

    Returns
    -------
    None
    """
    if not rkeys:
        rkeys = [
            "eppykey",
            "eppyname",
            "eppy_objepschema",
            "eppy_epj",
            "eppy_epobjects",
        ]
    for key, epobjects in epmunch.items():
        for name, epobject in epobjects.items():
            for rkey in rkeys:
                epobject.pop(rkey, None)
