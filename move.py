def move_x(x: float, y: float, z: float, amt: float):
    return x + amt, y, z


def move_y(x: float, y: float, z: float, amt: float):
    return x, y + amt, z


def move_z(x: float, y: float, z: float, amt: float):
    return x, y, z + amt
