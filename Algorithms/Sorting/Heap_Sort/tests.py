import unittest, random

from HSort import h_sort

class test_HSort(unittest.TestCase):

    def test_init(self):
        self.assertEqual(h_sort([]), None)

    def test_basic(self):
        # self.assertEqual(h_sort([9,5,8,1,7,4,3,2,6]), [1,2,3,4,5,6,7,8,9])

        arr = [random.randint(0, 1000) for x in range(10**5)]
        self.assertEqual(h_sort(arr), sorted(arr))
    # def test_random(self):
    #
    #     for i in range(10**2):
    #         arr = [random.randint(0, 1000) for x in range(10**2)]
    #         self.assertEqual(h_sort(arr), sorted(arr))

if __name__ == "__main__":
    unittest.main()
