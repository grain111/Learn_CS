import unittest, random

from RSort import r_sort, c_sort

class test_counting(unittest.TestCase):

    def test_basic(self):
        arr = [9,8,7,6,5,4,3,2,1,0]
        self.assertEqual(c_sort(arr, 10, lambda x: x), [0,1,2,3,4,5,6,7,8,9])

    def test_random(self):
        for x in range(100):
            arr = [random.randint(0,1000) for n in range(10**2)]
            self.assertEqual(c_sort(arr, 1000, lambda x: x), sorted(arr))

class test_radix(unittest.TestCase):

    def test_basic(self):
        arr = [9,8,7,6,5,4,3,2,1,0]
        self.assertEqual(r_sort(arr), [0,1,2,3,4,5,6,7,8,9])

    def test_random(self):
        for x in range(100):
            arr = [random.randint(0,1000) for n in range(10**2)]
            self.assertEqual(r_sort(arr), sorted(arr))


if __name__ == "__main__":
    unittest.main()
