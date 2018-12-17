# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""class for the idd file"""

import json
from io import StringIO
from munch import Munch



class IDDMunch(Munch):
    """Munch subcalssed to for the IDD json"""
    def __init__(self, *args, **kwargs):
        super(IDDMunch, self).__init__(*args, **kwargs)
        
    def fieldnames(self):
        """field names of the IDD object"""
        return [key for key in self.keys()]
        
    def fieldnames_list(self):
        """fieldnames that contain lists"""
        pass

    def fieldproperty(self, fieldname):
        """field names of the IDD object"""
        return self[fieldname]
        
def readidd(fhandle):
    """read the idd json as a munch"""
    try:
        fhandle = open(fhandle, 'r')
    except TypeError as e:
        pass
    as_json = json.load(fhandle)
    as_munch = IDDMunch.fromDict(as_json) # 0.410 seconds
    return as_munch


class IDD(object):
    """hold the data from the json idd file """
    def __init__(self, iddname):
        super(IDD, self).__init__()
        self.iddname = iddname
        self.read()
        
    def read(self):
        """read the json file"""
        self.idd = readidd(self.iddname)
        self.version = self.idd['epJSON_schema_version']
        self.required = self.idd['required']
        self.iddobjects = {key:val['patternProperties']['.*']['properties'] 
                            for key, val in self.idd['properties'].items()}
                
        
        
        