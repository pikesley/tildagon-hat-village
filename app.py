from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable

import app

from .lib.background import Background
from .lib.character import Character

DEBUG = False


class HatVillage(app.App):
    """HatVillage."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)

    def update(self, _):
        """Update."""
        self.scan_buttons()

    def draw(self, ctx):
        """Draw."""
        self.overlays = []
        self.overlays.append(Background(colour=(0, 0, 0)))

        scale = 8
        offset = -70
        chars = [
            {"char": "H", "angle": -45, "colour": (1, 0, 0)},
            {"char": "A", "angle": 0, "colour": (0, 1, 0)},
            {"char": "T", "angle": 45, "colour": (0, 0, 1)},
        ]

        start = -offset
        for char in chars:
            self.overlays.append(
                Character(
                    char["char"],
                    scale,
                    offset,
                    char["angle"],
                    char["colour"],
                )
            )
            start += offset

        self.draw_overlays(ctx)

        if DEBUG:
            ctx.rgb(0, 1, 0)
            ctx.begin_path()
            ctx.move_to(-120, 0)
            ctx.line_to(120, 0)
            ctx.move_to(0, 120)
            ctx.line_to(0, -120)
            ctx.stroke()

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()


__app_export__ = HatVillage
