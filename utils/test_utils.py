import unittest
from utils import check_if_size_is_correct, check_if_row_size_is_correct, check_if_row_contains_only_valid_chars, \
    check_if_wanted_values_are_valid, check_if_wanted_values_are_in_the_bounds


class TestCheckIfSizeIsCorrect(unittest.TestCase):
    def test_with_invalid_input_should_return_false(self):
        size1 = '-1, 1'
        size2 = '1, -1'
        size3 = '4, 3'
        size4 = '0, 1'
        size5 = '1, 0'

        self.assertFalse(check_if_size_is_correct(size1))
        self.assertFalse(check_if_size_is_correct(size2))
        self.assertFalse(check_if_size_is_correct(size3))
        self.assertFalse(check_if_size_is_correct(size4))
        self.assertFalse(check_if_size_is_correct(size5))

    def test_with_valid_input_should_return_True(self):
        size = '5, 5'

        self.assertTrue(check_if_size_is_correct(size))

    def test_with_size_that_is_not_digits_should_return_false(self):
        size1 = 'five, six'
        size2 = 'ab'
        size3 = '3:4:a'

        self.assertFalse(check_if_size_is_correct(size1))
        self.assertFalse(check_if_size_is_correct(size2))
        self.assertFalse(check_if_size_is_correct(size3))


class TestCheckIfRowSizeIsCorrect(unittest.TestCase):
    def test_with_valid_input_should_return_true(self):
        row = '10001'
        size = 5

        self.assertTrue(check_if_row_size_is_correct(row, size))

    def test_with_invalid_input_should_return_false(self):
        row = '10001'
        size = 4

        self.assertFalse(check_if_row_size_is_correct(row, size))


class TestCheckIfRowContainsOnlyValidChars(unittest.TestCase):
    def test_with_invalid_input_should_return_false(self):
        row = '123'

        self.assertFalse(check_if_row_contains_only_valid_chars(row))

    def test_with_valid_input_should_return_true(self):
        row = '10001'

        self.assertTrue(check_if_row_contains_only_valid_chars(row))


class TestCheckIfWantedValuesAreValid(unittest.TestCase):
    def test_with_invalid_input_should_return_false(self):
        wanted1 = '-1, 0, 50'
        wanted2 = '0, -1, 50'
        wanted3 = '0, 0, -30'

        self.assertFalse(check_if_wanted_values_are_valid(wanted1))
        self.assertFalse(check_if_wanted_values_are_valid(wanted2))
        self.assertFalse(check_if_wanted_values_are_valid(wanted3))

    def test_with_incorrect_written_input_should_return_false(self):
        wanted1 = 'fifty, five, zero'
        wanted2 = '1,2,3,4,5'
        wanted3 = '1, 2'
        wanted4 = '1,2,50'

        self.assertFalse(check_if_wanted_values_are_valid(wanted1))
        self.assertFalse(check_if_wanted_values_are_valid(wanted2))
        self.assertFalse(check_if_wanted_values_are_valid(wanted3))
        self.assertFalse(check_if_wanted_values_are_valid(wanted4))

    def test_with_valid_input_should_return_true(self):
        wanted1 = '0, 0, 50'
        wanted2 = '1, 1, 30'

        self.assertTrue(check_if_wanted_values_are_valid(wanted1))
        self.assertTrue(check_if_wanted_values_are_valid(wanted2))


class TestCheckIfWantedValuesAreInTheBounds(unittest.TestCase):
    def test_with_wanted_in_bound_should_return_true(self):
        wanted1, x1, y1 = '1, 2, 3', 3, 3
        wanted2, x2, y2 = '1, 1, 3', 2, 2

        self.assertTrue(check_if_wanted_values_are_in_the_bounds(wanted1, x1, y1))
        self.assertTrue(check_if_wanted_values_are_in_the_bounds(wanted2, x2, y2))

    def test_with_wanted_outside_the_bound_should_return_false(self):
        wanted1, x1, y1 = '1, 1, 3', 1, 1
        wanted2, x2, y2 = '1, 3, 3', 2, 2

        self.assertFalse(check_if_wanted_values_are_in_the_bounds(wanted1, x1, y1))
        self.assertFalse(check_if_wanted_values_are_in_the_bounds(wanted2, x2, y2))


if __name__ == '__main__':
    unittest.main()
