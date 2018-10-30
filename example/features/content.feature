@fixture.browser.chrome @fixture.setup.SETUP_EXAMPLE
Feature: Content Sentences
    Content sentences allow a tester to verify information that is displayed
    in the application

    @example_app @content @checks @element_contains_text
    Scenario: The Demo App header contains the text "Hello World"
        Given that the browser is at "localhost-hello"
        Then the "Page Header" contains the text "Hello World"


    @example_app @content @checks @element_contains_text @tabular
    Scenario: The Demo App contains correct values
        Given that the browser is at "localhost-hello"
        Then the following items are displayed
        | element         | items            |
        | Page Header     | Hello World      |
        | Other Page Link | Go to Other Page |
        | Other Tab Link  | Go to Other Tab  |

    @example_app @content @checks @element_contains_text @tabular @xfail
    Scenario: The Demo App contains correct values
        Given that the browser is at "localhost-hello"
        Then the following items are displayed
        | element         | items                  |
        | Page Header     | Goodbye World          |
        | Other Page Link | Go to A Different Page |
        | Other Tab Link  | Go to A Different Tab  |

    @example_app @content @checks @element_contains_text @tabular
    Scenario Outline: The Demo App contains repeatable values
        Given that the browser is at "localhost-hello"
        Then the following items are displayed
        | element         | items             |
        | <elementname>   | <elementvalue>    |

      Examples: Element <elementname> = <elementvalue>
          | elementname     | elementvalue     |
          | Page Header     | Hello World      |
          | Other Page Link | Go to Other Page |
          | Other Tab Link  | Go to Other Tab  |

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

    @example_app @content @checks @element_contains_text @xfail
    Scenario: XFail: The Demo App header does not contain the text "Goodbye World"
        Given that the browser is at "localhost-hello"
        Then the "Page Header" contains the text "Goodbye World"

    @example_app @content @checks @element_contains_text @xfail
    Scenario: XFail: The Demo App header does not contain the Missing Link
        Given that the browser is at "localhost-hello"
        Then the "Missing Link" contains the text "Goodbye World"


    @example_app @content @checks @element_visible
    Scenario: The Demo App header is visible and the Hidden Content is not
        Given that the browser is at "localhost-hello"
        Then the "Page Header" is visible
        Then the "Hidden Content" is not visible
        Then the "Missing Link" is not visible


    @example_app @content @checks @element_visible @element_visible_table
    Scenario: The Demo App can check multiple items for visibility
        Given that the browser is at "localhost-hello"
        Then the following items are visible
          | items          |
          | Page Header    |
          | Required Field |
          | Optional Field |
          | Enabled Field  |
          | Disabled Field |
        Then the following items are not visible
          | items          |
          | Hidden Content |
          | Missing Link   |

    @example_app @aggregates @checks @element_visible_table @xfail
    Scenario: The Demo App raises the correct errors
        Given that the browser is at "localhost-hello"
        Then the following items are visible
          """
          Tabular instructions are not supported by compound sentences.
          This should respond that all sentences are not visible
          """
          | items          |
          | Hidden Content |
          | Missing Link   |


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

    @example_app @content @checks @element_visible @xfail
    Scenario: XFail: The visibility check responds for visible objects
        Given that the browser is at "localhost-hello"
        Then the "Page Header" is not visible

    @example_app @content @checks @element_visible @xfail
    Scenario: XFail: The visibility check responds for invisible objects
        Given that the browser is at "localhost-hello"
        Then the "Hidden Content" is visible

    @example_app @content @checks @element_visible @xfail
    Scenario: XFail: The visibility check responds for missing objects
        Given that the browser is at "localhost-hello"
        Then the "Missing Link" is visible

    @example_app @content @checks @nth_element_contains_text
    Scenario: The Nth item sentence finds the correct item and asserts its text
        Given that the browser is at "localhost-hello"
        Then the 2nd label in the "form" contains the text "Optional input"

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

    @example_app @content @checks @nth_element_contains_text @xfail
    Scenario: Xfail: The Nth item sentence responds with missing input
        Given that the browser is at "localhost-hello"
        Then the 2nd label in the "form" contains the text "Required input"

    @example_app @content @checks @nth_element_contains_text @xfail
    Scenario: Xfail: The Nth item sentence responds with not enough inputs
        Given that the browser is at "localhost-hello"
        Then the 99th label in the "form" contains the text "Required input"

    @example_app @content @checks @nth_element_contains_text @xfail
    Scenario: Xfail: The Nth item sentence responds with not found
        Given that the browser is at "localhost-hello"
        Then the 1st word in the "Missing Link" contains the text "Not"

    @example_app @content @checks @page_title
    Scenario: The Demo App Page Title is "Hello World"
        Given that the browser is at "localhost-hello"
        Then the page title should be "Hello World"

    @example_app @content @checks @page_title @exceptions
    Scenario: The Demo App Page Title is not "Goodbye World"
        Given that the browser is at "localhost-hello"
        Then it is not the case that the page title should be "Goodbye World"
        Then the statement that 'the page title should be "Goodbye World"' responds with
          """
          The page title was supposed to be "Goodbye World" but was "Hello World".
          """

    @example_app @content @checks @page_title @xfail
    Scenario: XFail: The Demo App Page Title is not "Goodbye World"
        Given that the browser is at "localhost-hello"
        Then the page title should be "Goodbye World"
