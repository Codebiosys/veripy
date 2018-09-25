.. _docid.steps.veripy.steps.navigation.actions.browser_at_page:
.. index:: veripy.steps.navigation.actions.browser_at_page

======================================================================
veripy.steps.navigation.actions.browser_at_page
======================================================================

:Module:   veripy.steps.navigation.actions.browser_at_page
:Filename: veripy/steps/navigation/actions/browser_at_page.py

Step Overview
=============


===================================== ===== ==== ==== ====
Step Definition                       Given When Then Step
===================================== ===== ==== ==== ====
Given that the browser is at "{name}"   x                 
===================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Given step; Given that the browser is at "{name}"

.. _given that the browser is at "{name}":

**Step:** Given that the browser is at "{name}"
-----------------------------------------------

Tells the browser to load a specific page designated by an identifer.
::

    Given that the browser is at "google.com"

In order to interact with a page, you must first perform this check. This
statement sets the page context so that later steps can refer to the page
by it's predefined identifiers.

