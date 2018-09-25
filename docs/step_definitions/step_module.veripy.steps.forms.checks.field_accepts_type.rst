.. _docid.steps.veripy.steps.forms.checks.field_accepts_type:
.. index:: veripy.steps.forms.checks.field_accepts_type

======================================================================
veripy.steps.forms.checks.field_accepts_type
======================================================================

:Module:   veripy.steps.forms.checks.field_accepts_type
:Filename: veripy/steps/forms/checks/field_accepts_type.py

Step Overview
=============


===================================================================================== ===== ==== ==== ====
Step Definition                                                                       Given When Then Step
===================================================================================== ===== ==== ==== ====
Then the "{field}" field does {not_:optional_not}accept {input_type:field_input_type}              x      
===================================================================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Then step; Then the "{field}" field does {not_:optional_not}accept {input_type:field_input_type}

.. _then the "{field}" field does {not_:optional_not}accept {input_type:field_input_type}:

**Step:** Then the "{field}" field does {not_:optional_not}accept {input_type:field_input_type}
-----------------------------------------------------------------------------------------------

Require that a field be configured to accept or not accept certain input types.
This sentence allows the user to specify their requirements in natural
language.

- Users can specify that a field accepts any typical HTML input type.
- Users can use the word "not".
- Input types can be plural. (``number`` & ``numbers`` have the same effect)

::

    # These have the same effect.
    The "Phone Number" field does accept text
    The "Phone Number" field does not accept numbers

