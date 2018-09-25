.. _docid.steps.veripy.steps.forms.actions.enter_text_into_current:
.. index:: veripy.steps.forms.actions.enter_text_into_current

======================================================================
veripy.steps.forms.actions.enter_text_into_current
======================================================================

:Module:   veripy.steps.forms.actions.enter_text_into_current
:Filename: veripy/steps/forms/actions/enter_text_into_current.py

Step Overview
=============


=============================================== ===== ==== ==== ====
Step Definition                                 Given When Then Step
=============================================== ===== ==== ==== ====
When "{text}" is entered into the current field         x           
=============================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: When step; When "{text}" is entered into the current field

.. _when "{text}" is entered into the current field:

**Step:** When "{text}" is entered into the current field
---------------------------------------------------------

Tells the browser to enter the given test into the element with
the current focus.
::

    When "query text" is entered into the current field

