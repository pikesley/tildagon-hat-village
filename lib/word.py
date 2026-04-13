from ..common.colour_tools import rgb_from_hue
from .character import Character
from .conf import conf
from .tools import assign_angles, assign_offsets


class Word:
    """Write letters 'n' shit, yo."""

    def __init__(self, params):
        """Construct."""
        self.text = params.get("text")
        self.scale = params.get("scale")
        self.offset = params.get("offset")
        self.angle = params.get("angle")
        self.hue = params.get("hue")
        self.hue_gap = params.get("hue-gap", 0)
        self.colour = rgb_from_hue(self.hue)

        self.offsets = None
        self.angles = None

        if params.get("angle"):
            self.angles = assign_angles(len(self.text), self.angle)
        else:
            self.offsets = assign_offsets(len(self.text), self.scale)

    def letters(self, app):
        """Letters."""
        for index, letter in enumerate(self.text):
            colour = rgb_from_hue(self.hue + (self.hue_gap * index))
            params = {
                "char": letter,
                "scale": self.scale,
                "offset": self.offset,
                "colour": colour,
                "opacity": conf["letter-opacity"],
            }

            if self.angles:
                params["angle"] = self.angles[index]
            if self.offsets:
                params["x-offset"] = self.offsets[index]

            app.overlays.append(Character(params))
