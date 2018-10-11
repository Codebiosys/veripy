@configure.SETUP_EXAMPLE @skip
Feature: Setup Sentences
    Setup sentences are parsed by tag, and do setup and/or teardown

    Scenario: I do setup
        Given we have behave installed

    Scenario Outline: Test that the system can handle Scenario outlines
        Given that the browser is at "<page-name>"
        Then the browser should be at "<page-name>"
        Then the page title should be "<page-title>"

        Examples: Page Name "<name>"
        | name          | page-name          | page-title  |
        | Localhost     | localhost-hello    | Hello World |
        | Other Page    | other-page          | Other Page |

    @teardown
    Scenario: I do teardown
        Given we have behave installed
