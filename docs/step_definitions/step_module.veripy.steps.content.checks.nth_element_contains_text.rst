.. _docid.steps.veripy.steps.content.checks.nth_element_contains_text:
.. index:: veripy.steps.content.checks.nth_element_contains_text

======================================================================
veripy.steps.content.checks.nth_element_contains_text
======================================================================

:Module:   veripy.steps.content.checks.nth_element_contains_text
:Filename: veripy/steps/content/checks/nth_element_contains_text.py

Step Overview
=============


=========================================================================================================== ===== ==== ==== ====
Step Definition                                                                                             Given When Then Step
=========================================================================================================== ===== ==== ==== ====
Then the {position:d}{ordinal:ordinal_indicator} {words} in the "{element_name}" contains the text "{text}"              x      
=========================================================================================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Then step; Then the {position:d}{ordinal:ordinal_indicator} {words} in the "{element_name}" contains the text "{text}"

.. _then the {position:d}{ordinal:ordinal_indicator} {words} in the "{element_name}" contains the text "{text}":

**Step:** Then the {position:d}{ordinal:ordinal_indicator} {words} in the "{element_name}" contains the text "{text}"
---------------------------------------------------------------------------------------------------------------------

Asserts that the nth element contains the given value as text
::

    the 3rd label of the "Form" contains the text "First Name"

