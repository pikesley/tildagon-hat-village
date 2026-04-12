from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable

import app

from .lib.background import Background
from .lib.conf import font
from .lib.rectangle import Rectangle

DEBUG = True


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

        self.x = 0
        self.y = 0
        self.scale = 4
        start_x = self.x - (8 * self.scale / 2)
        start_y = self.y - (8 * self.scale / 2)
        for item in font["H"]:
            colour = (1, 0, 0, 1)
            left = item["x"] * self.scale
            width = item["width"] * self.scale
            top = item["y"] * self.scale
            height = item["height"] * self.scale

            self.overlays.append(
                Rectangle(
                    start_x + left,
                    width,
                    start_y + top,
                    height,
                    colour,
                )
            )

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
