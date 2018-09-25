.. _docid.steps.veripy.steps.forms.checks.field_has_empty_value:
.. index:: veripy.steps.forms.checks.field_has_empty_value

======================================================================
veripy.steps.forms.checks.field_has_empty_value
======================================================================

:Module:   veripy.steps.forms.checks.field_has_empty_value
:Filename: veripy/steps/forms/checks/field_has_empty_value.py

Step Overview
=============


======================================= ===== ==== ==== ====
Step Definition                         Given When Then Step
======================================= ===== ==== ==== ====
Then the "{element}" has an empty value              x      
======================================= ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Then step; Then the "{element}" has an empty value

.. _then the "{element}" has an empty value:

**Step:** Then the "{element}" has an empty value
-------------------------------------------------

Asserts that a form element has an empty value.
This is useful in identifying fields that do not have default values.

- Users can specify that a field has an empty value.

::

    The "Phone Number" has an empty value

