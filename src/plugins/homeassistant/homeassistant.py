<<<<<<< HEAD
<<<<<<< HEAD
from plugins.base_plugin.base_plugin import BasePlugin
import requests
<<<<<<< HEAD
=======
import requests
from plugins.base_plugin import BasePlugin
>>>>>>> 0d9077a (homeassistant)
=======
from plugins.base_plugin.base_plugin import BasePlugin
import requests
>>>>>>> d4b9274 (BasePlugin fix)
from PIL import Image, ImageDraw, ImageFont
=======
import logging

logger = logging.getLogger(__name__)
>>>>>>> 83b6be5 (Home assistant)

class HomeAssistantPlugin(BasePlugin):
    def generate_settings_template(self):
        template_params = super().generate_settings_template()
        template_params['style_settings'] = True
        return template_params
    
    def generate_image(self, settings, device_config):    
        ha_url = settings.get("ha_url") # schon in HTML
        ha_token = settings.get("ha_token", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2MmQzMmMwNTMzNmM0NTk2ODZiZmI3ZTlhYTg2MTY5ZiIsImlhdCI6MTc0MzM1Mzk2MiwiZXhwIjoyMDU4NzEzOTYyfQ.XqW6_a8fsSAhz7j77NClRY2V3Ofhffp4BhSDNVfpYPc")
        entities = settings.get("entities", {
            "temp": "sensor.aqara_luftsensor_wohnzimmer_temperature",
            "strom": "sensor.geschirrspuler_energy",
            "fenster": "binary_sensor.fenster_wohnzimmer"
        })

        headers = {"Authorization": f"Bearer {ha_token}", "Content-Type": "application/json"}
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        title = "Titel"
=======
>>>>>>> 0d9077a (homeassistant)
=======
        title = "Titel"
=======
        title = settings.get("title")
>>>>>>> 83b6be5 (Home assistant)

<<<<<<< HEAD
>>>>>>> 0b30510 (titel)

=======
>>>>>>> 4889497 (test)
        # API-Anfragen
        temp = self.get_state(ha_url, headers, entities["temp"])
        strom = self.get_state(ha_url, headers, entities["strom"])
        fenster = self.get_state(ha_url, headers, entities["fenster"])

        # Bild erstellen
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 83b6be5 (Home assistant)
        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]

<<<<<<< HEAD
>>>>>>> 0b30510 (titel)
=======
>>>>>>> 4889497 (test)
=======
        # Template-Parameter vorbereiten
>>>>>>> 83b6be5 (Home assistant)
        image_template_params = {
            "title": title,
            "temperature": temp,
            "power_usage": strom,
            "window_status": "Offen" if fenster == "on" else "Geschlossen",
            "plugin_settings": settings
        }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        image = Image.new("RGB", (600, 448), (255, 255, 255))
=======
        display_width = device_config.get("display_width", 600)
        display_height = device_config.get("display_height", 448)
=======
        display_width = device_config.get('display_width', 600)
        display_height = device_config.get('display_height', 448)
>>>>>>> 85c3065 (fix)
        image = Image.new("1", (display_width, display_height), 255)
>>>>>>> 0d9077a (homeassistant)
=======
        image = Image.new(dimensions, image_template_params)
>>>>>>> 0b30510 (titel)
=======
        display_width = device_config.get('display_width', 600)
        display_height = device_config.get('display_height', 448)

        image = Image.new((display_width, display_height), image_template_params)
>>>>>>> 4889497 (test)
=======
        image = Image.new((600, 448), image_template_params)
>>>>>>> 6d1df08 (test)
=======
        image = Image.new("RGB", (600, 448), (255, 255, 255))
>>>>>>> c559b91 (tupel)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        # Daten auf das Bild zeichnen
        draw.text((10, 10), f"🌡 Temperatur: {temp}°C", font=font, fill=0)
        draw.text((10, 40), f"⚡ Stromverbrauch: {strom} kWh", font=font, fill=0)
        draw.text((10, 70), f"🚪 Fenster: {'Offen' if fenster == 'on' else 'Geschlossen'}", font=font, fill=0)
=======
        image = self.render_image(dimensions, "homeassistant.html", "homeassistant.css", image_template_params)
>>>>>>> 83b6be5 (Home assistant)

        return image
    
  #  def parse_entities(self):


    def get_state(self, url, headers, entity_id):
        """ Ruft den aktuellen Zustand einer Entität ab """
        try:
            response = requests.get(f"{url}/api/states/{entity_id}", headers=headers)
            response.raise_for_status()
            return response.json().get("state", "N/A")
        except requests.RequestException as e:
            return f"Fehler: {e}"
