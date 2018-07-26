import unittest, random

from InsSort import i_sort

class test_InsSort(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(i_sort([]), None)

    def test_sort(self):
        self.assertEqual(i_sort([5,4,2,1,3]), [1,2,3,4,5])

    def test_big(self):
        lst = [random.randint(0,500) for x in range(10**3)]
        self.assertEqual(i_sort(lst), sorted(lst))


if __name__ == "__main__":
    unittest.main()
