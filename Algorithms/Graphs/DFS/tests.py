import unittest

from DFS import DFS

class test_DFS(unittest.TestCase):

    def test_basic(self):
        graph = {
        'a': ['b', 'd'],
        'b': ['e'],
        'c': ['e', 'f'],
        'd': ['b'],
        'e': ['d'],
        'f': ['f']
        }

        ans, te, be, fe, ce = DFS(graph)
        for key in graph:
            self.assertEqual(key in ans, True)

        self.assertEqual(te, ['ab', 'be', 'ed', 'cf'])
        self.assertEqual(be, ['db'])
        self.assertEqual(fe, ['ad'])
        self.assertEqual(ce, ['ce'])

    def test_basic2(self):
        graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d'],
        'd': ['e', 'g'],
        'e': ['f', 'g'],
        'f': ['b'],
        'g': []
        }

        ans, te, be, fe, ce = DFS(graph)
        for key in graph:
            self.assertEqual(key in ans, True)

        self.assertEqual(te, ['ab', 'bd', 'de', 'ef', 'eg', 'ac'])
        self.assertEqual(be, ['fb'])
        self.assertEqual(fe, ['dg'])
        self.assertEqual(ce, ['cd'])

if __name__ == "__main__":
    unittest.main()
