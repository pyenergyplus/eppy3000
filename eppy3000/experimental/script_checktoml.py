# Copyright (c) 2023 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""compare write toml with a read toml"""
# run this script from the root folder of eppy3000

import sys

# pathnameto_eppy = 'c:/eppy'
pathnameto_eppy = "./"
sys.path.append(pathnameto_eppy)

import eppy3000.experimental.toml as toml
import eppy3000.experimental.openidf as openidf
import tomli
import json

fname = "eppy3000/resources/epJSON/V9_6/ShopWithPVandBattery.idf"
wfile = "eppy3000/resources/weatherfiles/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw"
outname = "a.toml"
epj = openidf.openidf(fname, wfile=wfile)

toml.writetoml(epj, outname)
epj1 = toml.readtoml(outname)
assert epj.jsonstr() == epj1.jsonstr()

