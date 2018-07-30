import unittest, random

from RK import find_string

class test_RK(unittest.TestCase):

    def test_basic(self):
        text = "abcde"
        string = 'cde'

        self.assertEqual(find_string(string, text), string in text)

    def test_beg(self):
        text = "abcdefghijkl"
        string = 'abc'

        self.assertEqual(find_string(string, text), string in text)

    def test_mid(self):
        text = "abcdefghijkl"
        string = 'efg'

        self.assertEqual(find_string(string, text), string in text)

    def test_end(self):
        text = "abcdefghijkl"
        string = 'jkl'

        self.assertEqual(find_string(string, text), string in text)

    def test_all(self):
        text = "abcdefghijkl"
        string = 'abcdefghijkl'

        self.assertEqual(find_string(string, text), string in text)

    def test_none(self):
        text = "abcdefghijkl"
        string = 'mn'

        self.assertEqual(find_string(string, text), string in text)


    def test_random(self):
        for i in range(10**1):
            text = ''
            for i in range(10**4):
                text += chr(random.randint(97,122))
            string = 'cde'

            self.assertEqual(find_string(string, text), string in text)

if __name__ == "__main__":
    unittest.main()
