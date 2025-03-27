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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class Screenshot(BasePlugin):
    def generate_image(self, settings, device_config):
        ip_address = settings.get('ip_address')
        if not ip_address:
            raise RuntimeError("IP-Adresse nicht angegeben.")

        url = f"http://{ip_address}"
        screenshot = self.capture_screenshot(url)

        # Bild auf die Displaygröße skalieren
        display_width = device_config.get('display_width', 600)  # Standardwerte anpassen
        display_height = device_config.get('display_height', 448)
        screenshot = screenshot.resize((display_width, display_height), Image.ANTIALIAS)

        return screenshot

    def capture_screenshot(self, url):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument(f"--window-size=1920,1080")
        
        service = Service("/usr/lib/chromium-browser/chromedriver")  # Pfad anpassen, falls nötig
        driver = webdriver.Chrome(service=service, options=chrome_options)

        #driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
        driver.get(url)
        png = driver.get_screenshot_as_png()
        driver.quit()

        image = Image.open(io.BytesIO(png))
        return image
<<<<<<< HEAD
>>>>>>> 395b136 (Rename plugin)
=======
>>>>>>> 395b136 (Rename plugin)
