from math import radians

from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable

import app

from .common.led_lighter import LEDLighter
from .common.rotation_monitor import RotationMonitor
from .lib.background import Background
from .lib.conf import conf
from .lib.word import Word


class HatVillage(app.App):
    """HatVillage."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.hue = 0
        self.leds = LEDLighter(conf["led-brightness"])
        self.rotation_manager = RotationMonitor()
        self.rotation = 0

        self.is_rotating = False

    def update(self, _):
        """Update."""
        self.scan_buttons()
        self.hue += conf["hue-increment"]
        self.leds.light(self.hue, self.hue + 0.5)

        if self.is_rotating:
            self.rotation += conf["rotation-rate"]

    def draw(self, ctx):
        """Draw."""
        self.rotation_manager.rotate(ctx)
        ctx.rotate(radians(self.rotation))

        self.overlays = [Background(colour=(0, 0, 0))]

        for item in conf["strings"]:
            params = {
                "text": item["text"],
                "scale": item["scale"],
                "offset": item["offset"],
                "hue": self.hue + item["hue-offset"],
                "hue-gap": 1 / len(item["text"] * item["hue-gap-factor"]),
            }
            if "total-angle" in item:
                params["angle"] = item["total-angle"] / (len(item["text"]) - 1)

            word = Word(params)
            word.letters(self)

        self.draw_overlays(ctx)

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

        if self.button_states.get(BUTTON_TYPES["UP"]):
            self.button_states.clear()
            self.is_rotating = False
            self.rotation = 0

        if self.button_states.get(BUTTON_TYPES["CONFIRM"]):
            self.button_states.clear()
            self.is_rotating = not self.is_rotating


__app_export__ = HatVillage
