=======
History
=======

Releases
--------

Date:   Tue Jul 7 08:09:26 2020 -0700
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fixed issue #48

:Problem: No Tutorial for eppy3000
:Solution: tutorial for eppy3000

+ This tutorial is based on eppy turorial
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
