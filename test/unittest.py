import unittest
from src.loops_n_linq import add, is_even


class TestEm(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(is_even(2)) # python ... totally consistent ...

    def test_add(self):
        self.assertEqual(add(10, 20), 30)


if __name__ == '__main__':
    unittest.main()