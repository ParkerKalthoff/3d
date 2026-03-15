from pygame import Surface

# https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm#All_cases


def plotLineLow(x0: int, y0: int, x1: int, y1: int, screen: Surface):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy

    d = (2 * dy) - dx
    y = y0

    for x in range(x0, x1):
        screen.set_at((x, y), (255, 255, 255))
        if d > 0:
            y = y + yi
            d = d + (2 * (dy - dx))
        else:
            d = d + 2 * dy


def plotLineHigh(x0: int, y0: int, x1: int, y1: int, screen: Surface):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx

    d = (2 * dx) - dy
    x = x0

    for y in range(y0, y1):
        screen.set_at((x, y), (255, 255, 255))
        if d > 0:
            x = x + xi
            d = d + (2 * (dx - dy))
        else:
            d = d + 2 * dx


def plotLine(x0: int, y0: int, x1: int, y1: int, screen: Surface):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            plotLineLow(x1, y1, x0, y0, screen)
        else:
            plotLineLow(x0, y0, x1, y1, screen)
    else:
        if y0 > y1:
            plotLineHigh(x1, y1, x0, y0, screen)
        else:
            plotLineHigh(x0, y0, x1, y1, screen)
