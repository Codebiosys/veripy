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

    @External @fixture.browser.chrome
    Scenario: check that google exists
        Given that the browser is at "google"
        When "hello world" is entered into the "search_field"
        And the user waits 2 seconds
        And the user clicks the "submit_button"
        Then the page title should be "hello world - Google Search"
        Then take a screen shot
