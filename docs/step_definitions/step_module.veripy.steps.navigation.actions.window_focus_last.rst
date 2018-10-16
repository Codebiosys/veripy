.. _docid.steps.veripy.steps.navigation.actions.window_focus_last:
.. index:: veripy.steps.navigation.actions.window_focus_last

======================================================================
veripy.steps.navigation.actions.window_focus_last
======================================================================

:Module:   veripy.steps.navigation.actions.window_focus_last
:Filename: veripy/steps/navigation/actions/window_focus_last.py

Step Overview
=============


======================================================= ===== ==== ==== ====
Step Definition                                         Given When Then Step
======================================================= ===== ==== ==== ====
When the user switches to the last opened {screen_type}         x           
When the last opened {screen_type} is focused                   x           
======================================================= ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: When step; When the user switches to the last opened {screen_type}

.. _when the user switches to the last opened {screen_type}:

**Step:** When the user switches to the last opened {screen_type}
-----------------------------------------------------------------

Tells the browser to switch to the tab that was most recently openened
::

    When the last opened tab is focused

.. index:: 
    single: When step; When the last opened {screen_type} is focused

.. _when the last opened {screen_type} is focused:

**Step:** When the last opened {screen_type} is focused
-------------------------------------------------------

Tells the browser to switch to the tab that was most recently openened
::

    When the last opened tab is focused

