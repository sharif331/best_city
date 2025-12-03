from selenium.webdriver.common.by import By
from base import BaseClass


class HomePage(BaseClass):

    title = (By.XPATH, "//h1 | //h2[contains(@class, 'title')]")
    property_header_nav = (By.XPATH, "//a[@href='/properties' and text()='Properties']")

    def open_home(self):
        self.open("/")

    def click_on_property_nav(self):
        self.click(self.property_header_nav)

    def title_is_visible(self):
        return self.is_visible(self.title)
