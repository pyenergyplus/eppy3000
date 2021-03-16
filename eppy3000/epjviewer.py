# Copyright (c) 2021 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""HTML viewer for EPJ and epMunch"""


import tempfile

try:
    from IPython.display import IFrame
except ModuleNotFoundError as e:
    pass
from munch import Munch
import json2html


class JupyterNotInstalled(Exception):
    pass


def removeeppykeys_inepmunch(epmunch, rkeys=None):
    """remove the eppy keys in epmunch"""
    if not rkeys:
        rkeys = [
            "eppykey",
            "eppyname",
            "eppy_objepschema",
            "eppy_epj",
            "eppy_epobjects",
        ]
    for rkey in rkeys:
        epmunch.pop(rkey, None)


def _epmunch2displaymunch(epmunch):
    """modify epmunch for display in HTML"""
    todict = epmunch.toDict()
    todict = Munch.fromDict(todict)
    eppykey = todict["eppykey"]
    eppyname = todict["eppyname"]
    removeeppykeys_inepmunch(todict)
    en = Munch()
    en[eppyname] = todict
    ek = Munch()
    ek[eppykey] = en
    return ek


def epmunch2dct(epmunch):
    """convert epmunch to and json string"""
    ek = _epmunch2displaymunch(epmunch)
    dct = ek.toDict()
    return dct


def epmunch2html(epmunch):
    """convert epmunch to an HTML table"""
    dct = epmunch2dct(epmunch)
    html = json2html.json2html.convert(json=dct)
    return html


def epmuchhtmllines(epmunch):
    """return the rows in the html table made from epmunch"""
    lines = 0
    for field in epmunch.epjfieldnames():
        if type(epmunch[field]) is list:
            lines += len(epmunch[field])
        else:
            lines += 1
    return lines


def epjhtmllines(epj):
    """return the number of rows in all the epmunch tables
    that make up the epj"""
    lines = 0
    for key in epj.epj.keys():
        for epmunch in epj.epobjects[key]:
            lines += epmuchhtmllines(epmunch)
    return lines


def epobjectslines(epobjects):
    """return the number of rows in all the epmunch tables
    that make up the epobjects"""
    lines = 0
    for epmunch in epobjects:
        lines += epmuchhtmllines(epmunch)
    return lines


def epmunch2ipythonhtml(epmunch, fname="./eppy3000_deletethis.html"):
    """display the epmunch as HTML table in jupyter notebook"""
    htmllines = epmuchhtmllines(epmunch)
    html = epmunch2html(epmunch)
    open(fname, "wb").write(html.encode())
    try:
        return IFrame(src=fname, width=800, height=30 * htmllines + 50)
    except NameError as e:
        raise JupyterNotInstalled


def epj2html(epj):
    """convert the epj to html"""
    epjjsonstr = epj.jsonstr()
    html = json2html.json2html.convert(json=epjjsonstr)
    return html


def epj2ipythonhtml(epj, fname="./eppy3000_deletethis.html"):
    """display the epj as HTML tables in jupyter notebook"""
    html = epj2html(epj)
    open(fname, "wb").write(html.encode())
    lines = epjhtmllines(epj)
    height = 30 * lines + 50
    try:
        return IFrame(src=fname, width=8000, height=height)
    except NameError as e:
        raise JupyterNotInstalled


def epobjects2dct(epobjects):
    """convert epobjects to dcts for display"""
    dct = {}
    for i, epmunch in enumerate(epobjects):
        eppykey = epmunch.eppykey
        eppyname = epmunch.eppyname
        displaymunch = _epmunch2displaymunch(epmunch)
        displaydict = displaymunch.toDict()
        for k1, val1 in displaydict.items():
            pass
        dct.setdefault(eppykey, dict())
        dct[eppykey].update(val1)
    return dct


def epobjects2html(epobjects):
    """convert epobjects to html"""
    dct = epobjects2dct(epobjects)
    html = json2html.json2html.convert(json=dct)
    return html


def epobjects2ipythonhtml(epobjects, fname="./eppy3000_deletethis.html"):
    """display the epobjects as HTML tables in jupyter notebook"""
    html = epobjects2html(epobjects)
    open(fname, "w").write(html)
    lines = epobjectslines(epobjects)
    height = 30 * lines + 50
    try:
        return IFrame(src=fname, width=800, height=height)
    except NameError as e:
        raise JupyterNotInstalled
