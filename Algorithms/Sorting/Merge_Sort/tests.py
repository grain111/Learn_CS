import unittest, random

from MSort import m_sort

class test_InsSort(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(m_sort([]), None)

    def test_sort(self):
        self.assertEqual(m_sort([5,4,2,1,3,6]), [1,2,3,4,5,6])

    def test_big(self):
        for y in range(1000):
            lst = [random.randint(0,500) for x in range(10**2)]
            self.assertEqual(m_sort(lst), sorted(lst))


if __name__ == "__main__":
    unittest.main()
