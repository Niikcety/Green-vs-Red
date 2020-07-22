from utils.utils import check_if_size_is_correct, check_if_row_size_is_correct, check_if_row_contains_only_valid_chars, check_if_wanted_values_are_valid, check_if_wanted_values_are_in_the_bounds
from grid.grid import Grid


class BaseGrid:
    def __init__(self):
        self.wanted_x = -1
        self.wanted_y = -1
        self.turns = -1
        self.grid = Grid()

    def get_input(self):
        size = input("Enter the size of the grid in format: 'x, y'. ")
        if check_if_size_is_correct(size):
            size_list = size.split(', ')
            self.grid.x = int(size_list[0])
            self.grid.y = int(size_list[1])
        else:
            raise ValueError("Invalid input! Size must be like 'x, y'.")
        for row in range(0, self.grid.x):
            new_row = input('Enter row #{}: '.format(row))
            if check_if_row_size_is_correct(new_row, self.grid.y) and check_if_row_contains_only_valid_chars(new_row):
                self.grid.add_row(new_row)
            else:
                raise ValueError(
                    "Invalid row it should only contain '1' and '0' and must be with length {}".format(self.grid.y))
        wanted = input("Enter the coordinates of the cell and the round in format: 'x, y, round'. ")
        if check_if_wanted_values_are_valid(wanted) and check_if_wanted_values_are_in_the_bounds(wanted, self.grid.x, self.grid.y):
            wanted_list = wanted.split(', ')
            self.wanted_x = int(wanted_list[0])
            self.wanted_y = int(wanted_list[1])
            self.turns = int(wanted_list[2])
        else:
            raise ValueError("Invalid expected input it should be like: 'x, y, turns'.")
