from math import cos, radians, sin

from .conf import font


class Character:
    """A character."""

    def __init__(self, char, scale, offset, angle, colour, opacity=1):  # noqa: PLR0913
        """Construct."""
        self.char = char
        self.scale = scale
        self.offset = offset
        self.angle = angle
        self.colour = list(colour) + [opacity]

        self.data = font[char]

    def draw(self, ctx):
        """Draw."""
        ctx.rgba(*self.colour)

        ctx.translate(
            sin(radians(self.angle)) * -self.offset,
            cos(radians(self.angle)) * self.offset,
        )
        print(
            sin(radians(self.angle)) * -self.offset,
            cos(radians(self.angle)) * self.offset,
        )
        ctx.rotate(radians(self.angle))

        start_x = 0 - (8 * self.scale / 2)
        start_y = 0 - (8 * self.scale / 2)
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
