from plugins.base_plugin.base_plugin import BasePlugin
from PIL import Image
import io
import requests
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

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
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument(f"--window-size=1920,1080")
        
        driver = webdriver.Chrome() #options=chrome_options)

        driver.get(url)
        png = driver.get_screenshot_as_png()
        driver.quit()

        image = Image.open(io.BytesIO(png))
        return image
