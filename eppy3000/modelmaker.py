# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""same as modelmaker in eppy"""

class IDF(object):
    def __init__(self, idfname=None, epw=None):
        super(IDF, self).__init__()
        self.idfname = idfname
        self.epw = epw


