@fixture.browser.chrome
Feature: Aggregate Sentences
    Aggregate sentences allow the Tester to run multiple sentences in one action
    or modify an existing sentence in new ways

    @example_app @aggregates @action @auth
    Scenario: Test that the user can send login credentials at the specified page
        Given that the browser is at "login"
        Then take a screen shot

        Given the user logged in via "login" with username "username" and password "password"
        Then the page title should be "Logged In"
        Then take a screen shot


    @example_app @aggregates @check @invert_check
    Scenario: Test that the Test Writer can check the inverse of a sentence
        Given that the browser is at "login"
        Then the page title should be "Log In"
        Then it is not the case that the page title should be "Logged In"

    @example_app @aggregates @checks @xfail
    Scenario: The Demo App raises the correct errors for tabular sentences
        Given that the browser is at "localhost-hello"
        Then the statement that 'the the following items are visible' responds with
          """
          Tabular instructions are not supported by compound sentences.
          """
          | item           |
          | Hidden Content |
          | Missing Link   |

    @example_app @aggregates @actions @wait_for
    Scenario: The tester can wait for an element
        Given that the browser is at "localhost-hello"
        Then after a few seconds, the "Required Field" is visible
            """
            This checks for visibility; it just waits 1 second before
            checking if the element is visible
            """
        Then after 1 second, it is not the case that the "Missing Field" is visible
        Then the statement that 'after 2 seconds, the "Missing Field" is visible' responds with
          """
          The "Missing Field" was supposed to be visible but it was not present.
          """
        Then take a screen shot
