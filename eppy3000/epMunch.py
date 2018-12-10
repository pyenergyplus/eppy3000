# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""subclass Munch"""

from munch import Munch


class EPMunch(Munch):
    """Subclass of Munch for eppy3000"""
    def __init__(self, *args, **kwargs):
        super(EPMunch, self).__init__(*args, **kwargs)


