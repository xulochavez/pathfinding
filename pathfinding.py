from collections import deque


class Grid(object):
    def __init__(self, grid_points):
        self._grid = grid_points

    def is_reachable(self, position):
        if position.row < 0 or position.col < 0:
            return False
        try:
            return self._grid[position.row][position.col] == 0
        except IndexError:
            return False


class Position(object):
    def __init__(self, row, col):
        self.row, self.col = row, col

    def __repr__(self):
        return "({0.row}, {0.col})".format(self)

    def surrounding_positions(self):
        for row_move, col_move in [(-1,0), (0,1), (1,0), (0,-1)]:
            yield Position(self.row + row_move, self.col + col_move)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


def find_shortest_path(grid, starting_position, end_position):
    found = []
    paths_to_check = deque([[starting_position],])
    current_posn = starting_position
    while paths_to_check:
        path = paths_to_check.popleft()
        for posn in path[-1].surrounding_positions():
            if posn == end_position:
                found.append(path+[posn])
            elif posn not in path and grid.is_reachable(posn):
                paths_to_check.append(path[:] + [posn])
    return sorted(found, key=len)[0]

def find_shortest_path_recursive(grid, path, end_position):
    branches = []
    for posn in path[-1].surrounding_positions():
        if posn == end_position:
            branches.append(path + [posn])
        elif posn not in path and grid.is_reachable(posn):
            branches.extend(find_shortest_path_recursive(grid, path + [posn], end_position))
    if branches:
        return sorted(branches, key=len)[0]
    else:
        return []





