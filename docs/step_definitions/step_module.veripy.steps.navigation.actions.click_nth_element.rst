.. _docid.steps.veripy.steps.navigation.actions.click_nth_element:
.. index:: veripy.steps.navigation.actions.click_nth_element

======================================================================
veripy.steps.navigation.actions.click_nth_element
======================================================================

:Module:   veripy.steps.navigation.actions.click_nth_element
:Filename: veripy/steps/navigation/actions/click_nth_element.py

Step Overview
=============


======================================================================================================== ===== ==== ==== ====
Step Definition                                                                                          Given When Then Step
======================================================================================================== ===== ==== ==== ====
Given the user clicks on the {position:d}{ordinal:ordinal_indicator} option in the "{element_list_name}"   x                 
When the user clicks on the {position:d}{ordinal:ordinal_indicator} option in the "{element_list_name}"          x           
======================================================================================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Given step; Given the user clicks on the {position:d}{ordinal:ordinal_indicator} option in the "{element_list_name}"

.. _given the user clicks on the {position:d}{ordinal:ordinal_indicator} option in the "{element_list_name}":

**Step:** Given the user clicks on the {position:d}{ordinal:ordinal_indicator} option in the "{element_list_name}"
------------------------------------------------------------------------------------------------------------------

Tells the browser to click on the nth option in the list of elements of the given identifier.
::

    When the user clicks on the 2nd option in the "Table"

Note that in order for this step to work properly, you *must* specify
`allow_multiple` to `true` in the page fixture.

.. index:: 
    single: When step; When the user clicks on the {position:d}{ordinal:ordinal_indicator} option in the "{element_list_name}"

.. _when the user clicks on the {position:d}{ordinal:ordinal_indicator} option in the "{element_list_name}":

**Step:** When the user clicks on the {position:d}{ordinal:ordinal_indicator} option in the "{element_list_name}"
-----------------------------------------------------------------------------------------------------------------

Tells the browser to click on the nth option in the list of elements of the given identifier.
::

    When the user clicks on the 2nd option in the "Table"

Note that in order for this step to work properly, you *must* specify
`allow_multiple` to `true` in the page fixture.

