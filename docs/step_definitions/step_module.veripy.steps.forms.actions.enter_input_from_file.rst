.. _docid.steps.veripy.steps.forms.actions.enter_input_from_file:
.. index:: veripy.steps.forms.actions.enter_input_from_file

======================================================================
veripy.steps.forms.actions.enter_input_from_file
======================================================================

:Module:   veripy.steps.forms.actions.enter_input_from_file
:Filename: veripy/steps/forms/actions/enter_input_from_file.py

Step Overview
=============


================================================================================ ===== ==== ==== ====
Step Definition                                                                  Given When Then Step
================================================================================ ===== ==== ==== ====
When the content from "{filename:file_input_type}" is entered into the "{field}"         x           
================================================================================ ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: When step; When the content from "{filename:file_input_type}" is entered into the "{field}"

.. _when the content from "{filename:file_input_type}" is entered into the "{field}":

**Step:** When the content from "{filename:file_input_type}" is entered into the "{field}"
------------------------------------------------------------------------------------------

Copies the text from the given filename and enters it into the target element
::

    When the content from "My File.md" has been entered into the "Markdown Editor"

