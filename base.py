import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


def env_true(var):
    return os.environ.get(var, 'false') == 'true'


class BaseClass:
    """
    Unified Base Class for:
    - Selenium driver setup/teardown
    - Common reusable UI actions used by Page Objects
    """
    HEADLESS = env_true('HEADLESS')
    if os.environ.get('URL') is not None:
        base_url = os.environ.get('URL')
    else:
        base_url = "http://localhost:3000"

    def setup_method(self):
        chrome_options = Options()

        chrome_options.add_argument("--start-maximized")
        if env_true('HEADLESS'):
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        chrome_options.page_load_strategy = 'eager'
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        if self.driver:
            self.driver.quit()

    # -------------------------------------
    # Common Page Functions
    # -------------------------------------

    def open(self, path=""):
        url = self.base_url.rstrip("/") + path
        self.driver.get(url)

    def click(self, locator):
        """
        Clicks on an element:
        - waits until it's clickable
        - scrolls it into view
        - retries with JS click if normal click is intercepted
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))

        # Scroll into view (centered)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element
        )

        try:
            element.click()
        except ElementClickInterceptedException:
            # Fallback: JS click if something still intercepts it
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def wait_for(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text.strip()

    def current_url(self):
        return self.driver.current_url

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        return element

    def scroll_by_pixels(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

