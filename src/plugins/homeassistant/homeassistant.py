from plugins.base_plugin.base_plugin import BasePlugin
import requests
import logging

logger = logging.getLogger(__name__)

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
        title = settings.get("title")

        # API-Anfragen
        temp = self.get_state(ha_url, headers, entities["temp"])
        strom = self.get_state(ha_url, headers, entities["strom"])
        fenster = self.get_state(ha_url, headers, entities["fenster"])

        # Bild erstellen
        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]

        # Template-Parameter vorbereiten
        image_template_params = {
            "title": title,
            "temperature": temp,
            "power_usage": strom,
            "window_status": "Offen" if fenster == "on" else "Geschlossen",
            "plugin_settings": settings
        }

        image = self.render_image(dimensions, "homeassistant.html", "homeassistant.css", image_template_params)

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
