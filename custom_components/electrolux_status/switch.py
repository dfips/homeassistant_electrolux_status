"""Switch platform for Electrolux Status."""
from homeassistant.components.switch import SwitchEntity

from .const import SWITCH, DOMAIN
from .entity import ElectroluxEntity
import logging

_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup_entry(hass, entry, async_add_entities):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    appliances = coordinator.data.get('appliances', None)
    if appliances is not None:
        for appliance_id, appliance in appliances.appliances.items():
            entities = [entity for entity in appliance.entities if entity.entity_type == SWITCH]
            _LOGGER.debug("Electrolux add %d sensors to registry for appliance %s", len(entities), appliance_id)
            async_add_entities(entities)


class ElectroluxSwitch(ElectroluxEntity, SwitchEntity):
    """Electrolux Status switch class."""

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        value = self.extract_value()
        if value is None:
            return self._cached_value
        else:
            self._cached_value = value
        return value

    async def async_turn_on(self, **kwargs):
        """Turn the entity on."""
        _LOGGER.error("Not supported yet")

    async def async_turn_off(self, **kwargs):
        """Turn the entity off."""
        _LOGGER.error("Not supported yet")
