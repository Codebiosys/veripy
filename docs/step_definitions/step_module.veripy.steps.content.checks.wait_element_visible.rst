.. _docid.steps.veripy.steps.content.checks.wait_element_visible:
.. index:: veripy.steps.content.checks.wait_element_visible

======================================================================
veripy.steps.content.checks.wait_element_visible
======================================================================

:Module:   veripy.steps.content.checks.wait_element_visible
:Filename: veripy/steps/content/checks/wait_element_visible.py

Step Overview
=============


===================================================================================== ===== ==== ==== ====
Step Definition                                                                       Given When Then Step
===================================================================================== ===== ==== ==== ====
Then the "{element_name}" is visible after {seconds:d} second{plural:optional_plural}              x      
===================================================================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Then step; Then the "{element_name}" is visible after {seconds:d} second{plural:optional_plural}

.. _then the "{element_name}" is visible after {seconds:d} second{plural:optional_plural}:

**Step:** Then the "{element_name}" is visible after {seconds:d} second{plural:optional_plural}
-----------------------------------------------------------------------------------------------

Wait for a given element on the page to become visible.

::

    Then the "Page Title" is visible after 3 seconds

