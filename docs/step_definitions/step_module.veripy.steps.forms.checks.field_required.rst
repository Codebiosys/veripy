.. _docid.steps.veripy.steps.forms.checks.field_required:
.. index:: veripy.steps.forms.checks.field_required

======================================================================
veripy.steps.forms.checks.field_required
======================================================================

:Module:   veripy.steps.forms.checks.field_required
:Filename: veripy/steps/forms/checks/field_required.py

Step Overview
=============


============================================================================ ===== ==== ==== ====
Step Definition                                                              Given When Then Step
============================================================================ ===== ==== ==== ====
Then the "{field}" field is {not_:optional_not}{state:field_required_option}              x      
============================================================================ ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Then step; Then the "{field}" field is {not_:optional_not}{state:field_required_option}

.. _then the "{field}" field is {not_:optional_not}{state:field_required_option}:

**Step:** Then the "{field}" field is {not_:optional_not}{state:field_required_option}
--------------------------------------------------------------------------------------

Require that a field is required or optional in a form.
This sentence allows the user to specify their requirements in natural
language.

- Users can specify that a field is either "required" or "optional"
- Users can use the word "not".

::

    # These have the same effect.
    The "Phone Number" field is not required
    The "Phone Number" field is optional

