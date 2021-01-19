# Copyright (c) 2018-2019 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""subclass Munch"""

from munch import Munch
from eppy3000.epschema import EPSchemaMunch


class NotEPObject(Exception):
    pass


def printkey(key, indent=0, formatstr=None, func=None):
    """Prints the key in epMunch with the right indentation

    Used internally by printmunch"""
    if not func:
        func = print
    if not indent:
        func("")
        func("")
        indent = 0
    elif indent == 1:
        func("")
    if not formatstr:
        formatstr = "{}{}"
        func(formatstr.format(" " * 4 * indent, key))
    else:
        func(formatstr.format(" " * 4 * indent, key))


def printmunch(amunch, indent=0, index=None, func=None):
    """This prints the epMunch object

    In effect, it can print the epJSON file
    which may have nested epMunch objects in it. Or it can
    print a single epMunch object.
    printmunch is called recursively until all epMunch
    objects are exhausted. It will also  print a list of
    epMunch objects that can occur within an epJSON file

    It has been tested for epJSON files. The is no guarantee
    that will work on a more complex nesting of epMunch objects

    An epJSON object such as::


         "Heating Setpoint Schedule": {
             "data": [
                 {
                     "field": "Through: 12/31"
                 },
                 {
                     "field": "For: AllDays"
                 },
                 {
                     "field": "Until: 24:00"
                 },
                 {
                     "field": 15.0
                 }
             ],
             "idf_max_extensible_fields": 4,
             "idf_max_fields": 6,
             "idf_order": 59,
             "schedule_type_limits_name": "Any Number"
         },

    will print out as::


        Schedule:Compact                                 !-  EP_KEY
                    Heating Setpoint Schedule            !-  EPJOBJECT_NAME
                                                         !-  data
                        Through: 12/31                       !-  field #1
                        For: AllDays                         !-  field #2
                        Until: 24:00                         !-  field #3
                        15.0                                 !-  field #4
                    4                                    !-  idf_max_extensible_fields
                    6                                    !-  idf_max_fields
                    59                                   !-  idf_order
                    Any Number                           !-  schedule_type_limits_name

    which is much more easy on human eyes

    Parameters
    ----------
    amunch: epMunch
        an EpMunch object that may have more nested EpMunch objects within
    indent: int
        Used internally to indent the output
    index: int
        used internally to give index numbers to repeating items in a list
    func: function
        default func = print
        you can get a list by::

            lines = []
            printmunch(amunch, func=line.append)
            # lines will be a list of lines

    Returns
    -------
    None
    """  # noqa: E501
    if isinstance(amunch, EPSchemaMunch):  # don't print EPSchema stuff
        return
    if not func:
        func = print
    if isinstance(amunch, Munch):
        if "eppykey" in amunch:
            func("")
            func(
                f"{amunch['eppykey']:<36}{' '*4*(indent+1)} !-  EP_KEY         # use .eppykey"
            )
            ind1 = " " * 4 * (indent + 1)
            ind2 = " " * 4 * (indent - 1)
            func(
                f"{ind1}{amunch['eppyname']:<32} {ind2}!-  EPJOBJECT_NAME # use .eppyname"
            )
    for key, val in amunch.items():
        if key in ["eppy_epj", "eppy_epobjects"]:
            continue  # prevents an infinite recurse
        if isinstance(val, Munch):
            printmunch(val, indent=indent + 1, index=index, func=func)
        elif isinstance(val, list):
            printkey(key, indent=3, formatstr="{0}" + " " * 36 + " !-  {1}", func=func)
            for i, aval in enumerate(val):
                printmunch(aval, indent=indent + 1, index=i + 1, func=func)
        elif key not in [
            "eppykey",
            "eppyname",
            "eppy_obj_schema",
            "eppy_epj",
            "eppy_epobjects",
        ]:
            if index:
                ind = " " * 4 * (indent + 1)
                func(f"{ind}{val:<36} !-  {key} #{index}")
            else:
                ind = " " * 4 * (indent + 1)
                func(f"{ind}{val:<36} !-  {key}")


class EPMunch(Munch):
    """Subclass of Munch for eppy3000"""

    def __init__(self, *args, **kwargs):
        super(EPMunch, self).__init__(*args, **kwargs)

    # TODO : __repr__ and __str__ ahould be different
    def __repr__(self):
        """print this as a snippet"""
        lines = []
        printmunch(self, func=lines.append)
        return "\n".join(lines)

    def __str__(self):
        """same as __repr__"""
        return self.__repr__()

    def __setitem__(self, key, value):
        """only for epobjects and for key starting with eppy"""
        # EPMunchobj['keyname'] = value will
        #   call __setitem__
        # EPMunchobj.keyname = value will
        #   call __setattr__ and then call
        #   call __setitem__
        if "eppykey" not in self:
            # it is not an epobject. None of this applies
            super(EPMunch, self).__setitem__(key, value)
        else:
            # it is an epobject
            if key in self:
                if key.startswith("eppy"):  # TODO: test if it is a string
                    if key == "eppyname":
                        if key in self.keys():
                            # if 'eppyname' is changed, the following actions happen in the parent dict
                            # the old key (value of 'eppyname') is popped and a new key is added
                            # with the same value
                            # epobjects_dict = self.eppy_epj[self.eppykey]
                            epobjects_dict = self.eppy_epobjects
                            epobject = epobjects_dict.pop(self.eppyname)
                            epobjects_dict[value] = self
                            self.pop(key)
                            super(EPMunch, self).__setitem__(key, value)
                        else:
                            super(EPMunch, self).__setitem__(key, value)
                    else:
                        pass  # user is not allowed to change eppy fields
                else:
                    super(EPMunch, self).__setitem__(key, value)
            else:
                super(EPMunch, self).__setitem__(key, value)

    def __setattr__(self, name, value):
        """deals with names starting with eppy. Name starts with eppy only in epobjects"""
        # EPMunchobj['keyname'] = value will
        #   call __setitem__
        # EPMunchobj.keyname = value will
        #   call __setattr__ and then call
        #   call __setitem__
        if "eppykey" not in self:
            # it is not an epobject
            super(EPMunch, self).__setattr__(name, value)  # Let Munch handle it
        else:
            # it is an epobject
            if name.startswith("eppy"):
                if name in self:
                    pass  # if the key exists, user cannot change it
                else:
                    super(EPMunch, self).__setattr__(name, value)  # Let Munch handle it
            else:
                super(EPMunch, self).__setattr__(name, value)  # Let Munch handle it
            if name == "eppyname":
                if name in self.keys():
                    # if 'eppyname' is changed, the following actions happen in the parent dict
                    # the old key (value of 'eppyname') is popped and a new key is added
                    # with the same value
                    epobjects_dict = self.eppy_epobjects
                    epobject = epobjects_dict.pop(self.eppyname)
                    epobjects_dict[value] = self
                    self.pop(name)
                    super(EPMunch, self).__setattr__(name, value)  # Let Munch handle it
                else:
                    super(EPMunch, self).__setattr__(name, value)  # Let Munch handle it

    def delete(self):
        """delete this by removing it from the parent dict"""
        try:
            epobjects = self.eppy_epobjects
        except AttributeError as e:
            raise NotEPObject
        return epobjects.pop(self.eppyname)

    def copy(self, newname):
        """make a copy of this anc add it to parent dict"""
        pass

    def allfieldnames(self):
        return list(self.keys())

    def epjfieldnames(self):
        fieldnames = [key for key in self.keys() if not key.startswith("eppy")]
        return fieldnames

    def schemafieldnames(self):
        return list(self.eppy_objepschema.keys())
