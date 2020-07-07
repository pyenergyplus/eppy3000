# Copyright (c) 2020 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""convert an idf file into an epj file
Quick script to be used during development.

Remove this later
"""

import eppy
import eppy3000.oldeppy as oldeppy


inname = "./eppy3000/resources/snippets/V9_3/constructions.idf"
outname = "./eppy3000/resources/snippets/V9_3/constructions.epJSON"
epschema = './eppy3000/resources/schema/V9_3/Energy+.schema.epJSON'


idf = eppy.openidf(inname)
epj = oldeppy.idf2epj(idf, open(epschema, 'r'))
epj.saveas(outname)

