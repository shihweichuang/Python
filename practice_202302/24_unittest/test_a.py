import unittest
from a import calc_a

class TestCalcMethod(unittest.TestCase):

    def test_calc_a(self):
        predict = calc_a(1, 2)

        self.assertEqual(predict, -1)

if __name__ == "__main__":
    unittest.main()