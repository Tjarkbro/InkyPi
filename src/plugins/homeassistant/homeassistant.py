<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from plugins.base_plugin.base_plugin import BasePlugin
import requests
<<<<<<< HEAD
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
=======
import pytz
>>>>>>> 06b2d54 (Upgrade for setting entities by yourself)
=======
from plugins.base_plugin.base_plugin import BasePlugin
import requests
import pytz
>>>>>>> a1f700bd4f5de2b2565085cf1a6e0470f561deff
import logging
from datetime import datetime

logger = logging.getLogger(__name__)
<<<<<<< HEAD
>>>>>>> 83b6be5 (Home assistant)
=======
>>>>>>> a1f700bd4f5de2b2565085cf1a6e0470f561deff

DEFAULT_TIMEZONE = "US/Eastern"
UNITS = {
    "standard": {
        "temperature": "°C",
        "speed": "m/s",
        "humidity": "%",
        "energy": "kWh"
    }
}
# Idee: http://192.168.178.122:8123/api/config vewenden, um Config direkt daraus zu speisen

class HomeAssistantPlugin(BasePlugin):
    def generate_settings_template(self):
        template_params = super().generate_settings_template()
        template_params['style_settings'] = True
        return template_params
    
    def generate_image(self, settings, device_config):    
        ha_url = settings.get("ha_url") # schon in HTML
        ha_token = settings.get("ha_token", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2MmQzMmMwNTMzNmM0NTk2ODZiZmI3ZTlhYTg2MTY5ZiIsImlhdCI6MTc0MzM1Mzk2MiwiZXhwIjoyMDU4NzEzOTYyfQ.XqW6_a8fsSAhz7j77NClRY2V3Ofhffp4BhSDNVfpYPc")

        headers = {"Authorization": f"Bearer {ha_token}", "Content-Type": "application/json"}
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 83b6be5 (Home assistant)
=======
        temp_unit = settings.get("temp_unit", "°C")
>>>>>>> c2adcd1 (home assistant)
=======
        units = settings.get('units')
>>>>>>> 7b122af (home assistant css)
=======
        title = settings.get("title", "Home Assistant")
        units = settings.get('units', 'standard')
>>>>>>> 06b2d54 (Upgrade for setting entities by yourself)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0b30510 (titel)

=======
>>>>>>> 4889497 (test)
        # API-Anfragen
        temp = self.get_state(ha_url, headers, entities["temp"])
        strom = self.get_state(ha_url, headers, entities["strom"])
        fenster = self.get_state(ha_url, headers, entities["fenster"])
=======
        # # API-Anfragen
        # temp = self.get_state(ha_url, headers, entities["temp"])
        # strom = self.get_state(ha_url, headers, entities["strom"])
        # fenster = self.get_state(ha_url, headers, entities["fenster"])

=======
>>>>>>> fd79c66 (humidity)
=======
        title = settings.get("title", "Home Assistant")
        units = settings.get('units', 'standard')

>>>>>>> a1f700bd4f5de2b2565085cf1a6e0470f561deff
        numberRooms = int(settings.get('numberRooms', 1))  # Anzahl der Räume abrufen
        rooms_data = {}
        for i in range(1, numberRooms + 1):
            room_name = settings.get(f"room_name_{i}")
            entity_temp = settings.get(f"sensor_temp_{i}")
            entity_humidity = settings.get(f"sensor_humidity_{i}")
            entity_window = settings.get(f"sensor_window_{i}")
            # entity_temp = f"sensor.aqara_luftsensor_{room_name.lower()}_temperature"  # Sensor-Entity für Temperatur
            # entity_humidity = f"sensor.aqara_luftsensor_{room_name.lower()}_humidity"  # Sensor-Entity für Feuchtigkeit
            # entity_window = f"binary_sensor.aqara_fenstersensor_{room_name.lower()}_window_contact"  # Fensterstatus

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
<<<<<<< HEAD
>>>>>>> 94c4a29 (Multiple Rooms)

        # Bild erstellen
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 83b6be5 (Home assistant)
=======

        # Bild erstellen
>>>>>>> a1f700bd4f5de2b2565085cf1a6e0470f561deff
        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0b30510 (titel)
=======
>>>>>>> 4889497 (test)
=======
=======
        # # Template-Parameter vorbereiten
        # image_template_params = {
        #     "title": title,
        #    # "current_date": dt.strftime("%A, %B %d"),
        #     "temperature": temp,
        #     "temperature_unit": UNITS[units]["temperature"],
        #     "power_usage": strom,
        #     "energy_unit": UNITS[units]["energy"],
        #     "window_status": "Offen" if fenster == "on" else "Geschlossen",
        #     "plugin_settings": settings,
        #     "units": units
        # }

>>>>>>> 94c4a29 (Multiple Rooms)
=======
>>>>>>> fd79c66 (humidity)
=======
=======
>>>>>>> a1f700bd4f5de2b2565085cf1a6e0470f561deff
        # Aktuelles Datum und Uhrzeit abrufen
        timezone_name = device_config.get_config("timezone") or DEFAULT_TIMEZONE
        tz = pytz.timezone(timezone_name)
        current_datetime  = datetime.now(tz)
        formatted_date = current_datetime.strftime("%d.%m.%Y")  # Format: TT.MM.JJJJ
        formatted_time = current_datetime.strftime("%H:%M")  # Format: HH:MM

<<<<<<< HEAD
>>>>>>> c4c988f (date und time)
        # Template-Parameter vorbereiten
>>>>>>> 83b6be5 (Home assistant)
=======
        # Template-Parameter vorbereiten
>>>>>>> a1f700bd4f5de2b2565085cf1a6e0470f561deff
        image_template_params = {
            "title": title,
            "date": formatted_date,
            "time": formatted_time,
            "rooms": rooms_data,
            "plugin_settings": settings,
            "units": units
        }

<<<<<<< HEAD
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
=======
        image = self.render_image(dimensions, "homeassistant.html", "homeassistant.css", image_template_params)
>>>>>>> a1f700bd4f5de2b2565085cf1a6e0470f561deff

        return image
    
    def get_state(self, url, headers, entity_id):
        """ Ruft den aktuellen Zustand einer Entität ab """
        try:
            response = requests.get(f"{url}/api/states/{entity_id}", headers=headers)
            response.raise_for_status()
            return response.json().get("state", "N/A")
        except requests.RequestException as e:
            logger.error(f"Fehler beim Abrufen des Zustands für {entity_id}: {e}")
            return f"Fehler: {e}"
