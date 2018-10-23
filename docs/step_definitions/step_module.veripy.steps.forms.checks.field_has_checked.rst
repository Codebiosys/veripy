.. _docid.steps.veripy.steps.forms.checks.field_has_checked:
.. index:: veripy.steps.forms.checks.field_has_checked

======================================================================
veripy.steps.forms.checks.field_has_checked
======================================================================

:Module:   veripy.steps.forms.checks.field_has_checked
:Filename: veripy/steps/forms/checks/field_has_checked.py

Step Overview
=============


================================================================ ===== ==== ==== ====
Step Definition                                                  Given When Then Step
================================================================ ===== ==== ==== ====
Then the "{element_name}" checkbox is {not_:optional_not}checked              x      
================================================================ ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Then step; Then the "{element_name}" checkbox is {not_:optional_not}checked

.. _then the "{element_name}" checkbox is {not_:optional_not}checked:

**Step:** Then the "{element_name}" checkbox is {not_:optional_not}checked
--------------------------------------------------------------------------

Asserts that a form checkbox is or is not checked.
::

    The "User Accepts Terms" checkbox is checked"
    The "User Accepts Terms" checkbox is not checked"

