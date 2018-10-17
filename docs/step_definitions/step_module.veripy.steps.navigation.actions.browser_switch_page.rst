.. _docid.steps.veripy.steps.navigation.actions.browser_switch_page:
.. index:: veripy.steps.navigation.actions.browser_switch_page

======================================================================
veripy.steps.navigation.actions.browser_switch_page
======================================================================

:Module:   veripy.steps.navigation.actions.browser_switch_page
:Filename: veripy/steps/navigation/actions/browser_switch_page.py

Step Overview
=============


========================================= ===== ==== ==== ====
Step Definition                           Given When Then Step
========================================= ===== ==== ==== ====
Given the browser is now at "{page_name}"   x                 
When the browser is now at "{page_name}"          x           
========================================= ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Given step; Given the browser is now at "{page_name}"

.. _given the browser is now at "{page_name}":

**Step:** Given the browser is now at "{page_name}"
---------------------------------------------------

Allow the user to specify that the browser has implicitly navigated
to a new page (usually by clicking a link or submitting a form).
::

    When the browser is now at "Requisition Detail Page"
    # or
    Given the browser is now at "Requisition Detail Page"

This step simply changes the context of the browser page to allow the user
to specify elements using the page's convenience selectors.

In some cases it is not possible to assert that the page URL is some value
because the value is determined at runtime (dynamic URLs, etc). In most cases
users should prefer the assertion statement:
::

    Then the browser is now at "Requisitions Page"

This statement not only switches the context, but asserts that the current URL
is correct for the given page context.

.. index:: 
    single: When step; When the browser is now at "{page_name}"

.. _when the browser is now at "{page_name}":

**Step:** When the browser is now at "{page_name}"
--------------------------------------------------

Allow the user to specify that the browser has implicitly navigated
to a new page (usually by clicking a link or submitting a form).
::

    When the browser is now at "Requisition Detail Page"
    # or
    Given the browser is now at "Requisition Detail Page"

This step simply changes the context of the browser page to allow the user
to specify elements using the page's convenience selectors.

In some cases it is not possible to assert that the page URL is some value
because the value is determined at runtime (dynamic URLs, etc). In most cases
users should prefer the assertion statement:
::

    Then the browser is now at "Requisitions Page"

This statement not only switches the context, but asserts that the current URL
is correct for the given page context.

