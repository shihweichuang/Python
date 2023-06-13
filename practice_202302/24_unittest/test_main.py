import unittest
from main import calc

class TestCalcMethod(unittest.TestCase):

    def test_calc(self):
        predict = calc(1, 2)

        self.assertEqual(predict, 3)

if __name__ == "__main__":
    unittest.main()