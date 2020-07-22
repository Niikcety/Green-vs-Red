from utils.utils import check_if_size_is_correct, check_if_row_size_is_correct, check_if_row_contains_only_valid_chars,
    check_if_wanted_values_are_valid


class BaseGrid:
    def __init__(self):
        self.x = -1
        self.y = -1
        self.wanted_x = -1
        self.wanted_y = -1
        self.turns = -1

    def get_input(self):
        size = input()
        if check_if_size_is_correct(size):
            size_list = size.split(', ')
            self.x = size_list[0]
            self.y = size_list[1]
        else:
            raise ValueError("Invalid input! Size must be like 'x, y'")
        for row in range(0, self.x):
            new_row = input('Enter row #{}'.format(row))
            if check_if_row_size_is_correct(new_row) and check_if_row_contains_only_valid_chars(new_row):
                # should append it to the grid
                pass
            else:
                raise ValueError(
                    "Invalid row it should only contain '1' and '0' and must be with length {}".format(self.y))
        wanted = input()
        if check_if_wanted_values_are_valid(wanted):
            wanted_list = wanted.split(', ')
            self.wanted_x = wanted_list[0]
            self.wanted_y = wanted_list[1]
            self.turns = wanted_list[2]
        else:
            raise ValueError("Invalid expected input it should be like: 'x, y, turns'.")
