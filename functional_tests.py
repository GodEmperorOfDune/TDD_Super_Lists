from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # user is invited to enter a to-do item right away

        # they enter their task into a text box

        # when they hit enter the page updates and the page now lists 1: to-do task

        # there is still a text box for adding more items

        # the user enters more text and hits enter the page updates again and now has a list of both items

        # the site generates a unique URL for this list to remember it for later - there is text to explain this

        # the user visits the URL and the to-do list is still there

        # User checks the homepage of an online to-do list app
if __name__ == '__main__':
    unittest.main()