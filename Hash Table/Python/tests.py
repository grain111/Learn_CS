import unittest

from HashTable import hash_table

class test_HashTable(unittest.TestCase):

    def test_basic(self):
        ht = hash_table()
        ht.insert(54578, 15)
        ht.insert(58, 2)
        ht.insert(14, 89)
        ht.insert(4987, 1)
        ht.insert(726552322, "Bartek")
        ht.insert("Cat", "Dog")

        self.assertEqual(ht.get(58), 2)
        self.assertEqual(ht.get(726552322), "Bartek")
        self.assertEqual(ht.get("Cat"), "Dog")

        ht.set(726552322, "Kasia")
        self.assertEqual(ht.get(726552322), "Kasia")
        self.assertRaises(ValueError, ht.set, 5, 15)
        self.assertRaises(ValueError, ht.get, 5)

if __name__ == "__main__":
    unittest.main()
