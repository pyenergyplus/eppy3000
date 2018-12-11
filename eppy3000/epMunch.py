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

    def __repr__(self):
        """print this as a snippet"""
        lines = []
        for key, val in self.items():
            print(key, val)
            try:
                lines.append("{0: <16} !-  {1}".format(val, key))
            except TypeError as e:
                raise e
                # lines.append("    {0: <16} !-  {1}".format("", '-'*8))
                # lines.append("    {0: <16} !-  {1}".format("", key))
                # for item in self[key]:
                #     for key1, val1 in item.items():
                #         lines.append("    {0: <16} !-  {1}".format(val1, key1))
                # lines.append("    {0: <16} !-  {1}".format("", '-'*8))
        astr = '\n'.join(lines)
        return '\n%s\n' % (astr,)


    def __str__(self):
        """same as __repr__"""
        return self.__repr__()
