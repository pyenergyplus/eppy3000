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

``eppy`` works in this way::

    #### epyy - idf ####
    from eppy import modeleditor
    from eppy.modeleditor import IDF

    iddfile = "/Applications/EnergyPlus-9-6-0/Energy+.idd"
    fname1 = "../eppy3000/eppy3000/resources/epJSON/V9_6/ShopWithPVandBattery.idf"

    IDF.setiddname(iddfile)
    idf = IDF(fname1)
    zones = idf.idfobjects["zone"]
    zone = zones[0]

The key API oin ``eppy`` is using ``idfobjects`` and getting a list zones, where each zone is a dict (or Bunch/Munch in this case). When using ``eppy`` we make changes to zones by:

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

We need to use a similar strategy in eppy300

::

    print(f"{type(idf)=}")
    >> type(idf)=<class 'eppy.modeleditor.IDF'>
    
    print(f"{type(zone)=}")
    ype(zone)=<class 'eppy.bunch_subclass.EpBunch'>




``eppy3000`` has a similar API::

    #### eppy3000 - epj ####
    epj = EPJ(epjname)
    zones = epj.epobjects['Zone']
    zone = zones[0]
    print(zone.eppyname
    >> First Zone
    print(zone.eppykey)
    >> Zone

Let us look at the ``type`` of the variables and understand how it works::

    print(f"{type(epj)=}")
    >> type(epj)=<class 'eppy3000.modelmaker.EPJ'>

OK. that makes sense. Let us look at ``zones`` and ``zone``::

    print(f"{type(zones)=}")
    >> type(zones)=<class 'eppy3000.epj_mmapping.EpjSequence'>

What is ``eppy3000.epj_mmapping.EpjSequence`` and why doe we need it
