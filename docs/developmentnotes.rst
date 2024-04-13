=================
Development Notes
=================

This a a fairly free form document exploring the directions in which early development could go. It is also a repository for ideas that may or may not be used.  

This section may not be needed once the code gets more stable. Right now this a way to document these ideas so that they don't get lost as we make pragmatic decisions.

Munch classes for epJSON
------------------------


From a `presentation <http://web.eecs.utk.edu/~jnew1/presentations/2017_IBPSA_JSON.pdf>`_. at the buildsim conference in 2017 

.. image:: ./images/developmentnotes/epJSON_structure.png

**The rest of this section may be superseded by the actual code written. See the next section for updates.**

This opens up the possibilty of having three classes:

- EPMunch -> general
    - Root
    - E+ Object type
- EPObject -> for items got from EPJ.epobjects()
    - E+ Name
    - Fields
- EPListinObject -> for lists in EPObject

The class heirarchy would be::

    Munch -> EPMunch -> EPObject
             EPMunch -> EPListinObject

Right now we have only ``EPMunch`` for all of the above.

The initial benifit in having the three classes is that is eases the ``__repr__`` (and ``__str__``) code. Right now there are too many if statements. The same for ``__setattr__`` and ``__setitem__``. It is not a critical change, since everything works right now.

The development has veered away from code structure shown above. Now it looks more like this. The intent is to stick close the ``eppy`` API, but modify as needed. The present code structure looks this


Code Structure
==============

This describes the structure in the actual code:

EPJ
---

``EPJ``  is the main class. An ``epj`` file is opened by

::

    epjname = "somthin.epj"
    epj = EPJ(epjname=epjname)

``EPJ(epjname=epjname)`` calls ``EPJ.read()`` that does the following. 

::

    self.epj = readepjjson(self.epjname) 
    self.epobjects = EpjMapping(self.epj)
    # where self is EPJ
    
``self.epj`` is a Munch. This is where the file data is stored. Basically any modifications to the file should be done at ``self.epj``

The internal E+ data for a file ins in ``json`` format. Python libraries reads the ``json`` text file as a dict. We read it here as ``Munch`` which is derived from a dict. 

Holding the entire file structure as a dict is problematic in terms of accessing and manipulating it. For one, it is hard to use the ``eppy`` API with it (although this is not obvious at first glance, but trust me - it is hard). The ``eppy`` is well tested and easy to use. There is no reason to invent a new API.

::

    self.epj = readepjjson(self.epjname) -> reads the data in as a Munch
    self.epobjects = EpjMapping(self.epj) -> acts like a dict
                        # but actually reflects the changes in self.epj
    # epobject = epobjects -> This acts like a list
                        # is a EpjSequence descendant of abc.MutableSequence
                        # makes any updates into self.epj
