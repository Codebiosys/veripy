Feature: showing off behave

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
