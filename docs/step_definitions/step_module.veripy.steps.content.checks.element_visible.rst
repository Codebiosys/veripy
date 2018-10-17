.. _docid.steps.veripy.steps.content.checks.element_visible:
.. index:: veripy.steps.content.checks.element_visible

======================================================================
veripy.steps.content.checks.element_visible
======================================================================

:Module:   veripy.steps.content.checks.element_visible
:Filename: veripy/steps/content/checks/element_visible.py

Step Overview
=============


======================================================= ===== ==== ==== ====
Step Definition                                         Given When Then Step
======================================================= ===== ==== ==== ====
Then the "{element_name}" is {not_:optional_not}visible              x      
======================================================= ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Then step; Then the "{element_name}" is {not_:optional_not}visible

.. _then the "{element_name}" is {not_:optional_not}visible:

**Step:** Then the "{element_name}" is {not_:optional_not}visible
-----------------------------------------------------------------

Asserts that the element is the visible on the page.

::

    Then the "Modal Window" is not visible

