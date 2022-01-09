=====================================
Evaluation of JSON as a format for E+
=====================================

Positives
=========

- all the positives for choosing JSON in the first place (refer paper)
- Allows user tags to be included, that will be ignored by E+
    - Use case: Floor numbers can be put in for ASHRAE 90.1 baseline modeling
- Allows user objects that will be ignored by E+
    - Use Case: There can be user defined HVAC_Templates, that can be preprocessed 

Negatives
=========

- JSON not as human readable as advertised
- This may reduce direct text editing of a JSON file
- JSON's use of "{}" causes visual clutter and feels verbose
- if the keywords are case sensitive (need to confirm this), user has an addtional concern
- the nesting of blocks is hard to identify visually
    - in a long list of MATERIAL or CONSTRUCTION objects
    - you have to scroll up to the outer block to see what type of object you are looking at.
- No comments possible in JSON
    - Although comments can be added by comment tag ignored by E+
    - hard to do diagrams as in IDF format
    - hard to have free form comments
- Groups are not documented in present schema 9.6. ** Correction: it is there **
    - group names in schema do always match those in html documentation (bigladder.com)
    - some object names are missing in html documentation (bigladder.com)




Interesting
===========

- E+ schema does not use spaces in keyword, even though JSON allows it. Is this going to be enforced in future versions ?

Design Pathways
===============

Continue to use IDF or YAML or other format for human readabllity. Have builtin translators that convert to JSON that E+ can use internally. Bothe IDF and YAML allow for comments.

IDF format may be limited as it depends on the legacy idd documentation within the JSON schema. This is likely to be phased out. In principle this should not be a constraint. If a comment line next to the field value identifies the field tag/key, one can write a translator to JSON.  Proof of concept of this can be prototyped

YAML is a more obvious format since converter to JSON are easily avaliable. This can be prototyped too.