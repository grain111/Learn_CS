import unittest

from BST import BST

class test_BST(unittest.TestCase):

    def test_basic(self):
        bin = BST()
        bin.insert(5)
        self.assertEqual(bin.root.val, 5)

        bin.insert(6)
        self.assertEqual(bin.root.right.val, 6)

    def test_search(self):
        bin = BST()
        for i in range(50):
            bin.insert(i)

        self.assertEqual(bin.find(8), 8)
        self.assertEqual(bin.find(49), 49)
        self.assertEqual(bin.find(60), None)

    def test_next(self):
        bin = BST()
        bin.insert(7)
        bin.insert(3)
        bin.insert(8)
        bin.insert(1)
        bin.insert(5)
        bin.insert(2)
        bin.insert(4)
        bin.insert(6)
        bin.insert(10)
        bin.insert(9)
        bin.insert(20)
        bin.insert(11)
        bin.insert(12)

        node1 = bin.next(bin.root)
        node2 = bin.next(node1)
        node3 = bin.next(node2)
        node4 = bin.next(node3)
        node5 = bin.next(node4)
        node6 = bin.next(node5)

        self.assertEqual(node1.val, 8)
        self.assertEqual(node2.val, 9)
        self.assertEqual(node3.val, 10)
        self.assertEqual(node4.val, 11)
        self.assertEqual(node5.val, 12)
        self.assertEqual(node6.val, 20)
        self.assertEqual(bin.next(node6), None)

    def test_sorted(self):
        bin = BST()
        bin.insert(7)
        bin.insert(3)
        bin.insert(8)
        bin.insert(1)
        bin.insert(5)
        bin.insert(2)
        bin.insert(4)
        bin.insert(6)
        bin.insert(10)
        bin.insert(9)
        bin.insert(20)
        bin.insert(11)
        bin.insert(12)

        self.assertEqual(bin.sorted(), [1,2,3,4,5,6,7,8,9,10,11,12,20])



if __name__ == "__main__":
    unittest.main()
