import math


def rotate_x(x: float, y: float, z: float, angle: float):
    cos = math.cos(angle)
    sin = math.sin(angle)

    y2 = y * cos - z * sin
    z2 = y * sin + z * cos

    return x, y2, z2


def rotate_y(x: float, y: float, z: float, angle: float):
    cos = math.cos(angle)
    sin = math.sin(angle)

    x2 = x * cos + z * sin
    z2 = -x * sin + z * cos

    return x2, y, z2


def rotate_z(x: float, y: float, z: float, angle: float):
    cos = math.cos(angle)
    sin = math.sin(angle)

    x2 = x * cos - y * sin
    y2 = x * sin + y * cos

    return x2, y2, z
