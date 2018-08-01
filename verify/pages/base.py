import os.path
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_DIR = os.path.join(BASE_DIR, 'fixtures')


class Page(object):

    name = 'base'

    class PageElements(object):
        """ A container object that holds the Python object representations
        of a given page fixture.
        """
        def __init__(self, configuration):
            self.__dict__.update(**configuration)

    class InvalidConfiguration(Exception):
        pass

    def __init__(self, name, browser):
        self.name = name
        self.browser = browser
        self.find_selectors = {
            # General Selectors
            'id': browser.find_by_id,
            'css': browser.find_by_css,
            'name': browser.find_by_name,
            'tag': browser.find_by_tag,
            'text': browser.find_by_text,
            'value': browser.find_by_value,
            'xpath': browser.find_by_xpath,

            # Link Selectors
            'link.href': browser.find_link_by_href,
            'link.partial_href': browser.find_link_by_partial_href,
            'link.partial_text': browser.find_link_by_partial_text,
            'link.text': browser.find_link_by_text,

            # Option Selectors
            'option.text': browser.find_option_by_text,
            'option.value': browser.find_option_by_value,
        }

        self.presence_selectors = {
            'id': browser.is_element_present_by_id,
            'css': browser.is_element_present_by_css,
            'name': browser.is_element_present_by_name,
            'tag': browser.is_element_present_by_tag,
            'text': browser.is_element_present_by_text,
            'value': browser.is_element_present_by_value,
            'xpath': browser.is_element_present_by_xpath,
        }

        self.abscence_selectors = {
            'id': browser.is_element_not_present_by_id,
            'css': browser.is_element_not_present_by_css,
            'name': browser.is_element_not_present_by_name,
            'tag': browser.is_element_not_present_by_tag,
            'text': browser.is_element_not_present_by_text,
            'value': browser.is_element_not_present_by_value,
            'xpath': browser.is_element_not_present_by_xpath,
        }

        # Load the configuration for this page.
        fixture = os.path.join(FIXTURES_DIR, f'{self.name}.json')

        try:
            with open(fixture) as f:
                fixture_config = json.load(f)
        except FileNotFoundError:
            raise Page.InvalidConfiguration(
                f'Unable to load configuration file for page named: {self.name}. '
                f'Please ensure that a configuration object exists in {FIXTURES_DIR}. '
                f'\nThe file should take the form: {self.name}.json'
            )

        # Save the page elements config to the elements object. Then spread
        # the rest of the config into ourselves.
        self._elements = Page.PageElements(fixture_config.pop('elements'))
        self.__dict__.update(**fixture_config)

    def __getattr__(self, name):
        property = getattr(self._elements, name)
        return self.find(property['selector'], property['by'])

    # Public Methods

    def find(self, selector, by='id', **kwargs):
        """ Given a method and a selector, attempt to find the given element
        with the selector by the given method. The default method is by ID. All
        additional kwargs are passed to the selector method.

        Example
        -------

        page.find('submitButton')
        page.find('button[type="submit"]', by='css')
        """
        method = self.find_selectors[by]
        return method(selector, **kwargs)

    def wait_for(self, selector, by=None, present=True, **kwargs):
        if by is None:
            by = getattr(self._elements, selector)['by']

        if present:
            method = self.presence_selectors[by]
        else:
            method = self.abscence_selectors[by]
        return method(selector, **kwargs)
