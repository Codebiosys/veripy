
import logging

from behave import given

from veripy import custom_types  # noqa


logger = logging.getLogger('auth')


@given('the user logged in via "{name}" with username "{username}" and password "{password}"')
def user_logged_in(context, name, username, password):
    """ Tells the browser to to navigate to the given page to authenticate
    ::

        Given the user logged in via "Login Page" with username "user" and password "password"


    This is a convenience step for the purposes of logging into a basic
    web application. This step assumes that for the most part, a login
    page consists of a `User Name Field`, a `Password Field`, and
    a `Login Button`.
    These can be specified in the page fixture for the login page.

    Note that this step doesn't actually check if the user correctly
    authenticated. It only enters the specified credentials at the
    specified page.

    :param name: The name of the page fixture to use for the login page
                 This page should specify the following keys:
                 - `User Name Field`: Selector for the user name field
                 - `Password Field`: Selector for the password field
                 - `Log In Button`: Selector for the log in button
    :param username: The username value
    :param password: The password value
    """
    username_field = 'User Name Field'
    password_field = 'Password Field'
    login_button = 'Log In Button'

    context.execute_steps(f"""
        Given that the browser is at "{name}"
        When "{username}" is entered into the "{username_field}"
        And "{password}" is entered into the "{password_field}"
        And the user clicks the "{login_button}"
    """)
