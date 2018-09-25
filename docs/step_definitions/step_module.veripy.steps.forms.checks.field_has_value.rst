.. _docid.steps.veripy.steps.forms.checks.field_has_value:
.. index:: veripy.steps.forms.checks.field_has_value

======================================================================
veripy.steps.forms.checks.field_has_value
======================================================================

:Module:   veripy.steps.forms.checks.field_has_value
:Filename: veripy/steps/forms/checks/field_has_value.py

Step Overview
=============


=========================================== ===== ==== ==== ====
Step Definition                             Given When Then Step
=========================================== ===== ==== ==== ====
Then the "{element}" has the value "{text}"              x      
=========================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Then step; Then the "{element}" has the value "{text}"

.. _then the "{element}" has the value "{text}":

**Step:** Then the "{element}" has the value "{text}"
-----------------------------------------------------

Asserts that a form element has the given value.
This is useful in identifying the value of a given field.

- Users can assert that a field has a value.

::

    The "Phone Number Field" has the value "123-123-1231"

