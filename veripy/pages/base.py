import logging
import os.path
import json

from .. import settings
from ..utils import allow_retries


logger = logging.getLogger(__name__)


class Page(object):
    """ A page is a dynamic container for interacting with Browser elements
    using Splinter. A page is configured using a fixture config JSON file.
    Once the fixture JSON is loaded, elements in the file can be accessed as
    follows:

    **Example**::

        # Assuming there is a fixture in FIXTURES_DIR named "google.com.json"
        # then the page for 'google.com' can be loaded as follows.
        browser = get_browser()
        page = Page('google.com', browser)
        page['search_field'].fill('a search string')
        page['submit_button'].click()

    Elements are automatically selected using the configured selector for the
    given element. Once the item is returned, the normal Splinter methods can be
    used.

    **Example JSON Configuration**::

        // google.com.json
        {
            "url": "https://google.com/",
            "elements": {
                "search_field": {
                    "by": "id",
                    "selector": "lst-ib"
                },
                "submit_button": {
                    "by": "value",
                    "selector": "Google Search"
                }
            }
        }

    **Important Note:** Top-level configuration fields are spread into the Page
    object directly while elements must be accessed via dictionary-like getter
    methods.

    **Example Top-Level Attribute**::

        # Using the above google.com.json configuration, the URL attribute can be
        # accessed as follows:
        browser = get_browser()
        page = Page('google.com', browser)
        print(page.url)
        # >>> 'https://google.com/'
    """

    name = 'base'

    class PageElements(object):
        """ A container object that holds the Python object representations
        of a given page fixture.
        """
        def __init__(self, configuration):
            self.__dict__.update(**configuration)

    class InvalidConfiguration(Exception):
        pass

    class ElementNotFound(Exception):
        pass

    class MultipleElementsFound(Exception):
        pass

    def __init__(self, name, browser):
        self.name = name
        self.browser = browser

        # Load the configuration for this page.
        fixture = os.path.join(settings.FIXTURES_DIR, f'{self.name}.json')

        try:
            with open(fixture) as f:
                fixture_config = json.load(f)
        except FileNotFoundError:
            message = (
                f'Unable to load configuration file for page named: {self.name}. '
                f'Please ensure that a configuration object exists in {settings.FIXTURES_DIR}. '
                f'\nThe file should take the form: {self.name}.json'
            )
            logger.critical(message)
            raise Page.InvalidConfiguration(message)

        # Save the page elements config to the elements object. Then spread
        # the rest of the config into ourselves.
        self._elements = Page.PageElements(fixture_config.pop('elements'))
        self.__dict__.update(**fixture_config)
        logger.info(f'Finished initializing page: "{name}"')

    def __getitem__(self, name):
        property = self.get_element_properties(name)
        return self.find(property['selector'], property['by'], **property.get('kwargs', {}))

    def _find_selectors(self, by='id', parent=None):
        if parent is None:
            parent = self.browser
            selectors = {
                'id': parent.find_by_id,
                'css': parent.find_by_css,
                'name': parent.find_by_name,
                'tag': parent.find_by_tag,
                'text': parent.find_by_text,
                'value': parent.find_by_value,
                'xpath': parent.find_by_xpath,
                'link.href': parent.find_link_by_href,
                'link.partial_href': parent.find_link_by_partial_href,
                'link.partial_text': parent.find_link_by_partial_text,
                'link.text': parent.find_link_by_text,
                'option.text': parent.find_option_by_text,
                'option.value': parent.find_option_by_value,
            }
        else:
            selectors = {
                'id': parent.find_by_id,
                'css': parent.find_by_css,
                'name': parent.find_by_name,
                'tag': parent.find_by_tag,
                'text': parent.find_by_text,
                'value': parent.find_by_value,
                'xpath': parent.find_by_xpath,
            }
        return selectors[by]

    def _presence_selectors(self, by='id', parent=None):
        if parent is None:
            parent = self.browser

        selectors = {
            'id': parent.is_element_present_by_id,
            'css': parent.is_element_present_by_css,
            'name': parent.is_element_present_by_name,
            'tag': parent.is_element_present_by_tag,
            'text': parent.is_element_present_by_text,
            'value': parent.is_element_present_by_value,
            'xpath': parent.is_element_present_by_xpath,
        }
        return selectors[by]

    def _abscence_selectors(self, by='id', parent=None):
        if parent is None:
            parent = self.browser

        selectors = {
            'id': parent.is_element_not_present_by_id,
            'css': parent.is_element_not_present_by_css,
            'name': parent.is_element_not_present_by_name,
            'tag': parent.is_element_not_present_by_tag,
            'text': parent.is_element_not_present_by_text,
            'value': parent.is_element_not_present_by_value,
            'xpath': parent.is_element_not_present_by_xpath,
        }
        return selectors[by]

    # Public Methods

    def get_element_properties(self, name):
        """ Given a page element's name, return the configured properties for
        the element.

        Unless configured otherwise, the returned dictionary will contain a
        `selector` and `by` attributes. These will contain both the method to
        select the element and the selector's type.

        Example::

            { 'selector': '//div[@id="top"]/a', 'by': 'xpath' }
        """
        return getattr(self._elements, name)


    @allow_retries(retry_on=(ElementNotFound,), retries=1)
    def find(self, selector, by='id', allow_multiple=False, **kwargs):
        """ Given a method and a selector, attempt to find the given element
        with the selector by the given method. The default method is by ID. All
        additional kwargs are passed to the selector method.

        **Example**::

            page.find('submitButton')
            page.find('button[type="submit"]', by='css')
        """
        logger.info(f'Selecting element "{selector}" by "{by}" on page "{self.name}".')

        # Before we attempt to select the item, wait a max of 3 seconds to give
        # animations or other effects to render the item we need.
        self.wait_for(selector, by, wait_time=3)

        method = self._find_selectors(by)
        results = method(selector, **kwargs)

        if len(results) == 0:
            raise Page.ElementNotFound(
                f'The element described by "{selector}" was not found.'
            )

        visible_results = [result for result in results if result.visible]
        if not allow_multiple and len(visible_results) > 1:
            raise Page.MultipleElementsFound(
                f'The selector "{selector}" describes multiple visible elements.'
            )

        if allow_multiple:
            return results
        else:
            return results[0]

    def wait_for(self, selector, by=None, present=True, **kwargs):
        logger.info(f'Selecting element "{selector}" by "{by}" on page "{self.name}".')
        if by is None:
            by = getattr(self._elements, selector)['by']

        if present:
            method = self._presence_selectors(by)
        else:
            method = self._abscence_selectors(by)
        return method(selector, **kwargs)
