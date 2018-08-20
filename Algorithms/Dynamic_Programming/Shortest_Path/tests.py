import unittest

from SP import SP, reverse_graph

class test_reverse_graph(unittest.TestCase):

    def test_basic(self):
        graph = {
        'a': [['b', 10]],
        }
        self.assertEqual(reverse_graph(graph), {'b': [['a',10]]})

    def test_basic_1(self):
        graph = {
        'a': [['b', 10]],
        'b': [['c', 5]]
        }
        ans = {
        'b': [['a', 10]],
        'c': [['b', 5]]
        }

        self.assertEqual(reverse_graph(graph), ans)

    def test_basic_2(self):
        graph = {
        'a': [['b', 10], ['c', 8]],
        'b': [['c', 5]]
        }
        ans = {
        'b': [['a', 10]],
        'c': [['a', 8], ['b', 5]]
        }

        self.assertEqual(reverse_graph(graph), ans)

    def test_basic_3(self):
        graph = {
        'a': [['b', 10], ['c', 8]],
        'b': [['c', 5], ['d', 2]]
        }
        ans = {
        'b': [['a', 10]],
        'c': [['a', 8], ['b', 5]],
        'd': [['b', 2]]
        }

        self.assertEqual(reverse_graph(graph), ans)

class test_SP_DP(unittest.TestCase):

    def test_basic(self):
        graph = {
        'a': [['b', 10], ['c', 3]],
        'b': [['c', 1], ['d', 2]],
        'c': [['d', 8], ['e', 2]],
        'e': [['d', 1]]
        }

        self.assertEqual(SP(graph, 'a', 'a'), 0)
        self.assertEqual(SP(graph, 'a', 'b'), 10)
        self.assertEqual(SP(graph, 'a', 'c'), 3)
        self.assertEqual(SP(graph, 'a', 'd'), 6)
        self.assertEqual(SP(graph, 'a', 'e'), 5)

        # self.assertEqual(p['a'], None)
        # self.assertEqual(p['b'], 'c')
        # self.assertEqual(p['c'], 'a')
        # self.assertEqual(p['d'], 'b')
        # self.assertEqual(p['e'], 'c')

    # def test_basic2(self):
    #     graph = {
    #     'a': [['b', 7], ['c', 3]],
    #     'b': [['a', 7], ['c', 1], ['d', 2], ['e', 6]],
    #     'c': [['a', 3], ['b', 1], ['d', 2]],
    #     'd': [['c', 2], ['b', 2], ['e', 4]],
    #     'e': [['b', 6], ['d', 4]]
    #     }
    #
    #     result, p = DJ(graph, 'a')
    #     self.assertEqual(result['a'], 0)
    #     self.assertEqual(result['b'], 4)
    #     self.assertEqual(result['c'], 3)
    #     self.assertEqual(result['d'], 5)
    #     self.assertEqual(result['e'], 9)
    #
    #     self.assertEqual(p['a'], None)
    #     self.assertEqual(p['b'], 'c')
    #     self.assertEqual(p['c'], 'a')
    #     self.assertEqual(p['d'], 'c')
    #     self.assertEqual(p['e'], 'd')

if __name__ == "__main__":
    unittest.main()
