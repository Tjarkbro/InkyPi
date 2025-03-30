from plugins.base_plugin.base_plugin import BasePlugin
import requests
from PIL import Image, ImageDraw, ImageFont

class HomeAssistantPlugin(BasePlugin):
    def generate_image(self, settings, device_config):
        """ Erstellt ein Bild mit Daten von der Home Assistant API """
        
        ha_url = settings.get("ha_url", "http://192.168.178.122:8123")
        ha_token = settings.get("ha_token", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2MmQzMmMwNTMzNmM0NTk2ODZiZmI3ZTlhYTg2MTY5ZiIsImlhdCI6MTc0MzM1Mzk2MiwiZXhwIjoyMDU4NzEzOTYyfQ.XqW6_a8fsSAhz7j77NClRY2V3Ofhffp4BhSDNVfpYPc")
        entities = settings.get("entities", {
            "temp": "sensor.wohnzimmer_temperature",
            "strom": "sensor.stromverbrauch",
            "fenster": "binary_sensor.fenster_wohnzimmer"
        })

        headers = {"Authorization": f"Bearer {ha_token}", "Content-Type": "application/json"}
        title = "Titel"

        # API-Anfragen
        temp = self.get_state(ha_url, headers, entities["temp"])
        strom = self.get_state(ha_url, headers, entities["strom"])
        fenster = self.get_state(ha_url, headers, entities["fenster"])

        # Bild erstellen
        image_template_params = {
            "title": title
        }

        display_width = device_config.get('display_width', 600)
        display_height = device_config.get('display_height', 448)

        image = Image.new((display_width, display_height), image_template_params)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        # Daten auf das Bild zeichnen
        draw.text((10, 10), f"🌡 Temperatur: {temp}°C", font=font, fill=0)
        draw.text((10, 40), f"⚡ Stromverbrauch: {strom} kWh", font=font, fill=0)
        draw.text((10, 70), f"🚪 Fenster: {'Offen' if fenster == 'on' else 'Geschlossen'}", font=font, fill=0)

        return image

    def get_state(self, url, headers, entity_id):
        """ Ruft den aktuellen Zustand einer Entität ab """
        try:
            response = requests.get(f"{url}/api/states/{entity_id}", headers=headers)
            response.raise_for_status()
            return response.json().get("state", "N/A")
        except requests.RequestException as e:
            return f"Fehler: {e}"
