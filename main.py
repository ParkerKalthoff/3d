import os
import pygame
import plotline
import time
import rotate
from collections.abc import Callable
import move

# playing around with graphics, probably not the most efficient way to do this stuff

# wsl no sound drivers
os.environ["SDL_AUDIODRIVER"] = ""

pygame.init()

HEIGHT = 600
WIDTH = 800
FPS_CAP = 60

MIN_FRAME_TIME = 1.0 / FPS_CAP

screen = pygame.display.set_mode((WIDTH, HEIGHT))

verticies = [
    (0.01, 0.01, 0.01),
    (0.01, 0.01, 1.01),
    (0.01, 1.01, 0.01),
    (0.01, 1.01, 1.01),
    (1.01, 0.01, 0.01),
    (1.01, 0.01, 1.01),
    (1.01, 1.01, 0.01),
    (1.01, 1.01, 1.01),
]

edges = [
    (0, 1),
    (1, 3),
    (3, 2),
    (2, 0),
    (4, 5),
    (5, 7),
    (7, 6),
    (6, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7),
]


def project(
    x: float, y: float, z: float, width: int, height: int, fov: float, distance: float
):
    factor = fov / (z + distance)
    x = x * factor + width / 2
    y = -y * factor + height / 2
    return int(x), int(y)


def rotate_verts(
    func: Callable[[float, float, float, float], tuple[float, float, float]],
    angle: float,
):
    for i in range(len(verticies)):
        vert = verticies[i]
        x, y, z = func(vert[0], vert[1], vert[2], angle)
        verticies[i] = (x, y, z)


def move_verts(
    func: Callable[[float, float, float, float], tuple[float, float, float]],
    amt: float,
):
    for i in range(len(verticies)):
        vert = verticies[i]
        x, y, z = func(vert[0], vert[1], vert[2], amt)
        verticies[i] = (x, y, z)


def main():

    print(
        "Controls :",
        "\nW / S for forward / backward",
        "\nA / D for left / right",
        "\nKP 8 / KP 5 for up / down",
        "\nX for rotating x coord",
        "\ny for rotating y coord",
        "\nz for rotating z coord",
    )

    frame = 0

    running = True

    while running:
        start = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            move_verts(move.move_x, 0.1)

        if keys[pygame.K_d]:
            move_verts(move.move_x, -0.1)

        if keys[pygame.K_w]:
            move_verts(move.move_z, 0.1)

        if keys[pygame.K_s]:
            move_verts(move.move_z, -0.1)

        if keys[pygame.K_KP8]:
            move_verts(move.move_y, 0.1)

        if keys[pygame.K_KP5]:
            move_verts(move.move_y, -0.1)

        if keys[pygame.K_x]:
            rotate_verts(rotate.rotate_x, 0.03)

        if keys[pygame.K_y]:
            rotate_verts(rotate.rotate_y, 0.03)

        if keys[pygame.K_z]:
            rotate_verts(rotate.rotate_z, 0.03)

        screen.fill((0, 0, 0))

        proj_verts: list[tuple[int, int]] = []

        for vert in verticies:
            px, py = project(vert[0], vert[1], vert[2], WIDTH, HEIGHT, 270, 2)

            screen.set_at((px, py), (255, 255, 255))

            proj_verts.append((px, py))

        for edge in edges:
            x1, y1 = proj_verts[edge[0]][0], proj_verts[edge[0]][1]
            x2, y2 = proj_verts[edge[1]][0], proj_verts[edge[1]][1]

            plotline.plotLine(x1, y1, x2, y2, screen)

        pygame.display.flip()

        FRAME_TIME = time.time() - start
        if FRAME_TIME < MIN_FRAME_TIME:
            time.sleep(MIN_FRAME_TIME - FRAME_TIME)

        frame += 1

    pygame.quit()


if __name__ == "__main__":
    main()
