=======
History
=======

Releases
--------

Sun Oct 15 14:59:38 2023 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fixed issue #82

:Problem: Need read and write function for TOML format
:Solution: functions in experimental/toml.py

Sat Oct 14 19:04:56 2023 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fixed issue #96

:Problem: number of temp files remaining from #94
:Solution: removed temp tiles

Wed Oct 4 13:32:41 2023 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fixed issue #94

:Problem: need functions to do unit conversions to IP
:Solution: made a module experimental/epconversions.py for this



Wed Sep 20 21:45:16 2023 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fixed issue #92

:Problem: Need an easy way to open IDF file into epj
:solution: eppy3000.experimental.openidf.openidf(fname, wfile)

Wed Sep 20 16:25:41 2023 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fixed issue #90

:Problem: the code is throwing an error at the start of the tutorial
:Solution: fixed by added a weather file to the idf

Thu Jun 29 16:56:03 2023 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fixed issue #88

:Problem: readthedocs.org needs a .readthedocs.yaml
:Solution: added a .readthedocs.yaml file


Fri Apr 21 15:07:27 2023 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fixed issue #80

:Problem: Store E+ schema in DBM
:Solution: Done ! eppy3000viewer uses this code

Fri Apr 21 07:16:19 2023 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fixed issue #83

:Problem: pytest was throwing a `PytestRemovedIn8Warning` warning
:Solution: replaced setup function with fixtures


Release 0.1.13  (2021-03-16)
----------------------------

2021-03-16
~~~~~~~~~~

Fixed #76

:Problem: Need easier conversion from IDF to epJSON
:Solution: ``idffile2epjfile`` will convert a single file and ``idffolder2epjfolder`` will do batch conversion

Date: Mon Jan 18 21:53:40 PST 2021
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fixed issue #73

:Problem: Would be nice to have an html viewer for epj
:Solution: pytested eppy3000.epjviewer with sphinx user documentation

Date: Tue Jan 12 14:18:37 PST 2021
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fixed issue #69

:Problem: no EPJ.run() function
:Solution: EPJ.run() function implemented


Release 0.1.4  (2020-07-09)
---------------------------


Date:   Tue Jul 7 08:09:26 2020 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fixed issue #48

:Problem: No Tutorial for eppy3000
:Solution: tutorial for eppy3000

+ This tutorial is based on eppy tutorial
+ Identifies the gaps in the eppy3000 tagged by TODO in the tutorial
+ open issues on these TODOs and resolve


Release 0.1.3 (2020-07-04)
--------------------------

Date:   Wed May 13 14:20:34 2020 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    fixed issue # 45
    
    Problem: setup.py not including folders `oldeppy` and `experimental`
    Solution: setup.py updated and tested



Release 0.1.2 (2020-05-12)
--------------------------

Date:   Tue May 12 08:11:39 2020 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    fixed issue #41
    
    Problem: function to get an array of xyz points from the surfaces
    Solution: function in eppy300.experimental.listfields.surf2list()


Date:   Mon May 11 08:15:50 2020 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    fixed issue #34
    
    Problem: need an easy to use converter between
    epj (epyy300 format) and idf (eppy format)
    
    Solution: functions idf2epj() epj2idf() do this.
    epj.saveas(filename) and idf.saveas(filename)
    will save it to disk



Date:   Mon May 11 15:35:54 2020 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    fixed issue #39

    **Problem:** need a place to put experimental functions
    **Solution:** created an experimental folder in eppy3000


Date:   Mon May 11 08:15:50 2020 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    fixed issue #34
    
    Problem: need an easy to use converter between
    epj (epyy300 format) and idf (eppy format)
    
    Solution: functions idf2epj() epj2idf() do this.
    epj.saveas(filename) and idf.saveas(filename)
    will save it to disk



Sun May 10 09:26:32 2020 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    fixed issue #36

    Problem: modelbuilder.EPJ need savecopy() to fix issue #34
    Solution: coded EPJ.savecopy and EPJ.jsonstr()





Release 0.1.1 (2019-06-06)
--------------------------

2019-06-06
~~~~~~~~~~

- functions to read and write IDF files
    - issue #20

0.1.0 (2018-10-15)
------------------

* First release on PyPI.
