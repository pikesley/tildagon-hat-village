from .conf import font
from .rectangle import Rectangle


class Character:
    """A character."""

    def __init__(self, char, x, y, scale, colour, opacity=1):
        """Construct."""
        self.char = char
        self.x = x
        self.y = y
        self.scale = scale
        self.colour = list(colour) + [opacity]

        self.data = font[char]

    @property
    def pixels(self):
        """Draw."""
        pix = []

        start_x = self.x - (8 * self.scale / 2)
        start_y = self.y - (8 * self.scale / 2)
        for item in self.data:
            colour = self.colour
            left = item["x"] * self.scale
            width = item["width"] * self.scale
            top = item["y"] * self.scale
            height = item["height"] * self.scale

            pix.append(
                Rectangle(
                    start_x + left,
                    width,
                    start_y + top,
                    height,
                    colour,
                )
            )

        return pix
