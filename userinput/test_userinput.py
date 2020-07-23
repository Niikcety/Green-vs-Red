import unittest
from userinput import UserInput


class TestUserInput(unittest.TestCase):
    def test_set_size_with_invalid_size_should_raise_value_error(self):
        user_input = UserInput()
        exc = None
        size = '3,3'

        try:
            user_input.set_size(size)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEquals(str(exc), "Invalid input! Size must be like 'x, y'.")

    def test_set_size_with_valid_size_should_set_grid_properties(self):
        user_input = UserInput()
        size = '3, 4'

        user_input.set_size(size)

        self.assertEquals(user_input.grid.x, 3)
        self.assertEquals(user_input.grid.y, 4)

    def test_set_wanted_with_invalid_wanted_should_raise_value_error(self):
        user_input = UserInput()
        exc = None
        wanted = '3,3,50'

        try:
            user_input.set_wanted(wanted)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEquals(str(exc), "Invalid expected input it should be like: 'x, y, turns'.")

    def test_set_wanted_with_out_of_bounds_should_raise_value_error(self):
        user_input = UserInput()
        user_input.grid.x = 2
        user_input.grid.y = 2
        wanted = '2, 2, 50'
        exc = None

        try:
            user_input.set_wanted(wanted)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEquals(str(exc), "Invalid expected input it should be like: 'x, y, turns'.")

    def test_set_wanted_with_valid_input_should_set_userinput_properties(self):
        user_input = UserInput()
        user_input.set_size('4, 4')
        wanted = '2, 3, 30'

        user_input.set_wanted(wanted)

        self.assertEquals(user_input.wanted_x, 2)
        self.assertEquals(user_input.wanted_y, 3)
        self.assertEquals(user_input.turns, 30)


if __name__ == '__main__':
    unittest.main()

