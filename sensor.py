import logging

from homeassistant.components.sensor import SensorEntity

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([dog()])

class dog(SensorEntity):
    def __init__(self):
        self._state = true
        self._attributes = {"last_pee": "12:00", "last_poo": "12:00", "last_fed": "12:00", "last_crated": "12:00"}

    @property
    def name(self):
        return "dog"

    @property
    def state(self):
        return self._state

    @property
    def device_state_attributes(self):
        return self._attributes

    @property
    def unique_id(self):
        return "dog"
