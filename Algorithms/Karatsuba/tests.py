import unittest, random
import time

from KSuba import simple_mul, kar_mul

class test_simple_mul(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(simple_mul(5874, 3213), 18873162)
        self.assertEqual(simple_mul(123456789, 2), 246913578)
        self.assertEqual(simple_mul(2, 123456789), 246913578)
        self.assertEqual(simple_mul(2, 2), 4)

    def test_big(self):
        for j in range(10**2):
            a = random.randint(0, 10**10)
            b = random.randint(0, 10**10)
            self.assertEqual(simple_mul(a, b), a * b)

class test_kar_mul(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(kar_mul(5874, 3213), 18873162)
        self.assertEqual(kar_mul(123456789, 2), 246913578)
        self.assertEqual(kar_mul(2, 123456789), 246913578)
        self.assertEqual(kar_mul(2, 2), 4)

    def test_big(self):
        for j in range(10**2):
            a = random.randint(0, 10**10)
            b = random.randint(0, 10**10)
            self.assertEqual(kar_mul(a, b), a * b)

if __name__ == "__main__":
    unittest.main()
