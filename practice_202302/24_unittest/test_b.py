import unittest
from b import calc_b

class TestCalcMethod(unittest.TestCase):

    def test_calc_b(self):
        predict = calc_b(1, 2)

        self.assertEqual(predict, 2)

if __name__ == "__main__":
    unittest.main()