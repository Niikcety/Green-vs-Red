class Grid:
    def __init__(self):
        self.x = -1
        self.y = -1
        self.grid = []

    def add_row(self, row):
        row_list = list(row)
        self.grid.append(row_list)

    def check_for_green_neighbours(self, curr_x, curr_y, x=0, y=0):
        try:
            if self.grid[curr_x + x][curr_y + y] == '1':
                return 1
        except IndexError:
            return 0

    def check_for_green_neighbours_corner_cells(self, curr_x, curr_y):
        # check on (0, 0), (0, y - 1), (x -1 , 0), (x - 1, y - 1)
        # needs testing
        green_number = 0
        if curr_x == 0 and curr_y == 0:
            green_number += self.check_for_green_neighbours(curr_x, curr_y, y=1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1, y=1)
        elif curr_x == 0 and curr_y == self.y - 1:
            green_number += self.check_for_green_neighbours(curr_x, curr_y, y=-1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1, y=-1)
        elif curr_x == self.x - 1 and curr_y == 0:
            green_number += self.check_for_green_neighbours(curr_x, curr_y, y=1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1, y=1)
        else:
            green_number += self.check_for_green_neighbours(curr_x, curr_y, y=-1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1, y=-1)
        return green_number

    def check_for_green_neighbours_bound_line_cells(self, curr_x, curr_y):
        # check on (0, y), (x, 0), (x - 1, y), (x, y - 1)
        green_number = 0
        if curr_x == 0:
            green_number += self.check_for_green_neighbours(curr_x, curr_y, y=1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, y=-1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1, y=-1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1, y=1)
        elif curr_x == self.x - 1:
            green_number += self.check_for_green_neighbours(curr_x, curr_y, y=1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, y=-1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1, y=1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1, y=1)
        elif curr_y == 0:
            green_number += self.check_for_green_neighbours(curr_x, curr_y, y=1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1, y=1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1, y=1)
        else:
            green_number += self.check_for_green_neighbours(curr_x, curr_y, y=-1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1, y=-1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1)
            green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1, y=-1)
        return green_number

    def check_for_green_neighbours_inner_cells(self, curr_x, curr_y):
        green_number = 0
        green_number += self.check_for_green_neighbours(curr_x, curr_y, y=-1)
        green_number += self.check_for_green_neighbours(curr_x, curr_y, y=1)
        green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1, y=-1)
        green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1)
        green_number += self.check_for_green_neighbours(curr_x, curr_y, x=-1, y=1)
        green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1, y=-1)
        green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1)
        green_number += self.check_for_green_neighbours(curr_x, curr_y, x=1, y=1)
        return green_number

    def create_next_generation(self):
        next_generation = []
        for r in range(0, self.x):
            next_gen_row = []
            for c in range(0, self.y):
                if self.grid[r][c] == '0':
                    if (r == 0 and (c == self.y - 1 or c == 0)) or (r == self.x - 1 and (c == self.y - 1 or c == 0)):
                        green_neighbours = self.check_for_green_neighbours_corner_cells(r, c)
                    elif c == 0 or c == self.y - 1 or r == 0 or r == self.x - 1:
                        green_neighbours = self.check_for_green_neighbours_bound_line_cells(r, c)
                    else:
                        green_neighbours = self.check_for_green_neighbours_inner_cells(r, c)
                    if green_neighbours == 3 or green_neighbours == 6:
                        next_gen_row.append('1')
                    else:
                        next_gen_row.append('0')
                else:
                    if (r == 0 and (c == self.y - 1 or c == 0)) or (r == self.x - 1 and (c == self.y - 1 or c == 0)):
                        green_neighbours = self.check_for_green_neighbours_corner_cells(r, c)
                    elif c == 0 or c == self.y - 1 or r == 0 or r == self.x - 1:
                        green_neighbours = self.check_for_green_neighbours_bound_line_cells(r, c)
                    else:
                        green_neighbours = self.check_for_green_neighbours_inner_cells(r, c)
                    if green_neighbours == 2 or green_neighbours == 3 or green_neighbours == 6:
                        next_gen_row.append('1')
                    else:
                        next_gen_row.append('0')
            next_generation.append(next_gen_row)
        self.grid = next_generation
