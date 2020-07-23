class Grid:
    def __init__(self):
        self.x = -1
        self.y = -1
        self.grid = []

    def add_row(self, row):
        self.grid.append(list(row))

    def check_for_green_neighbours(self, curr_x, curr_y, x=0, y=0):
        if curr_x + x < 0 or curr_y + y < 0 or curr_x + x >= self.x or curr_y + y >= self.y:
            return 0
        if self.grid[curr_x + x][curr_y + y] == '1':
            return 1
        return 0

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
                    green_neighbours = self.check_for_green_neighbours_inner_cells(r, c)
                    if green_neighbours == 3 or green_neighbours == 6:
                        next_gen_row.append('1')
                    else:
                        next_gen_row.append('0')
                else:
                    green_neighbours = self.check_for_green_neighbours_inner_cells(r, c)
                    if green_neighbours == 2 or green_neighbours == 3 or green_neighbours == 6:
                        next_gen_row.append('1')
                    else:
                        next_gen_row.append('0')
            next_generation.append(next_gen_row)
        self.grid = next_generation
