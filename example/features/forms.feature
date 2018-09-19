Feature: Form Sentences
    Form sentences allow a tester to interact with forms

    @example_app @forms @actions @clear_input
    Scenario: The Demo App form field can be cleared
        Given that the browser is at "localhost-hello"
        Then the "Default Field" has the value "Default Value"
        Then take a screen shot

        When the user clears the "Default Field"
        Then the "Default Field" has an empty value
        Then take a screen shot

    @example_app @forms @actions @clear_input @exceptions
    Scenario: The clear input sentence handles the input not being found
        Given that the browser is at "localhost-hello"
        Then if 'the user clears the "Missing Field"', the system responds with
            """
            The "Missing Field" was not found on the page.
            """

    @example_app @forms @actions @enter_input_from_file
    Scenario: The Demo App form field can be entered from a file
        Given that the browser is at "localhost-hello"
        Then the "Textarea Field" has an empty value
        Then take a screen shot

        When the content from "copyable-file.txt" is entered into the "Textarea Field"
        Then it is not the case that the "Textarea Field" has an empty value
        Then take a screen shot


    @example_app @forms @actions @enter_input_from_file @exceptions
    Scenario: The file entry sentence handles missing files or form fields
        Given that the browser is at "localhost-hello"
        Then if 'the content from "copyable-file.txt" is entered into the "Missing Field"', the system responds with
            """
            The "Missing Field" was not found on the page.
            """
        Then if 'the content from "missing-file.txt" is entered into the "Textarea Field"', the system responds with
            """
            The specified file does not exist.
            """


    @example_app @forms @actions @enter_text_into_current
    Scenario: The tester can press keyboard keys
        Given that the browser is at "localhost-hello"
        When "Example Text" is entered into the "Required Field"
        When the user presses the "tab" key
        When "New Text" is entered into the current field
        Then the "Optional Field" has the value "New Text"
        Then take a screen shot


    @example_app @forms @actions @enter_text_into_field
    Scenario: A specified input can have text intered into it
        Given that the browser is at "localhost-hello"
        When "Example Text" is entered into the "Default Field"
        Then the "Default Field" has the value "Example Text"
        Then take a screen shot


    @example_app @forms @actions @enter_text_into_field @exceptions
    Scenario: The system responds correctly when an error occurs entering text
        Given that the browser is at "localhost-hello"
        Then if '"Example Text" is entered into the "Disabled Field"', the system responds with
            """
            The "Disabled Field" cannot accept text.
            """
        Then if '"Example Text" is entered into the "Other Page Link"', the system responds with
            """
            The "Other Page Link" cannot accept text.
            """
        Then if '"Example Text" is entered into the "Missing Field"', the system responds with
            """
            The "Missing Field" was not found on the page.
            """


    @example_app @forms @actions @select_option
    Scenario: A select field can have an option selected
        Given that the browser is at "localhost-hello"
        When "green" is selected for "Select Field"
        Then the "Select Field" has the value "green"
        Then take a screen shot


    @example_app @forms @actions @select_option @exceptions
    Scenario: The system responds correctly when a select field can have not an option selected
        Given that the browser is at "localhost-hello"
        Then if '"yellow" is selected for "Select Field"', the system responds with
          """
          "Select Field" has no option with value "yellow".
          """
        Then if '"green" is selected for "Missing Field"', the system responds with
          """
          The "Missing Field" was not found on the page.
          """


    @example_app @forms @actions @upload_file_to_field
    Scenario: A file can be uploaded to a field
        Given that the browser is at "localhost-hello"
        Then the "File Upload Field" has an empty value
        Then take a screen shot

        When the file "uploadable-file.txt" has been added to the "File Upload Field"
        Then it is not the case that the "File Upload Field" has an empty value
        Then take a screen shot


    @example_app @forms @actions @upload_file_to_field @exceptions
    Scenario: The file upload sentence handles missing files or form fields
        Given that the browser is at "localhost-hello"
        Then if 'the file "uploadable-file.txt" has been added to the "Missing Field"', the system responds with
            """
            The "Missing Field" was not found on the page.
            """
        Then if 'the file "missing-file.txt" has been added to the "File Upload Field"', the system responds with
            """
            The specified file does not exist.
            """


    @example_app @forms @checks @field_accepts_type
    Scenario: The fields can accept certain types of data
        Given that the browser is at "localhost-hello"
        Then the "Text Field" field does accept text
        Then the "Text Field" field does not accept numbers
        Then the "Number Field" field does accept numbers
        Then the "Number Field" field does not accept passwords
        Then the "File Upload Field" field does accept files
        Then take a screen shot

    @example_app @forms @checks @field_accepts_type @exceptions
    Scenario: The check that fields can accept certain types of data handles errors correctly
        Given that the browser is at "localhost-hello"
        Then the statement that 'the "Text Field" field does not accept text' responds with
            """
            "Text Field" is not supposed to accept text but did.
            """
        Then the statement that 'the "Text Field" field does accept numbers' responds with
            """
            "Text Field" is supposed to accept number but did not.
            """
        Then the statement that 'the "Missing Field" field does accept text' responds with
            """
            The "Missing Field" was not found on the page.
            """


    @example_app @forms @checks @field_disabled
    Scenario: The fields can be enabled or disabled
        Given that the browser is at "localhost-hello"
        Then the "Enabled Field" field is enabled
        Then the "Disabled Field" field is not enabled
        Then take a screen shot


    @example_app @forms @checks @field_disabled @exceptions
    Scenario: The check that fields are enabled or disabled handles errors correctly
        Given that the browser is at "localhost-hello"
        Then the statement that 'the "Enabled Field" field is not enabled' responds with
            """
            "Enabled Field" is supposed to be disabled and it was not.
            """
        Then the statement that 'the "Disabled Field" field is enabled' responds with
            """
            "Disabled Field" is supposed to be enabled and it was not.
            """
        Then the statement that 'the "Missing Field" field is enabled' responds with
            """
            The "Missing Field" was not found on the page.
            """


    @example_app @forms @checks @field_required
    Scenario: The fields can be required or optional
        Given that the browser is at "localhost-hello"
        Then the "Optional Field" field is not required
        Then it is not the case that the "Optional Field" field is required
        Then the "Required Field" field is required
        Then it is not the case that the "Required Field" field is not required
        Then take a screen shot


    @example_app @forms @checks @field_required @exception
    Scenario: The check that fields are required or optional handles errors correctly
        Given that the browser is at "localhost-hello"
        Then the statement that 'the "Required Field" field is not required' responds with
            """
            "Required Field" is supposed to be optional and it was not.
            """
        Then the statement that 'the "Optional Field" field is required' responds with
            """
            "Optional Field" is supposed to be required and it was not.
            """
        Then the statement that 'the "Missing Field" field is required' responds with
            """
            The "Missing Field" was not found on the page.
            """
