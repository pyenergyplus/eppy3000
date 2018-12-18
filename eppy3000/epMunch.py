# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""subclass Munch"""

from munch import Munch
from eppy3000.idd import IDDMunch

def printkey(key, indent=0, format=None, func=None):
    if not func:
        func = print
    if not indent:
        func("")
        func("")
    elif indent == 1:
        func("")
    if not format:
        format = '{}{}'
        func(format.format(' '*4*indent, key))
    else:
        func(format.format(' '*4*indent, key))


def printmunch(amunch, indent=0, index=None, func=None):
    if isinstance(amunch, IDDMunch): # don't print IDD stuff
        return
    if not func:
        func = print
    if isinstance(amunch, Munch):
        if 'eppykey' in amunch:
            func("")
            func('{0: <36}{1} !-  {2}'.format(amunch['eppykey'],
                                        ' '*4*(indent+1),
                                        'KEY'))
            func('{0}{1: <36}{2} !-  {3}'.format(' '*4*(indent+1),
                                        amunch['eppyname'],
                                        ' '*4*(indent), 'NAME'))
    for key, val in amunch.items():
        if isinstance(val, Munch):
            printmunch(val, indent=indent+1, index=index,
                        func=func)
        elif isinstance(val, list):
            printkey(key, indent=3,
                    format= "{0}" + " " * 36 + " !-  {1}",
                    func=func)
            for i, aval in enumerate(val):
                printmunch(aval, indent=indent+1, index=i+1, func=func)
        elif key not in ['eppykey', 'eppyname', 'eppy_objidd']:
            if index:
                astr = '{0}{1: <36} !-  {2} #{3}'
                func(astr.format(' '*4*(indent+1), val, key, index))
            else:
                astr = '{0}{1: <36} !-  {2}'
                func(astr.format(' '*4*(indent+1), val, key))

class EPMunch(Munch):
    """Subclass of Munch for eppy3000"""
    def __init__(self, *args, **kwargs):
        super(EPMunch, self).__init__(*args, **kwargs)

    def __repr__(self):
        """print this as a snippet"""
        lines = []
        printmunch(self, func=lines.append)
        return "\n".join(lines)

    def __str__(self):
        """same as __repr__"""
        return self.__repr__()
