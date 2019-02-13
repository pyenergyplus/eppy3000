========
eppy3000
========


.. image:: https://img.shields.io/pypi/v/eppy3000.svg
        :target: https://pypi.python.org/pypi/eppy3000

.. image:: https://img.shields.io/travis/pyenergyplus/eppy3000.svg
        :target: https://travis-ci.org/pyenergyplus/eppy3000

.. image:: https://readthedocs.org/projects/eppy3000/badge/?version=latest
        :target: https://eppy3000.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




E+ scripting using epJSON file format


* Free software: Mozilla Public License, v. 2.0
* Documentation: https://eppy3000.readthedocs.io.
* Home Page: https://github.com/pyenergyplus/eppy3000


Features - so far :-)
---------------------

* Open and read an epJSON file with *some* `eppy <https://github.com/santoshphilip/eppy>`_ functionality.
* Right now the `eppy <https://github.com/santoshphilip/eppy>`_ functionality is only partial


Background
----------

E+ has been moving from the IDD/IDF text format to a JSON format. `Eppy <https://github.com/santoshphilip/eppy>`_ reads the old IDD/IDF format. There is a need to have `eppy <https://github.com/santoshphilip/eppy>`_ read the JSON format and/or have a new package that will read the JSON format.

Whats in a name
---------------

Why is this package called eppy3000 ?

It is a play on the word python3000. Guido van van Rossum said about python in 2007 *"The first time I came up with the idea of Python 3000 was probably at a Python conference in the year 2000. The name was a take on Windows 2000. ...<snip>...  The idea was that Python 3000 would be the first Python release to give up backwards compatibility in favor of making it the best language going forward."*

Eppy3000 will also break backward compatibility with eppy. Also eppy3000 will be written only for python3. Eppy3000 and eppy will continue to remain the best scripting language for modelling :-)


So what is eppy3000
-------------------

This project is an attempt to read JSON file formats and work like eppy. There is some value in trying to do this from scratch. The dot syntax that makes the original eppy useful can be recreated with a couple of lines in eppy3000. It took a lot of deep hacking to make the dot syntax work in the original eppy. Eppy3000 reads the JSON format as a dictionary. The package `Munch <https://github.com/Infinidat/munch>`_ (what was `Bunch <https://github.com/dsc/bunch>`_) allows the use of dot format syntax with a dictionary. The code is as simple as::

    as_json = json.load(open(fname, 'r'))
    for_dot_syntax = DefaultMunch.fromDict(as_json)

At this point eppy3000 is an exploration to find out what is possible. The API in eppy3000 will not be stable as we explore the possibilities. So, don't use it as production code yet :-)


What about eppy
---------------

Eppy will be continue to be developed and maintained. A major task will be to make eppy read the new JSON formats. Initial investigations shows that it is not too hard to develop this functionality. Internally eppy will continue to use the old format. Hopefully this will make the JSON reading functionality trivially easy. At the moment, E+ maintains a one to one mapping between the old IDD/IDF format and the new JSON format. This mapping is embedded in the file Energy+.schema.epJSON, pointing to an easy compatibility strategy.

In the long term, this may not be a viable strategy, as E+ may totally abandon the IDD/IDF file format breaking the link between JSON and IDD/IDF. Discussion thread at `unmethours <https://unmethours.com/question/36062/hvac-templates-to-be-discontinued/>`_ seems to indicate that this is about 5 yers in the future.


Future possibilites
-------------------

A number of possibilites came up in discussions at Simbuild 2018 in Chicago. The biggest takeaway was that the code base for the JSON format and the dot syntax can lead to a universal translator between modelling file formats. The thinking here is that if there exists a schema.JSON for two modelling file structures, the possibility of translating between the two exists.

Of course *the proof is in the pudding*. So we are going to write some quick and dirty translators between E+ and DOE2.1E (or EQuest) as well as between the older idds and the new epJSON. Lets see how that goes.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
