# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""subclass Munch"""

from munch import Munch

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
    if not func:
        func = print
    for key, val in amunch.items():
        if isinstance(val, Munch):
            # printkey(key, indent, func=func)
            if 'eppykey' in val:
                func("")
                func('KEY  = {}'.format(val['eppykey']))
                func('NAME = {}'.format(val['eppyname']))
            printmunch(val, indent=indent+1, index=index, func=func)
        elif isinstance(val, list):
            printkey(key, indent=3, format= "{0}" + " " * 36 + " !-  {1}", func=func)
            for i, aval in enumerate(val):
                printmunch(aval, indent=indent+1, index=i+1, func=func)
        else:
            if index:
                astr = '{0}{1: <36} !-  {2} #{3}'
                func(astr.format(' '*4*indent, val, key, index))
            else:
                astr = '{0}{1: <36} !-  {2}'
                func(astr.format(' '*4*indent, val, key))

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
