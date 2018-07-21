import unittest

from SLL import SLL, Node

class Test_SLL(unittest.TestCase):

    def test_print(self):
        """
        Test print statment
        """
        lst = SLL()
        lst.head = Node(5)
        lst.head.pointer = Node(6)
        lst.head.pointer.pointer = Node(8)

        self.assertEqual(lst.__str__(), '[5, 6, 8]')

    def test_pushfront(self):
        """
        Test push front
        """
        lst = SLL()
        self.assertEqual(lst.__str__(), '[]')
        lst.push_front(5)
        lst.push_front(15)
        lst.push_front(25)
        self.assertEqual(lst.__str__(), '[25, 15, 5]')

    def test_pushback(self):
        """
        Test push back
        """
        lst = SLL()
        self.assertEqual(lst.__str__(), '[]')
        lst.push_back(5)
        lst.push_back(15)
        lst.push_back(25)
        self.assertEqual(lst.__str__(), '[5, 15, 25]')

    def test_insert(self):
        """
        Test inserting a key
        """
        # Inserting front with non empty list
        lst = SLL()
        self.assertEqual(lst.__str__(), '[]')
        lst.push_back(5)
        lst.push_back(15)
        lst.push_back(25)
        lst.insert(0, 18)
        self.assertEqual(lst.__str__(), '[18, 5, 15, 25]')

        # Inserting front with empty list
        lst = SLL()
        self.assertEqual(lst.__str__(), '[]')
        lst.insert(0, 18)
        self.assertEqual(lst.__str__(), '[18]')

        # Inserting middle with non empty list
        lst = SLL()
        self.assertEqual(lst.__str__(), '[]')
        lst.push_back(5)
        lst.push_back(15)
        lst.push_back(25)
        lst.insert(1, 18)
        self.assertEqual(lst.__str__(), '[5, 18, 15, 25]')

        # Inserting middle with non empty list
        lst = SLL()
        self.assertEqual(lst.__str__(), '[]')
        lst.push_back(5)
        lst.push_back(15)
        lst.push_back(25)
        lst.insert(2, 18)
        self.assertEqual(lst.__str__(), '[5, 15, 18, 25]')

        # Inserting end with non empty list
        lst = SLL()
        self.assertEqual(lst.__str__(), '[]')
        lst.push_back(5)
        lst.push_back(15)
        lst.push_back(25)
        lst.insert(3, 18)
        self.assertEqual(lst.__str__(), '[5, 15, 25, 18]')

    def test_erase(self):
        """
        Test inserting a key
        """
        # Erasing front with non empty list
        lst = SLL()
        self.assertEqual(lst.__str__(), '[]')
        lst.push_back(5)
        lst.push_back(15)
        lst.push_back(25)
        lst.erase(0)
        self.assertEqual(lst.__str__(), '[15, 25]')

        # Erasing middle with non empty list
        lst = SLL()
        self.assertEqual(lst.__str__(), '[]')
        lst.push_back(5)
        lst.push_back(15)
        lst.push_back(25)
        lst.erase(1)
        self.assertEqual(lst.__str__(), '[5, 25]')

        # Erasing end with non empty list
        lst = SLL()
        self.assertEqual(lst.__str__(), '[]')
        lst.push_back(5)
        lst.push_back(15)
        lst.push_back(25)
        lst.erase(2)
        self.assertEqual(lst.__str__(), '[5, 15]')

    def test_get_from_end(self):
        lst = SLL()
        self.assertEqual(lst.__str__(), '[]')
        lst.push_back(5)
        lst.push_back(15)
        lst.push_back(25)
        self.assertEqual(lst.nth_val_from_end(0), 25)




if __name__ == '__main__':
    unittest.main()
