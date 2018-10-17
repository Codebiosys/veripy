.. _docid.steps.veripy.steps.aggregates.actions.auth:
.. index:: veripy.steps.aggregates.actions.auth

======================================================================
veripy.steps.aggregates.actions.auth
======================================================================

:Module:   veripy.steps.aggregates.actions.auth
:Filename: veripy/steps/aggregates/actions/auth.py

Step Overview
=============


=============================================================================================== ===== ==== ==== ====
Step Definition                                                                                 Given When Then Step
=============================================================================================== ===== ==== ==== ====
Given the user logged in via "{page_name}" with username "{username}" and password "{password}"   x                 
Given the username "{username}" and password "{password}", log in via "{page_name}"               x                 
=============================================================================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Given step; Given the user logged in via "{page_name}" with username "{username}" and password "{password}"

.. _given the user logged in via "{page_name}" with username "{username}" and password "{password}":

**Step:** Given the user logged in via "{page_name}" with username "{username}" and password "{password}"
---------------------------------------------------------------------------------------------------------

Tells the browser to to navigate to the given page to authenticate
::

    Given the username "user" and password "password", log in via "Login Page"

This is a convenience step for the purposes of logging into a basic
web application. This step assumes that for the most part, a login
page consists of a `User Name Field`, a `Password Field`, and
a `Login Button`.
These can be specified in the page fixture for the login page.

Note that this step doesn't actually check if the user correctly
authenticated. It only enters the specified credentials at the
specified page.

:param page_name: The name of the page fixture to use for the login page
             This page should specify the following keys:
             - `User Name Field`: Selector for the user name field
             - `Password Field`: Selector for the password field
             - `Log In Button`: Selector for the log in button
:param username: The username value
:param password: The password value

.. index:: 
    single: Given step; Given the username "{username}" and password "{password}", log in via "{page_name}"

.. _given the username "{username}" and password "{password}", log in via "{page_name}":

**Step:** Given the username "{username}" and password "{password}", log in via "{page_name}"
---------------------------------------------------------------------------------------------

Tells the browser to to navigate to the given page to authenticate
::

    Given the username "user" and password "password", log in via "Login Page"

This is a convenience step for the purposes of logging into a basic
web application. This step assumes that for the most part, a login
page consists of a `User Name Field`, a `Password Field`, and
a `Login Button`.
These can be specified in the page fixture for the login page.

Note that this step doesn't actually check if the user correctly
authenticated. It only enters the specified credentials at the
specified page.

:param page_name: The name of the page fixture to use for the login page
             This page should specify the following keys:
             - `User Name Field`: Selector for the user name field
             - `Password Field`: Selector for the password field
             - `Log In Button`: Selector for the log in button
:param username: The username value
:param password: The password value

