Feature: Content Sentences
    Content sentences allow a tester to verify information that is displayed
    in the application

    @example_app @content @checks @element_contains_text
    Scenario: The Demo App header contains the text "Hello World"
        Given that the browser is at "localhost-hello"
        Then the "Page Header" contains the text "Hello World"
        Then take a screen shot

    @example_app @content @checks @element_contains_text @exceptions
    Scenario: The Demo App header does not contain the text "Goodbye World"
        Given that the browser is at "localhost-hello"
        Then it is not the case that the "Page Header" contains the text "Goodbye World"
        Then the statement that 'the "Page Header" contains the text "Goodbye World"' responds with
             """
             The "Page Header" was supposed to contain "Goodbye World", but instead had "Hello World".
             """
        Then the statement that 'the "Missing Link" contains the text "Goodbye World"' responds with
             """
             The "Missing Link" was not found on the page.
             """
        Then take a screen shot

    @example_app @content @checks @element_contains_text @xfail
    Scenario: XFail: The Demo App header does not contain the text "Goodbye World"
        Given that the browser is at "localhost-hello"
        Then the "Page Header" contains the text "Goodbye World"
        Then take a screen shot

    @example_app @content @checks @element_contains_text @xfail
    Scenario: XFail: The Demo App header does not contain the Missing Link
        Given that the browser is at "localhost-hello"
        Then the "Missing Link" contains the text "Goodbye World"
        Then take a screen shot


    @example_app @content @checks @element_visible
    Scenario: The Demo App header is visible and the Hidden Content is not
        Given that the browser is at "localhost-hello"
        Then the "Page Header" is visible
        Then the "Hidden Content" is not visible
        Then the "Missing Link" is not visible
        Then take a screen shot


    @example_app @content @checks @element_visible @exceptions
    Scenario: The visibility check has the correct messages
        Given that the browser is at "localhost-hello"
        Then it is not the case that the "Page Header" is not visible
        Then it is not the case that the "Hidden Content" is visible
        Then the statement that 'the "Page Header" is not visible' responds with
             """
             The "Page Header" was not supposed to be visible but it was.
             """
        Then the statement that 'the "Hidden Content" is visible' responds with
             """
             The "Hidden Content" was supposed to be visible but it was not.
             """
        Then the statement that 'the "Missing Link" is visible' responds with
             """
             The "Missing Link" was supposed to be visible but it was not present.
             """
        Then take a screen shot

    @example_app @content @checks @element_visible @xfail
    Scenario: XFail: The visibility check responds for visible objects
        Given that the browser is at "localhost-hello"
        Then the "Page Header" is not visible
        Then take a screen shot

    @example_app @content @checks @element_visible @xfail
    Scenario: XFail: The visibility check responds for invisible objects
        Given that the browser is at "localhost-hello"
        Then the "Hidden Content" is visible
        Then take a screen shot

    @example_app @content @checks @element_visible @xfail
    Scenario: XFail: The visibility check responds for missing objects
        Given that the browser is at "localhost-hello"
        Then the "Missing Link" is visible
        Then take a screen shot

    @example_app @content @checks @nth_element_contains_text
    Scenario: The Nth item sentence finds the correct item and asserts its text
        Given that the browser is at "localhost-hello"
        Then the 2nd label in the "form" contains the text "Optional input"
        Then take a screen shot

    @example_app @content @checks @nth_element_contains_text @exceptions
    Scenario: The Nth item sentence has the correct messages
        Given that the browser is at "localhost-hello"
        Then it is not the case that the 1nd label in the "form" contains the text "Optional input"
        Then it is not the case that the 2nd label in the "form" contains the text "Required input"
        Then the statement that 'the 2nd label in the "form" contains the text "Required input"' responds with
             """
             The 2nd label in the "form" should have contained the text "Required input", but it did not.
             """
        Then the statement that 'the 99th label in the "form" contains the text "Required input"' responds with
            """
            The "form" does not have a 99th label.
            """
        Then the statement that 'the 1st word in the "Missing Link" contains the text "Not"' responds with
            """
            The "Missing Link" was not found on the page.
            """
        Then take a screen shot

    @example_app @content @checks @nth_element_contains_text @xfail
    Scenario: Xfail: The Nth item sentence responds with missing input
        Given that the browser is at "localhost-hello"
        Then the 2nd label in the "form" contains the text "Required input"
        Then take a screen shot

    @example_app @content @checks @nth_element_contains_text @xfail
    Scenario: Xfail: The Nth item sentence responds with not enough inputs
        Given that the browser is at "localhost-hello"
        Then the 99th label in the "form" contains the text "Required input"
        Then take a screen shot

    @example_app @content @checks @nth_element_contains_text @xfail
    Scenario: Xfail: The Nth item sentence responds with not found
        Given that the browser is at "localhost-hello"
        Then the 1st word in the "Missing Link" contains the text "Not"
        Then take a screen shot

    @example_app @content @checks @page_title
    Scenario: The Demo App Page Title is "Hello World"
        Given that the browser is at "localhost-hello"
        Then the page title should be "Hello World"
        Then take a screen shot


    @example_app @content @checks @page_title @exceptions
    Scenario: The Demo App Page Title is not "Goodbye World"
        Given that the browser is at "localhost-hello"
        Then it is not the case that the page title should be "Goodbye World"
        Then the statement that 'the page title should be "Goodbye World"' responds with
          """
          The page title was supposed to be "Goodbye World" but was "Hello World".
          """
        Then take a screen shot

    @example_app @content @checks @page_title @xfail
    Scenario: XFail: The Demo App Page Title is not "Goodbye World"
        Given that the browser is at "localhost-hello"
        Then the page title should be "Goodbye World"
        Then take a screen shot
