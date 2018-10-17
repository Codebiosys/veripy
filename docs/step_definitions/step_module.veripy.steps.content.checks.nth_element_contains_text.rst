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
Then the {position:d}{ordinal:ordinal_indicator} item in the "{element_name}" contains the text "{text}"                 x      
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

    Then the 3rd item in the "Form Labels" contains the text "First Name"

Note: in order to for this step to function properly, ``{"kwargs": "allow_mulitple": true}``
must be set for the element definition in the page fixture.

.. index:: 
    single: Then step; Then the {position:d}{ordinal:ordinal_indicator} item in the "{element_name}" contains the text "{text}"

.. _then the {position:d}{ordinal:ordinal_indicator} item in the "{element_name}" contains the text "{text}":

**Step:** Then the {position:d}{ordinal:ordinal_indicator} item in the "{element_name}" contains the text "{text}"
------------------------------------------------------------------------------------------------------------------

Asserts that the nth element contains the given value as text
::

    Then the 3rd item in the "Form Labels" contains the text "First Name"

Note: in order to for this step to function properly, ``{"kwargs": "allow_mulitple": true}``
must be set for the element definition in the page fixture.

