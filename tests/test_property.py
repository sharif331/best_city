from pages.home_page import HomePage
from pages.property_page import PropertyPage


class TestProperty(HomePage, PropertyPage):

    def test_property_navigation(self):
        self.open_home()
        self.click_on_property_nav()
        assert "/properties" in self.current_url(), "Wrong property detail URL."
        assert self.title_is_visible(), "Property title not visible."
        self.click_first_invest()
        assert self.property_detail_is_visible(), "property details is not visible"

