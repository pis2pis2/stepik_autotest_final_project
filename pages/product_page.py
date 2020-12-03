from .base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button add_to_basket is not presented"
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_be_book_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "book_name is not presented"
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_BASKET), "book_basket is not presented"
        book_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET).text
        assert book_name == book_basket, "Name is not same"

    def should_be_book_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "book_price is not presented"
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_BASKET), "basket_price is not presented"
        basket_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET).text
        assert book_price == basket_price, "Price is not same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"