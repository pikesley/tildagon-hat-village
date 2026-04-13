def assign_angles(length, angle):
    """Assign spread of angles."""
    start_angle = angle * ((length - 1) / 2)

    return [start_angle - (i * angle) for i in range(length)]


def assign_offsets(length, scale):
    """Assign offsets."""
    raw = [scale * i * 8 for i in range(length)]
    return [x - (scale * 8 * ((length - 1) / 2)) for x in raw]
