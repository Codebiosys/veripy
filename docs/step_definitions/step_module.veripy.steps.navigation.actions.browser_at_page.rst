.. _docid.steps.veripy.steps.navigation.actions.browser_at_page:
.. index:: veripy.steps.navigation.actions.browser_at_page

======================================================================
veripy.steps.navigation.actions.browser_at_page
======================================================================

:Module:   veripy.steps.navigation.actions.browser_at_page
:Filename: veripy/steps/navigation/actions/browser_at_page.py

Step Overview
=============


========================================== ===== ==== ==== ====
Step Definition                            Given When Then Step
========================================== ===== ==== ==== ====
Given that the browser is at "{page_name}"   x                 
Given the browser is at "{page_name}"        x                 
========================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Given step; Given that the browser is at "{page_name}"

.. _given that the browser is at "{page_name}":

**Step:** Given that the browser is at "{page_name}"
----------------------------------------------------

Tells the browser to load a specific page designated by an identifer.
::

    Given the browser is at "Google Home Page"

In order to interact with a page, you must first perform this check. This
statement sets the page context so that later steps can refer to the page
by it's predefined identifiers.

.. index:: 
    single: Given step; Given the browser is at "{page_name}"

.. _given the browser is at "{page_name}":

**Step:** Given the browser is at "{page_name}"
-----------------------------------------------

Tells the browser to load a specific page designated by an identifer.
::

    Given the browser is at "Google Home Page"

In order to interact with a page, you must first perform this check. This
statement sets the page context so that later steps can refer to the page
by it's predefined identifiers.

