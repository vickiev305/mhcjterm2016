from unittest import skip
from .base import TodoFunctionalTest


class ItemValidationTest(TodoFunctionalTest):
    def test_cannot_add_empty_list_item(self):
        #Edith goes to the homepage and tries to
        #submit an empty list item.
        #She hits "Enter" on the empty input box
        self.browser.get(self.live_server_url)
        self.enter_a_new_item('')

        #The homepage refreshes, and there is an error message
        #saying that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")


        #she tries again with some text for the item which now works
        self.enter_a_new_item('Buy milk')
        self.check_for_row_in_list_table('Buy milk')

        #Perversely tries to enter a second blank Item
        self.enter_a_new_item('')

        #She receives a similar warning on the list page
        self.check_for_row_in_list_table('Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #And she can correct it by fillinf some text in
        self.enter_a_new_item('Make tea')
        self.check_for_row_in_list_table('Buy milk')
        self.check_for_row_in_list_table('Make tea')
