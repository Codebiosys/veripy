.. _docid.steps.veripy.steps.forms.actions.upload_file_to_field:
.. index:: veripy.steps.forms.actions.upload_file_to_field

======================================================================
veripy.steps.forms.actions.upload_file_to_field
======================================================================

:Module:   veripy.steps.forms.actions.upload_file_to_field
:Filename: veripy/steps/forms/actions/upload_file_to_field.py

Step Overview
=============


================================================================================= ===== ==== ==== ====
Step Definition                                                                   Given When Then Step
================================================================================= ===== ==== ==== ====
When the file "{filename:file_input_type}" has been added to the "{element_name}"         x           
================================================================================= ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: When step; When the file "{filename:file_input_type}" has been added to the "{element_name}"

.. _when the file "{filename:file_input_type}" has been added to the "{element_name}":

**Step:** When the file "{filename:file_input_type}" has been added to the "{element_name}"
-------------------------------------------------------------------------------------------

Given that the desired file is located in the ``RESOURCES_DIR`` this
statement allows the user to add a file to a file input in a form.

::

    When the "My File.txt" has been added to the "File Upload Field"

