=======================
Development Notes - EPJ
=======================

This a a fairly free form document exploring the directions in which early development could go. It is also a repository for ideas that may or may not be used.  

This section may not be needed once the code gets more stable. Right now this a way to document these ideas so that they don't get lost as we make pragmatic decisions.

Code Structure
==============

This describes the structure in the actual code:

EPJ
---

``EPJ``  is the main class. An ``epj`` file is opened by

::

    epjname = "something.epj"
    epj = EPJ(epjname=epjname)

``EPJ(epjname=epjname)`` calls ``EPJ.read()`` that does the following. 

::

    self.epj = readepjjson(self.epjname) 
    self.epobjects = EpjMapping(self.epj)
    # where self is EPJ
    
``self.epj`` is a Munch. This is where the file data is stored. Basically any modifications to the file should be done at ``self.epj``

The internal E+ data for a file ins in ``json`` format. Python libraries reads the ``json`` text file as a dict. We read it here as ``Munch`` which is derived from a dict. 

Holding the entire file structure as a dict is problematic in terms of accessing and manipulating it. For one, it is hard to use the ``eppy`` API with it (although this is not obvious at first glance, but trust me - it is hard). The ``eppy`` is well tested and easy to use. There is no reason to invent a new API.

``eppy`` works in this way::

    #### epyy - idf ####
    from eppy import modeleditor
    from eppy.modeleditor import IDF

    iddfile = "/Applications/EnergyPlus-9-6-0/Energy+.idd"
    fname1 = "./eppy3000/resources/epJSON/V9_6/ShopWithPVandBattery.idf"

    IDF.setiddname(iddfile)
    idf = IDF(fname1)
    zones = idf.idfobjects["zone"]
    zone = zones[0]

The key API in ``eppy`` is using ``idfobjects`` and getting a list zones, where each zone is a dict (or Bunch/Munch in this case). When using ``eppy`` we make changes to zones by:

    - modifying items in the list ``zones``.
    - adding new items to it
    - deleting items from it.

The funny thing is the actual data for the model does not sit in the list ``zones``. It is sitting in ``idf.model``. Any changes you make to the list ``zones`` is making changes to the model. What kind of magic does this?

Let us look at the ``type`` for ``zones``. It acts like a list. Is it really a list ?

::

    print(f"{type(zones)=}")
    >> type(zones)=<class 'eppy.idf_msequence.Idf_MSequence'>

``Idf_MSequence`` is a class. What is it inherited from?

::

    import inspect
    inspect.getmro(eppy.idf_msequence.Idf_MSequence)

     >> (eppy.idf_msequence.Idf_MSequence,
     collections.abc.MutableSequence,

     ... more items ...

     object)

We are using ``MutableSequence`` as a way of making changes in ``model``. The module documentation for ``idf_msequence`` says the following::

    idf_msequence.py
    """
    Subclass from collections.MutableSequence to get finer control over a list like
    object.

    This is to work with issue 40 in github:

    idf1.idfobjects['BUILDING'] is a list and is not connected to
    idf1.model.dt['BUILDING']

    List has to be subclassed to solve this problem.

    # Alex Martelli describes how to use collections.MutableSequence in
    # <http://stackoverflow.com/questions/3487434/overriding-append-method-after-inheriting-from-a-python-list>

    """
    
    <snip>

    class Idf_MSequence(collections.abc.MutableSequence):
        """Used to keep IDF.idfobjects in sync with IDF.model.dt."""

    <snip>

Now let us look at EPJ and see how we can build up something similar::



    from eppy3000.modelmaker import EPJ
    fname = "./eppy3000/resources/epJSON/V9_6/ShopWithPVandBattery.epJSON"
    epj = EPJ(fname)

    zones = epj.epobjects["Zone"]
    zone = zones[0]

Let us look at the type for ``epj.epobjects``, ``zones`` and ``zone``

::

    print(f"{type(epj.epobjects)}")
    >> <class 'eppy3000.epj_mmapping.EpjMapping'>

    print(f"{type(zones)}")
    >> <class 'eppy3000.epj_mmapping.EpjSequence'>

    print(f"{type(zone)}")
    >> <class 'eppy3000.epMunch.EPMunch'>

The data for the ``*.epj`` file is held in ``epj.model``. Any changes made through EpjMapping, EpjSequence and EPMunch will result in a change in ``epj.model``

All of these variables can see ``epj.model``. Let us confirm this with an assertion statement.

::


    assert epj.model == epj.epobjects.themodel
    assert epj.model == zones.themodel
    assert epj.model == zone.eppy_model

EPJ.alldbms
-----------

The Energy+.schema.epJSON is stored in a dbm on the disk. ``EPJ.alldbms`` is the cache for the schema dbm. It holds the schema for all versions of the schema used in this instance pf eppy3000. 


To see how it works goto look at :doc:`/EPSchema`

Problem with Energy+.schema.epJSON (or IDD)
-------------------------------------------

Getting the terminology right (The narrative here is based on ``EnergyPlus-23-2-0``):

Let us start with ``eppy`` and the terminology used there. This is familiar terrain.

1. The files we build our models in and are called IDF files. They have an extension .idf
    - an example would be ``5ZoneAirCooled.idf``
2. The structure of the IDF files is defined in the IDD file. 
    - The specific file in question is ``Energy+.idd``. You can open it and take a look. It is very well written.

We need have an IDF file and the IDD file for ``eppy`` to work.

Now with Energyplus moving towards ``JSON`` format, we have a different set of files that map to the IDD and the IDF formats. Let us take a look at them:

1. Let us call the IDF file an EPJ file when it is in the JSON format. Makes it easy to talk about it. One could say "Let us look at the EPJ file" or "There is a typo in the EPJ file". The file extension is .epJSON. Which stands for *EnergyPlus JSON*.
    - an example would be ``5ZoneAirCooled.idf``
    - The ``ExampleFiles`` folder has this file ``RefBldgMediumOfficeNew2004_Chicago_epJSON.epJSON``, in case you want to look at a real file
2. The structure of the EPJ file is in the ``Energy+.schema.epJSON`` file. The file extension is .epJSON, since it is a JSON file. Let us call it "EPJ Schema" (written as EPJSchema) file.  It will describe the structure of objects in the EPJ files.

For eppy300 to work we need EPJ and EPJSchema file. 
    
In Summary:


+-------------+----------------------+-------------------------+
|             | eppy                 |   eppy3000              |
+=============+======================+=========================+
|model file   | IDF                  |   EPJ                   |
+-------------+----------------------+-------------------------+
|Example file | 5ZoneAirCooled.idf   |   5ZoneAirCooled.epJSON |
+-------------+----------------------+-------------------------+

+--------------------+---------------+-------------------------+
|        	     |  eppy	     |  eppy3000               |
+====================+===============+=========================+
|data structure	     |  IDD	     |  EPJSchema              |
+--------------------+---------------+-------------------------+
|data structure file |	Energy+.idd  |	Energy+.schema.epJSON  |
+--------------------+---------------+-------------------------+

``Energy+.schema.epJSON`` is a very large file (9.9 MB in EnergyPlus-22-1-0). This file contains the datastructure of the 

Archived - Munch classes for epJSON
-----------------------------------


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


