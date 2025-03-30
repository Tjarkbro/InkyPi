from plugins.base_plugin.base_plugin import BasePlugin
import requests
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

UNITS = {
    "standard": {
        "temperature": "°C",
        "speed": "m/s",
        "humidity": "%",
        "energy": "kWh"
    }
}

class HomeAssistantPlugin(BasePlugin):
    def generate_settings_template(self):
        template_params = super().generate_settings_template()
        template_params['style_settings'] = True
        return template_params
    
    def generate_image(self, settings, device_config):    
        ha_url = settings.get("ha_url") # schon in HTML
        ha_token = settings.get("ha_token", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2MmQzMmMwNTMzNmM0NTk2ODZiZmI3ZTlhYTg2MTY5ZiIsImlhdCI6MTc0MzM1Mzk2MiwiZXhwIjoyMDU4NzEzOTYyfQ.XqW6_a8fsSAhz7j77NClRY2V3Ofhffp4BhSDNVfpYPc")

        headers = {"Authorization": f"Bearer {ha_token}", "Content-Type": "application/json"}
        title = settings.get("title")
        units = settings.get('units')

        numberRooms = int(settings.get('numberRooms', 1))  # Anzahl der Räume abrufen
        rooms_data = {}
        for i in range(1, numberRooms + 1):  # Durch alle Räume iterieren
            room_name = settings.get(f"room_name_{i}", f"Raum_{i}")  # Falls leer, Standardname
            entity_temp = f"sensor.aqara_luftsensor_{room_name.lower()}_temperature"  # Sensor-Entity für Temperatur
            entity_humidity = f"sensor.aqara_luftsensor_{room_name.lower()}_humidity"  # Sensor-Entity für Feuchtigkeit
            entity_window = f"binary_sensor.aqara_fenstersensor_{room_name.lower()}_window_contact"  # Fensterstatus

            temp = self.get_state(ha_url, headers, entity_temp)
            humidity = self.get_state(ha_url, headers, entity_humidity)
            window_status = self.get_state(ha_url, headers, entity_window)

            rooms_data[room_name] = {
                "temperature": temp,
                "temperature_unit": UNITS[units]["temperature"],
                "humidity": humidity,
                "humidity_unit": UNITS[units]["humidity"],
                "window_status": "Offen" if window_status == "on" else "Geschlossen"
            }

        # Bild erstellen
        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]

        # Aktuelles Datum und Uhrzeit abrufen
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%d.%m.%Y")  # Format: TT.MM.JJJJ
        formatted_time = current_datetime.strftime("%H:%M:%S")  # Format: HH:MM:SS

        # Template-Parameter vorbereiten
        image_template_params = {
            "title": title,
            "date": formatted_date,
            "time": formatted_time,
            "rooms": rooms_data,
            "plugin_settings": settings,
            "units": units
        }

        image = self.render_image(dimensions, "homeassistant.html", "homeassistant.css", image_template_params)

        return image
    
    def get_state(self, url, headers, entity_id):
        """ Ruft den aktuellen Zustand einer Entität ab """
        try:
            response = requests.get(f"{url}/api/states/{entity_id}", headers=headers)
            response.raise_for_status()
            return response.json().get("state", "N/A")
        except requests.RequestException as e:
            return f"Fehler: {e}"
