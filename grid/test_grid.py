import unittest
from grid import Grid


class TestGrid(unittest.TestCase):
    def test_add_row_should_append_to_grid_property(self):
        grid = Grid()
        grid.add_row(['1', '0', '1'])
        grid.add_row(['0', '1', '0'])

        self.assertEquals(grid.grid, [['1', '0', '1'], ['0', '1', '0']])

    def test_check_for_green_neighbours_inner_cell_should_return_the_amount_of_green_cells(self):
        grid = Grid()
        grid.x, grid.y = 3, 3
        grid.add_row(['1', '1', '1'])
        grid.add_row(['1', '1', '1'])
        grid.add_row(['1', '1', '1'])

        # testing in the corner cell should return 3
        self.assertEquals(grid.check_for_green_neighbours_inner_cells(0, 0), 3)
        self.assertEquals(grid.check_for_green_neighbours_inner_cells(0, 2), 3)
        self.assertEquals(grid.check_for_green_neighbours_inner_cells(2, 0), 3)
        self.assertEquals(grid.check_for_green_neighbours_inner_cells(2, 2), 3)
        # testing in the bound line
        self.assertEquals(grid.check_for_green_neighbours_inner_cells(1, 0), 5)
        self.assertEquals(grid.check_for_green_neighbours_inner_cells(0, 1), 5)
        self.assertEquals(grid.check_for_green_neighbours_inner_cells(1, 2), 5)
        self.assertEquals(grid.check_for_green_neighbours_inner_cells(2, 1), 5)
        # testing in the middle
        self.assertEquals(grid.check_for_green_neighbours_inner_cells(1, 1), 8)

    def test_create_next_generation(self):
        grid = Grid()
        grid.x, grid.y = 3, 3
        grid.add_row(['1', '0', '1'])
        grid.add_row(['0', '1', '0'])
        grid.add_row(['0', '0', '1'])

        """
            1 0 1                  0 1 0
            0 1 0 Should become -> 0 1 1
            0 0 1                  0 0 0
        """

        grid.create_next_generation()

        self.assertEquals(grid.grid, [['0', '1', '0'], ['0', '1', '1'], ['0', '0', '0']])

        """
            0 1 0                  0 1 1
            0 1 1 Should become -> 0 1 1
            0 0 0                  0 0 0
        """

        grid.create_next_generation()

        self.assertEquals(grid.grid, [['0', '1', '1'], ['0', '1', '1'], ['0', '0', '0']])


if __name__ == '__main__':
    unittest.main()
