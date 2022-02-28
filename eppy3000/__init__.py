# -*- coding: utf-8 -*-
# Copyright (c) 2022 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""Top-level package for eppy3000."""

__author__ = """Santosh Philip"""
__email__ = "santosh@noemail.com"
__version__ = "0.1.13"

from io import StringIO
import pathlib
import os

from eppy3000.modelmaker import EPJ
from eppy3000.idfjsonconverter import getidfversion
from eppy3000.idfjsonconverter import idf2json
import eppy3000.installlocation as installlocation

from typing import Union
from os import PathLike


def openidf(idfpath: Union[str, PathLike[str]], 
            epjpath: Union[str, PathLike[str]]=None, 
            schemapath: Union[str, bytes, PathLike]=None,
            epjext: str=None) -> EPJ:
    """open and idf file as a epj file"""
    if not epjext:
        epjext = "epJSON"
    idfpath = pathlib.Path(idfpath)
    if not schemapath:
        with open(idfpath, "r") as idfhandle:
            version = getidfversion(idfhandle)
        schemapath = installlocation.schemapath(version)
    if not epjpath:
        epjpath = idfpath.with_suffix(f".{epjext}")
    schemahandle = open(schemapath, "r")
    idfhandle = open(idfpath, "r")
    epjtxt = idf2json(idfhandle, schemahandle)
    epj = EPJ(StringIO(epjtxt))
    epj.epjname = epjpath
    return epj


def newepj(version: str=None) -> EPJ:
    """open a new idf file

    easy way to open a new idf file for particular version. Works only if Energyplus of that version is installed.

    Parameters
    ----------
    version: string
        version of the new file you want to create. Will work only if this version of Energyplus has been installed.

    Returns
    -------
    idf
       file of type eppy.modelmake.IDF
    """  # noqa: E501
    if not version:
        version = "9.6"
    import eppy.easyopen as easyopen

    idfstring = """{{
    "Version": {{
        "Version 1": {{
            "version_identifier": "{}",
            "idf_order": 1
        }}
    }}
}}""".format(
        str(version)
    )
    fhandle = StringIO(idfstring)
    return EPJ(fhandle)
