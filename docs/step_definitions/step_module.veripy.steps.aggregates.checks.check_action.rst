.. _docid.steps.veripy.steps.aggregates.checks.check_action:
.. index:: veripy.steps.aggregates.checks.check_action

======================================================================
veripy.steps.aggregates.checks.check_action
======================================================================

:Module:   veripy.steps.aggregates.checks.check_action
:Filename: veripy/steps/aggregates/checks/check_action.py

Step Overview
=============


============================================== ===== ==== ==== ====
Step Definition                                Given When Then Step
============================================== ===== ==== ==== ====
Then if '{sentence}', the system responds with              x      
============================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Then step; Then if '{sentence}', the system responds with

.. _then if '{sentence}', the system responds with:

**Step:** Then if '{sentence}', the system responds with
--------------------------------------------------------

Asserts that the given sentence raises an exception with the given message
::

    if 'the user clears the "Missing Field"', the system responds with
    """The element "Home Link" was supposed to be visible and was not."""

