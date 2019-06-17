# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""same as modelmaker in eppy"""

from munch import Munch
from eppy3000.readidf import readidfjson
from eppy3000.epschema import read_epschema_asmunch
from eppy3000.readidf import removeeppykeys
from eppy3000.epschema import EPSchema
from eppy3000.epMunch import EPMunch


class IDF(object):
    def __init__(self, idfname=None, epw=None, epschemaname=None):
        super(IDF, self).__init__()
        self.idfname = idfname
        self.epw = epw
        self.epschemaname = epschemaname
        if self.epschemaname:
            self.readepschema()
        self.read()

    def read_epschema_asmunch(self):
        """Read the epschema file - will become a frozen singleton"""
        read_epschema_asmunch(self.epschemaname)

    def read(self):
        """read the idf file"""
        self.idf = readidfjson(self.idfname)
        self.idfobjects = {key: [val1 for val1 in val.values()]
                           for key, val in self.idf.items()}
        if self.epschemaname:
            for key in self.idfobjects.keys():
                for idfobject in self.idfobjects[key]:
                    idfobject['eppy_objepschema'] = self.epschema.epschemaobjects[key]

    def readepschema(self):
        """read the epschema file"""
        self.epschema = EPSchema(self.epschemaname)

    def __repr__(self):
        """print this"""
        return self.idf.__repr__()

    def saveas(self, filename, indent=4):
        """saveas in filename"""
        self.idfname = filename
        self.save(filename, indent=indent)

    def save(self, filename=None, indent=0):
        """save the file"""
        if not filename:
            filename = self.idfname
        with open(filename, 'w') as fhandle:
            tosave = self.idf.toDict()
            tosave = Munch.fromDict(tosave)
            removeeppykeys(tosave)
            fhandle.write(tosave.toJSON(indent=indent))

    def newidfobject(self, key, objname, defaultvalues=True, **kwargs):
        """create a new idf object"""
        # TODO test for dup name
        # TODO Kwargs strategy for array -
        #     delay implementation for now, throw exception
        # TODO exceptions for wrong field name
        # TODO exception for wrong field value type
        # TODO documentation in usage.rst
        objepschema = self.epschema.epschemaobjects[key]
        try:
            nobj = self.idf[key][objname] = EPMunch()
        except KeyError as e:
            self.idf[key] = EPMunch()
            nobj = self.idf[key][objname] = EPMunch()
        for fieldname in objepschema.fieldnames():
            try:
                if defaultvalues:
                    fieldfprop = objepschema.fieldproperty(fieldname)
                    nobj[fieldname] = fieldfprop['default']
            except KeyError as e:
                prop = objepschema.fieldproperty(fieldname)
                # print(fieldname, prop.keys())
                if 'type' in prop:
                    if prop['type'] == 'array':
                        # pprint(prop['items'])
                        pass
                pass
        for key1, val1 in kwargs.items():
            nobj[key1] = val1
        nobj['eppykey'] = key
        nobj['eppyname'] = objname
        nobj['eppy_objepschema'] = objepschema
        return nobj

    def removeidfobject(self, key, objname):
        """remove an idf object"""
        return self.idf[key].pop(objname)

    def copyidfobject(self, key, objname, newname):
        """copy an idf object with a new name"""
        # don't use the function dict.items() since the json for array has
        # field name `items`
        oldobj = self.idf[key][objname]
        newobj = EPMunch()
        self.idf[key][newname] = newobj
        for key1 in oldobj.keys():
            if not key1.startswith('eppy'):
                val1 = oldobj[key1]
                if isinstance(val1, list):
                    newobj[key1] = list()
                    for item in val1:
                        newobj[key1].append(item.copy())
                else:
                    newobj[key1] = val1
        newobj['eppyname'] = newname
        newobj['eppykey'] = key
        newobj['eppy_objepschema'] = oldobj['eppy_objepschema']
        return newobj
