@configure.FOO
Feature: Setup Sentences
    Setup sentences are parsed by tag, and do setup and/or teardown

    @setup
    Scenario: I do setup
        Given we have behave installed

    @teardown
    Scenario: I do teardown
        Given we have behave installed
