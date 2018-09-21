.. _docid.steps.veripy.steps.navigation.checks.browser_at_page:
.. index:: veripy.steps.navigation.checks.browser_at_page

======================================================================
veripy.steps.navigation.checks.browser_at_page
======================================================================

:Module:   veripy.steps.navigation.checks.browser_at_page
:Filename: veripy/steps/navigation/checks/browser_at_page.py

Step Overview
=============


====================================== ===== ==== ==== ====
Step Definition                        Given When Then Step
====================================== ===== ==== ==== ====
Then the browser should be at "{name}"              x      
====================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Then step; Then the browser should be at "{name}"

.. _then the browser should be at "{name}":

**Step:** Then the browser should be at "{name}"
------------------------------------------------

Assert that the browser has navigated to the new given page, and switch
the page context to the new page.
::

    Then the browser should be at "Requisitions"

This step simply changes the context of the browser page to allow the user
to specify elements using the page's convenience selectors.

If the user has implicitly landed on a page (as a result of a button click,
or form submission) that has a dynamic URL, asserting the page URL will cause
a failure. In those cases, use the following variation.
::

    When the browser is now at "Requisitions"
    # or
    Given the browser is now at "Requisitions"

These variations do the same context switch without asserting the current URL
is the same as the page URL value.

