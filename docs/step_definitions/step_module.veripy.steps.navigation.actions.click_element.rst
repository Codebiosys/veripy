.. _docid.steps.veripy.steps.navigation.actions.click_element:
.. index:: veripy.steps.navigation.actions.click_element

======================================================================
veripy.steps.navigation.actions.click_element
======================================================================

:Module:   veripy.steps.navigation.actions.click_element
:Filename: veripy/steps/navigation/actions/click_element.py

Step Overview
=============


========================================== ===== ==== ==== ====
Step Definition                            Given When Then Step
========================================== ===== ==== ==== ====
Given the user clicks the "{element_name}"   x                 
Given the "{element_name}" is clicked        x                 
When the user clicks the "{element_name}"          x           
When the "{element_name}" is clicked               x           
========================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Given step; Given the user clicks the "{element_name}"

.. _given the user clicks the "{element_name}":

**Step:** Given the user clicks the "{element_name}"
----------------------------------------------------

Tells the browser to click on an element with the given identifier.

::

    Given the "Search Button" is clicked
    # Or
    When the "Search Button" is clicked

.. index:: 
    single: Given step; Given the "{element_name}" is clicked

.. _given the "{element_name}" is clicked:

**Step:** Given the "{element_name}" is clicked
-----------------------------------------------

Tells the browser to click on an element with the given identifier.

::

    Given the "Search Button" is clicked
    # Or
    When the "Search Button" is clicked

.. index:: 
    single: When step; When the user clicks the "{element_name}"

.. _when the user clicks the "{element_name}":

**Step:** When the user clicks the "{element_name}"
---------------------------------------------------

Tells the browser to click on an element with the given identifier.

::

    Given the "Search Button" is clicked
    # Or
    When the "Search Button" is clicked

.. index:: 
    single: When step; When the "{element_name}" is clicked

.. _when the "{element_name}" is clicked:

**Step:** When the "{element_name}" is clicked
----------------------------------------------

Tells the browser to click on an element with the given identifier.

::

    Given the "Search Button" is clicked
    # Or
    When the "Search Button" is clicked

