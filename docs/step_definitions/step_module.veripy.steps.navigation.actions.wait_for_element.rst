.. _docid.steps.veripy.steps.navigation.actions.wait_for_element:
.. index:: veripy.steps.navigation.actions.wait_for_element

======================================================================
veripy.steps.navigation.actions.wait_for_element
======================================================================

:Module:   veripy.steps.navigation.actions.wait_for_element
:Filename: veripy/steps/navigation/actions/wait_for_element.py

Step Overview
=============


=============================================================================== ===== ==== ==== ====
Step Definition                                                                 Given When Then Step
=============================================================================== ===== ==== ==== ====
Given the user waits {seconds:d} seconds for the "{element_name}" to be visible   x                 
When the user waits {seconds:d} seconds for the "{element_name}" to be visible          x           
=============================================================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Given step; Given the user waits {seconds:d} seconds for the "{element_name}" to be visible

.. _given the user waits {seconds:d} seconds for the "{element_name}" to be visible:

**Step:** Given the user waits {seconds:d} seconds for the "{element_name}" to be visible
-----------------------------------------------------------------------------------------

Wait for a given element on the page to become visible.
::

    When the user waits 10 seconds for the "Search Field" to be visible

.. index:: 
    single: When step; When the user waits {seconds:d} seconds for the "{element_name}" to be visible

.. _when the user waits {seconds:d} seconds for the "{element_name}" to be visible:

**Step:** When the user waits {seconds:d} seconds for the "{element_name}" to be visible
----------------------------------------------------------------------------------------

Wait for a given element on the page to become visible.
::

    When the user waits 10 seconds for the "Search Field" to be visible

