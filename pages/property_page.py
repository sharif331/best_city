from selenium.webdriver.common.by import By
from base import BaseClass


class PropertyPage(BaseClass):

    invest_button = (By.XPATH, "//button[contains(text(), 'Invest Now')]")
    property_details = (By.XPATH, "//h2[contains(text(), 'Property Details')]")

    def open_home(self):
        self.open("/")

    def click_first_invest(self):
        self.click(self.invest_button)

    def property_detail_is_visible(self):
        return self.is_visible(self.property_details)
