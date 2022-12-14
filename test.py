import unittest
from Fibonachi import Fibonachi

class fibonachi(unittest.TestCase):
    def test_fibonachi_5(self):
        expected_res = [0, 1, 1, 2, 3]
        res = [i for i in Fibonachi(5)]
        self.assertEqual(res, expected_res)
    def test_fibonachi_10(self):
        expected_res = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        res = [i for i in Fibonachi(10)]
        self.assertEqual(res, expected_res)
    def test_fibonachi_0(self):
        expected_res = []
        res = [i for i in Fibonachi(0)]
        self.assertEqual(res, expected_res)

if __name__ == '__main__':
    unittest.main()
