import unittest

from DJ import DJ

class test_Dijkstra(unittest.TestCase):

    def test_basic(self):
        graph = {
        'a': [['b', 10], ['c', 3]],
        'b': [['c', 1], ['d', 2]],
        'c': [['b', 4], ['d', 8], ['e', 2]],
        'd': [['e', 7]],
        'e': [['d', 9]]
        }

        result, p = DJ(graph, 'a')
        self.assertEqual(result['a'], 0)
        self.assertEqual(result['b'], 7)
        self.assertEqual(result['c'], 3)
        self.assertEqual(result['d'], 9)
        self.assertEqual(result['e'], 5)

        self.assertEqual(p['a'], None)
        self.assertEqual(p['b'], 'c')
        self.assertEqual(p['c'], 'a')
        self.assertEqual(p['d'], 'b')
        self.assertEqual(p['e'], 'c')

    def test_basic2(self):
        graph = {
        'a': [['b', 7], ['c', 3]],
        'b': [['a', 7], ['c', 1], ['d', 2], ['e', 6]],
        'c': [['a', 3], ['b', 1], ['d', 2]],
        'd': [['c', 2], ['b', 2], ['e', 4]],
        'e': [['b', 6], ['d', 4]]
        }

        result, p = DJ(graph, 'a')
        self.assertEqual(result['a'], 0)
        self.assertEqual(result['b'], 4)
        self.assertEqual(result['c'], 3)
        self.assertEqual(result['d'], 5)
        self.assertEqual(result['e'], 9)

        self.assertEqual(p['a'], None)
        self.assertEqual(p['b'], 'c')
        self.assertEqual(p['c'], 'a')
        self.assertEqual(p['d'], 'c')
        self.assertEqual(p['e'], 'd')

if __name__ == "__main__":
    unittest.main()
