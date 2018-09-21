.. _docid.steps.veripy.steps.forms.actions.select_option:
.. index:: veripy.steps.forms.actions.select_option

======================================================================
veripy.steps.forms.actions.select_option
======================================================================

:Module:   veripy.steps.forms.actions.select_option
:Filename: veripy/steps/forms/actions/select_option.py

Step Overview
=============


======================================= ===== ==== ==== ====
Step Definition                         Given When Then Step
======================================= ===== ==== ==== ====
When "{value}" is selected for "{name}"         x           
======================================= ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: When step; When "{value}" is selected for "{name}"

.. _when "{value}" is selected for "{name}":

**Step:** When "{value}" is selected for "{name}"
-------------------------------------------------

Tells the browser to select the HTML `<option>` with the specified value.

::

    When "MOBILE" is selected for "Contact Options"

