.. _docid.steps.veripy.steps.navigation.actions.browser_wait_switch_page:
.. index:: veripy.steps.navigation.actions.browser_wait_switch_page

======================================================================
veripy.steps.navigation.actions.browser_wait_switch_page
======================================================================

:Module:   veripy.steps.navigation.actions.browser_wait_switch_page
:Filename: veripy/steps/navigation/actions/browser_wait_switch_page.py

Step Overview
=============


===================================================================================== ===== ==== ==== ====
Step Definition                                                                       Given When Then Step
===================================================================================== ===== ==== ==== ====
When the browser is at "{page_name}" after {seconds:d} second{plural:optional_plural}         x           
===================================================================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: When step; When the browser is at "{page_name}" after {seconds:d} second{plural:optional_plural}

.. _when the browser is at "{page_name}" after {seconds:d} second{plural:optional_plural}:

**Step:** When the browser is at "{page_name}" after {seconds:d} second{plural:optional_plural}
-----------------------------------------------------------------------------------------------

Allow the user to specify that the browser has implicitly navigated
to a new page (usually by clicking a link or submitting a form).
::

    When the browser is at "Requisition Detail Page" after 2 seconds

This step simply changes the context of the browser page to allow the user
to specify elements using the page's convenience selectors.

If time doesn't matter, use the following:
::

    When the browser is now at "Requisitions Page"

This statement not only switches the context, but asserts that the current URL
is correct for the given page context.

