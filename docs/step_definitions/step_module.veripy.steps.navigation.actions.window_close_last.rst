.. _docid.steps.veripy.steps.navigation.actions.window_close_last:
.. index:: veripy.steps.navigation.actions.window_close_last

======================================================================
veripy.steps.navigation.actions.window_close_last
======================================================================

:Module:   veripy.steps.navigation.actions.window_close_last
:Filename: veripy/steps/navigation/actions/window_close_last.py

Step Overview
=============


================================================== ===== ==== ==== ====
Step Definition                                    Given When Then Step
================================================== ===== ==== ==== ====
When the user closes the last opened {screen_type}         x           
When the last opened {screen_type} is closed               x           
================================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: When step; When the user closes the last opened {screen_type}

.. _when the user closes the last opened {screen_type}:

**Step:** When the user closes the last opened {screen_type}
------------------------------------------------------------

Tells the browser to close was most recently openened
::

    When the last opened tab is closed

.. index:: 
    single: When step; When the last opened {screen_type} is closed

.. _when the last opened {screen_type} is closed:

**Step:** When the last opened {screen_type} is closed
------------------------------------------------------

Tells the browser to close was most recently openened
::

    When the last opened tab is closed

