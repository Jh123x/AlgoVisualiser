from queue import PriorityQueue, Queue
from math import sqrt
from visualiser.visualiser import Animate
from visualiser.Animation.Blocks.Grid import Grid


def Astar(source: tuple, target: tuple, visited: Grid):
    """Astar"""
    arr = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    )

    stack = PriorityQueue()
    stack.put((0,) + source)

    while not stack.empty():
        _, x, y = stack.get()
        curr = (x, y)

        if not visited.in_range(*curr) or visited.is_blocked(*curr):
            continue

        if (x, y) == target:
            break

        for x, y in arr:
            x_coord = curr[0] + x
            y_coord = curr[1] + y
            euclid_dist_from_end = sqrt(
                (x_coord - target[0]) ** 2 + (y_coord - target[1]) ** 2)
            euclid_dist_from_start = sqrt(
                (x_coord - source[0]) ** 2 + (y_coord - source[1]) ** 2)
            euclid_dist = euclid_dist_from_end + euclid_dist_from_start
            stack.put((euclid_dist, x_coord, y_coord))

        if source != curr:
            visited.mark_visited(*curr)

        yield curr

    yield target


def bfs(source: tuple, target: tuple, visited: Grid):
    """BFS"""
    arr = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    )

    stack = Queue()
    stack.put((0,) + source)

    while not stack.empty():
        _, x, y = stack.get()
        curr = (x, y)

        if not visited.in_range(*curr) or visited.is_blocked(*curr):
            continue

        if (x, y) == target:
            break

        for x, y in arr:
            x_coord = curr[0] + x
            y_coord = curr[1] + y
            euclid_dist = sqrt(
                (x_coord - target[0]) ** 2 + (y_coord - target[1]) ** 2)
            stack.put((euclid_dist, x_coord, y_coord))

        if source != curr:
            visited.mark_visited(*curr)

        yield curr

    yield target


def dfs(source: tuple, target: tuple, visited: Grid):
    """DFS"""
    arr = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    )

    stack = [source]

    while len(stack):
        x, y = stack.pop()
        curr = (x, y)

        if not visited.in_range(*curr) or visited.is_blocked(*curr):
            continue

        if (x, y) == target:
            break

        for x, y in arr:
            x_coord = curr[0] + x
            y_coord = curr[1] + y
            stack.append((x_coord, y_coord))

        if source != curr:
            visited.mark_visited(*curr)

        yield curr

    yield target


if __name__ == '__main__':

    # Run the visualisation
    # game = Animate(Astar, ((0, 0), (80, 75)), dim = (100, 100), resolution= (1080,1080), fps =144)
    # game = Animate(bfs, ((0, 0), (80, 75)), dim=(100, 100), resolution=(1080, 1080), fps=144)
    game = Animate(dfs, ((0, 0), (80, 75)), dim=(100, 100), resolution=(1080, 1080), fps=144)
    game.run()
