def check_if_size_is_correct(size):
    size_list = size.split(', ')
    x = int(size_list[0])
    y = int(size_list[1])
    if x < 0 or y < 0 or x > y:
        return False
    else:
        return True


def check_if_row_size_is_correct(row, size):
    if len(row) == size:
        return True
    else:
        return False


def check_if_row_contains_only_valid_chars(row):
    for char in row:
        if char != '1' and char != '0':
            return False
    return True


def check_if_wanted_values_are_valid(wanted):
    wanted_list = wanted.split(', ')
    wanted_x = wanted_list[0]
    wanted_y = wanted_list[1]
    wanted_turns = wanted_list[2]
    if wanted_x < 0 or wanted_y < 0 or wanted_turns < 0:
        return False
    else:
        return True
