import unittest

class test_fib(unittest.TestCase):

    def test_naive(self):
        from fib import fib as fib

        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)

    def test_dp_2(self):
        from fib import fib_v2 as fib

        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)

    def test_dp_3(self):
        from fib import fib_v3 as fib

        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)

    def test_dp_4(self):
        from fib import fib_v4 as fib

        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)

    def test_dp_5(self):
        from fib import fib_v5 as fib

        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)

if __name__ == "__main__":
    unittest.main()
