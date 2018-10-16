.. _docid.steps.veripy.steps.forms.checks.field_disabled:
.. index:: veripy.steps.forms.checks.field_disabled

======================================================================
veripy.steps.forms.checks.field_disabled
======================================================================

:Module:   veripy.steps.forms.checks.field_disabled
:Filename: veripy/steps/forms/checks/field_disabled.py

Step Overview
=============


================================================================================== ===== ==== ==== ====
Step Definition                                                                    Given When Then Step
================================================================================== ===== ==== ==== ====
Then the "{element_name}" field is {not_:optional_not}{state:field_enabled_option}              x      
================================================================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Then step; Then the "{element_name}" field is {not_:optional_not}{state:field_enabled_option}

.. _then the "{element_name}" field is {not_:optional_not}{state:field_enabled_option}:

**Step:** Then the "{element_name}" field is {not_:optional_not}{state:field_enabled_option}
--------------------------------------------------------------------------------------------

Require that a field is enabled or disabled in a form.
This sentence allows the user to specify their requirements in natural
language.

- Users can specify that a field is either "enabled" or "disabled"
- Users can use the word "not".

::

    # These have the same effect.
    The "Phone Number" field is not enabled
    The "Phone Number" field is disabled

