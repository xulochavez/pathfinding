import unittest
from pathfinding import Position, Grid, find_shortest_path, find_shortest_path_recursive

# TESTS
class TestPosition(unittest.TestCase):

    def test_surounding_positions(self):
        posn = Position(1,1)
        expected = [Position(0,1),Position(1,2), Position(2,1),Position(1,0)]
        actual = list(posn.surrounding_positions())
        self.assertEquals(expected, actual)


class TestGrid(unittest.TestCase):

    def test_reachable(self):
        grid = Grid([[0,0,0,1],
                    [0,1,1,1],
                    [0,0,0,0],
                    [0,0,1,0]])
        self.assertFalse(grid.is_reachable(Position(0, -1)))
        self.assertFalse(grid.is_reachable(Position(-1, -1)))
        self.assertTrue(grid.is_reachable(Position(0, 2)))


class TestFindPath(unittest.TestCase):

    def test_simple_grid(self):

        grid = Grid([[0,0,0,1],
                    [0,1,1,1],
                    [0,0,0,0],
                    [0,0,1,0]])

        expected = [Position(0,0), Position(1,0), Position(2,0), Position(2,1), Position(2,2), Position(2,3), Position(3,3)]

        actual = find_shortest_path(grid, Position(0,0), Position(3,3))

        self.assertEquals(expected, actual)

    def test_recursive(self):

        grid = Grid([[0,0,0,1],
                    [0,1,1,1],
                    [0,0,0,0],
                    [0,0,1,0]])

        expected = [Position(0,0), Position(1,0), Position(2,0), Position(2,1), Position(2,2), Position(2,3), Position(3,3)]

        actual = find_shortest_path_recursive(grid, [Position(0,0)], Position(3,3))[0]

        self.assertEquals(expected, actual)