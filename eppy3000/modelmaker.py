# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""same as modelmaker in eppy"""

from munch import Munch
from eppy3000.readidf import readidfjson
from eppy3000.readidf import removeeppykeys

class IDF(object):
    def __init__(self, idfname=None, epw=None):
        super(IDF, self).__init__()
        self.idfname = idfname
        self.epw = epw
        self.read()
        
    def read(self):
        """read the idf file"""    
        self.idf = readidfjson(self.idfname)
        self.idfobjects = {key:[val1 for val1 in val.values()] 
                                for key, val in self.idf.items()}
        
    def __repr__(self):
        """print this"""
        return self.idf.__repr__()
        
    def saveas(self, filename):
        """saveas in filename"""
        self.idfname = filename
        self.save(filename)

    def save(self, filename=None):
        """save the file"""
        if not filename:
            filename = self.idfname
        with open(filename, 'w') as fhandle:
            tosave = self.idf.toDict()
            tosave = Munch.fromDict(tosave)
            removeeppykeys(tosave)
            fhandle.write(tosave.toJSON())
