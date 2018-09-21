.. _docid.steps.veripy.steps.navigation.actions.browser_size:
.. index:: veripy.steps.navigation.actions.browser_size

======================================================================
veripy.steps.navigation.actions.browser_size
======================================================================

:Module:   veripy.steps.navigation.actions.browser_size
:Filename: veripy/steps/navigation/actions/browser_size.py

Step Overview
=============


========================================================== ===== ==== ==== ====
Step Definition                                            Given When Then Step
========================================================== ===== ==== ==== ====
Given the browser window is {width:d} by {height:d} pixels   x                 
========================================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Given step; Given the browser window is {width:d} by {height:d} pixels

.. _given the browser window is {width:d} by {height:d} pixels:

**Step:** Given the browser window is {width:d} by {height:d} pixels
--------------------------------------------------------------------

Tells the browser to resize the viewport.
::

    Given the browser window is 500 by 1000 pixels

Resizing the browser viewport will be important for testing the web applciation
in various device screen sizes such as desktop, phone, tablet, etc.

