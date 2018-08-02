# Test Configuration
# This suite is run during CI tests. We should make sure to include all available
# statements here to know that they work.

Feature: showing off behave
    As a developer
    I want to ensure that all of the available test statements work

    Scenario: run a simple test
        Given we have behave installed
        When we implement a test
        Then behave will test it for us!


    Scenario: check that google exists
        Given that the browser is at "google"
        When "hello world" is entered into the search_field
        And the user clicks the submit_button
        And the user waits 5 seconds for the search_results_logo to be visible
        Then the page title should be "hello world - Google Search"
        Then take a screenshot


    Scenario: Test if the demo app has the title "Hello World"
        Given that the browser is at "localhost-hello"
        Then the page title should be "Hello World"
        Then the h1 does contain the text "Hello World"
        Then take a screenshot


    Scenario: Test if the demo app fields accept the right data.
        Given that the browser is at "localhost-hello"
        Then the optional_field field is not required
        Then the required_field field is required

        Then the enabled_field field is enabled
        Then the disabled_field field is not enabled

        Then the text_field field does accept text
        Then the text_field field does not accept numbers
        Then the number_field field does accept numbers
        Then the number_field field does not accept passwords

        Then take a screenshot
