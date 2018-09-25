.. _docid.steps.veripy.steps.forms.actions.clear_input:
.. index:: veripy.steps.forms.actions.clear_input

======================================================================
veripy.steps.forms.actions.clear_input
======================================================================

:Module:   veripy.steps.forms.actions.clear_input
:Filename: veripy/steps/forms/actions/clear_input.py

Step Overview
=============


========================================= ===== ==== ==== ====
Step Definition                           Given When Then Step
========================================= ===== ==== ==== ====
When the user clears the "{element_name}"         x           
========================================= ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: When step; When the user clears the "{element_name}"

.. _when the user clears the "{element_name}":

**Step:** When the user clears the "{element_name}"
---------------------------------------------------

Tells the browser to clear the target input element

This method only works with traditional HTML input elements.
Your mileage-may-vary with browser plugins.

::

    When the user clears the "Prefilled Input"

