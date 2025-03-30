<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
<<<<<<< HEAD
>>>>>>> ff4d02d (From Selenium)
=======
from selenium.webdriver.chrome.service import Service
>>>>>>> 4e55a9d (Service Selenium)
=======
>>>>>>> 72fb6c6 (Service Path Chrome)
from plugins.base_plugin.base_plugin import BasePlugin
from PIL import Image
from utils.image_utils import take_screenshot
import logging

logger = logging.getLogger(__name__)

class Screenshot(BasePlugin):
    def generate_image(self, settings, device_config):

        url = settings.get('url')
        if not url:
            raise RuntimeError("URL is required.")

        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]

        logger.info(f"Taking screenshot of url: {url}")

        image = take_screenshot(url, dimensions, timeout_ms=40000)

        if not image:
            raise RuntimeError("Failed to take screenshot, please check logs.")

        return image
=======
=======
>>>>>>> 395b136 (Rename plugin)
from plugins.base_plugin import BasePlugin
=======
from plugins.base_plugin.base_plugin import BasePlugin
>>>>>>> a9374bf (Import Base Plugin correctly)
from PIL import Image
import io
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

class Screenshot(BasePlugin):
    def generate_image(self, settings, device_config):
        ip_address = settings.get('ip_address')
        if not ip_address:
            raise RuntimeError("IP-Adresse nicht angegeben.")

        url = f"http://{ip_address}"
        screenshot = self.capture_screenshot(url)

        # Bild auf die Displaygröße skalieren
        display_width = device_config.get('display_width', 600)
        display_height = device_config.get('display_height', 448)
        screenshot = screenshot.resize((display_width, display_height), Image.ANTIALIAS)

        return screenshot

    def capture_screenshot(self, url):
        firefox_options = Options()
        firefox_options.binary_location = "/usr/bin/firefox"  # Falls Firefox woanders ist, anpassen!
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        #firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument(f"--window-size=1920,1080")
        firefox_options.add_argument("--disable-extensions")

        service = Service("/usr/local/bin/geckodriver", log_output='/tmp/geckodriver.log')  # Stelle sicher, dass dies der richtige Pfad ist!

        driver = webdriver.Firefox(service=service, options=firefox_options)

        driver.get(url)
        png = driver.get_screenshot_as_png()
        driver.quit()

        image = Image.open(io.BytesIO(png))
        return image
<<<<<<< HEAD
>>>>>>> 395b136 (Rename plugin)
=======
>>>>>>> 395b136 (Rename plugin)
