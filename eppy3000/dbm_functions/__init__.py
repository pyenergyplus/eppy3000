# Copyright (c) 2022 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

"""This module contains functions that work DBM database

- The "Energy+.schema.epJSON" is stored in DBM
- "Energy+.schema.epJSON" is indexed for 'references' and 'object_list' and the indices are stored in DBM
- This module contains code to do the following:
    + write "Energy+.schema.epJSON" into DBM
    + create the index and save into DBM
    + Read the DBM
    + use the indices in DBM"""
