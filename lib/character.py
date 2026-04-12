from .conf import font

# from .rectangle import Rectangle


class Character:
    """A character."""

    def __init__(self, char, x, y, scale, colour, opacity=1):  # noqa: PLR0913
        """Construct."""
        self.char = char
        self.x = x
        self.y = y
        self.scale = scale
        self.colour = list(colour) + [opacity]

        self.data = font[char]


    def draw(self, ctx):
        """Draw."""
        ctx.rgba(*self.colour)

        start_x = self.x - (8 * self.scale / 2)
        start_y = self.y - (8 * self.scale / 2)
        for item in self.data:
            left = item["x"] * self.scale
            width = item["width"] * self.scale
            top = item["y"] * self.scale
            height = item["height"] * self.scale

            ctx.rectangle(
                start_x + left,
                start_y + top,
                width,
                height,
            )

            ctx.fill()
