.. _docid.steps.veripy.steps.aggregates.checks.check_assertion:
.. index:: veripy.steps.aggregates.checks.check_assertion

======================================================================
veripy.steps.aggregates.checks.check_assertion
======================================================================

:Module:   veripy.steps.aggregates.checks.check_assertion
:Filename: veripy/steps/aggregates/checks/check_assertion.py

Step Overview
=============


================================================== ===== ==== ==== ====
Step Definition                                    Given When Then Step
================================================== ===== ==== ==== ====
Then the statement that '{sentence}' responds with              x      
================================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Then step; Then the statement that '{sentence}' responds with

.. _then the statement that '{sentence}' responds with:

**Step:** Then the statement that '{sentence}' responds with
------------------------------------------------------------

Asserts that the given sentence raises an exception with the given message
::

    the statement that 'the "Home Link" is visible' responds with
    """The element "Home Link" was supposed to be visible and was not."""

