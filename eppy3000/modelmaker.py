# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""same as modelmaker in eppy"""

from io import StringIO
from munch import Munch
from eppy3000.readepj import readepjjson
from eppy3000.epschema import read_epschema_asmunch
from eppy3000.readepj import removeeppykeys
from eppy3000.epschema import EPSchema
from eppy3000.epMunch import EPMunch
from eppy3000.epj_mmapping import EpjMapping
import eppy3000.runner.run_functions as run_functions


class EPJ(object):
    def __init__(self, epjname=None, epw=None, epschemaname=None):
        super(EPJ, self).__init__()
        self.epjname = epjname
        self.epw = epw
        self.epschemaname = epschemaname
        if self.epschemaname:
            self.readepschema()
        self.read()

    def read_epschema_asmunch(self):
        """Read the epschema file - will become a frozen singleton"""
        read_epschema_asmunch(self.epschemaname)
        # not used ???

    def read(self):
        """read the epj file"""
        self.epj = readepjjson(self.epjname)
        self.epobjects = EpjMapping(self.epj)
        # {
        #     key: [val1 for val1 in val.values()] for key, val in self.epj.items()
        # }
        # TODO: the above line should get the epobjects from the schema
        # This should happen whenever the schema is read.
        # in case the schema reading happens far in the future
        # eppy3000 should partilly work even without the schema
        # -

        # insert epj into the epobject
        # this allows the epobject to access all other objects in the epj
        for epobjects in self.epobjects.values():
            for epobject in epobjects:
                epobject["eppy_epj"] = self.epj
        if self.epschemaname:
            for key in self.epobjects.keys():
                for epobject in self.epobjects[key]:
                    epobject["eppy_objepschema"] = self.epschema.epschemaobjects[key]

    def readepschema(self):
        """read the epschema file"""
        self.epschema = EPSchema(self.epschemaname)

    def __repr__(self):
        """print this"""
        return self.epj.__repr__()

    def saveas(self, filename, indent=4):
        """saveas in filename"""
        self.epjname = filename
        self.save(filename, indent=indent)

    def savecopy(self, filename=None, indent=4):
        """save a copy of the file
        if filename==None: return copy in StringIO
        NOT unit TESTED at all. Not even use tested"""
        if filename:
            self.save(filename=filename, indent=indent)
        else:
            tosave = self.epj.toDict()
            tosave = Munch.fromDict(tosave)
            removeeppykeys(tosave)
            fhandle = StringIO()
            fhandle.write(tosave.toJSON(indent=indent))
            fhandle.seek(0)
            return fhandle

    def save(self, filename=None, indent=4):
        """save the file"""
        if not filename:
            filename = self.epjname
        try:
            with open(filename, "w") as fhandle:
                tosave = self.epj.toDict()
                tosave = Munch.fromDict(tosave)
                removeeppykeys(tosave)
                fhandle.write(tosave.toJSON(indent=indent))
        except TypeError as e:
            fhandle = filename
            tosave = self.epj.toDict()
            tosave = Munch.fromDict(tosave)
            removeeppykeys(tosave)
            fhandle.write(tosave.toJSON(indent=indent))

    def jsonstr(self, indent=4):
        """return a json string of the file"""
        fhandle = self.savecopy(indent=indent)
        return "\n".join([line.rstrip() for line in fhandle])

    def newepobject(self, key, objname, defaultvalues=True, **kwargs):
        """create a new epj object"""
        # TODO test for dup name
        # TODO Kwargs strategy for array -
        #     delay implementation for now, throw exception
        # TODO exceptions for wrong field name
        # TODO exception for wrong field value type
        # TODO documentation in usage.rst
        # should self.epobjects be updated here
        objepschema = self.epschema.epschemaobjects[key]
        try:
            nobj = self.epj[key][objname] = EPMunch()
        except KeyError as e:
            self.epj[key] = EPMunch()
            nobj = self.epj[key][objname] = EPMunch()
        for fieldname in objepschema.fieldnames():
            try:
                if defaultvalues:
                    fieldfprop = objepschema.fieldproperty(fieldname)
                    nobj[fieldname] = fieldfprop["default"]
            except KeyError as e:
                prop = objepschema.fieldproperty(fieldname)
                # print(fieldname, prop.keys())
                if "type" in prop:
                    if prop["type"] == "array":
                        # pprint(prop['items'])
                        pass
                pass
        for key1, val1 in kwargs.items():
            nobj[key1] = val1
        nobj["eppykey"] = key
        nobj["eppyname"] = objname
        nobj["eppy_objepschema"] = objepschema
        return nobj

    # def removeepobject(self, key, objname):
    #     """remove an epj object"""
    #     # should self.epobjects be updated here
    #     return self.epj[key].pop(objname)

    def popepobject(self, key, index):
        """Pop an EPJ object from the EPJ.

        Parameters
        ----------
        key : str
            The type of EPJ object.
        index : int
            The index of the object to pop.

        Returns
        -------
        EpBunch object.

        """
        return self.epobjects[key].pop(index)

    def removeepobject(self, epobject):
        """Remove an EPJ object from the EPJ.

        Parameters
        ----------
        epobject : EpBunch object
            The epobject to remove.

        """
        key = epobject.eppykey
        self.epobjects[key].remove(epobject)

    def removeallepobjects(self, epjkey):
        """Remove all epobjects of a certain type from the EPJ.

        Parameters
        ----------
        epjkey : key of the epobjects to remove

        """
        while len(self.epobjects[epjkey]) > 0:
            self.popepobject(epjkey, 0)


    def copyepobject(self, key, objname, newname):
        """copy an epj object with a new name"""
        # don't use the function dict.items() since the json for array has
        # field name `items`
        # should self.epobjects be updated here
        oldobj = self.epj[key][objname]
        newobj = EPMunch()
        self.epj[key][newname] = newobj
        for key1 in oldobj.keys():
            if not key1.startswith("eppy"):
                val1 = oldobj[key1]
                if isinstance(val1, list):
                    newobj[key1] = list()
                    for item in val1:
                        newobj[key1].append(item.copy())
                else:
                    newobj[key1] = val1
        newobj["eppyname"] = newname
        newobj["eppykey"] = key
        newobj["eppy_objepschema"] = oldobj["eppy_objepschema"]
        return newobj

    def run(self, **runoptions):
        return run_functions.run(self, **runoptions)
