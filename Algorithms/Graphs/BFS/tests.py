import unittest

from BFS import BFS

class test_BFS(unittest.TestCase):

    def test_basic(self):
        graph = {
        'a': ['z', 's'],
        'z': ['a'],
        's': ['a', 'x'],
        'x': ['s', 'd', 'c'],
        'd': ['x', 'c', 'f'],
        'c': ['x', 'v', 'd', 'f'],
        'f': ['d', 'c', 'v'],
        'v': ['c', 'f']
        }

        levels, parent = BFS('s', graph)

        self.assertEqual(levels['s'], 0)
        self.assertEqual(levels['a'], 1)
        self.assertEqual(levels['x'], 1)
        self.assertEqual(levels['z'], 2)
        self.assertEqual(levels['d'], 2)
        self.assertEqual(levels['c'], 2)
        self.assertEqual(levels['f'], 3)
        self.assertEqual(levels['v'], 3)

        self.assertEqual(parent['s'], None)
        self.assertEqual(parent['a'], 's')
        self.assertEqual(parent['x'], 's')
        self.assertEqual(parent['z'], 'a')
        self.assertEqual(parent['d'], 'x')
        self.assertEqual(parent['c'], 'x')
        self.assertEqual(parent['f'], 'd')
        self.assertEqual(parent['v'], 'c')



if __name__ == "__main__":
    unittest.main()
