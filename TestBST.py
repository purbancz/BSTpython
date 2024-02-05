import unittest
from random import randint

from BST import BST


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        for _ in range(20):
            self.bst.insert(randint(0, 99))
        self.bst.insert(100)
        for _ in range(20):
            self.bst.insert(randint(101, 200))

    def test_insert(self):
        self.bst.insert(201)
        self.assertIn(201, self.bst)
        self.bst.insert(100)
        self.assertIn(100, self.bst)
        self.bst.insert(1.5)
        self.assertIn(1.5, self.bst)
        with self.assertRaises(ValueError):
            self.bst.insert("str_test")

    def test_insert_placement(self):
        self.bst.insert(300)
        self.assertIn(300, self.bst)
        self.bst.insert(299)
        self.assertIn(299, self.bst)
        self.bst.insert(301)
        self.assertIn(301, self.bst)
        node = self.bst.get_node_by_value(300)
        self.assertIsNotNone(node.left)
        self.assertEqual(node.left.val, 299)
        self.assertIsNotNone(node.right)
        self.assertEqual(node.right.val, 301)

    def test_get_node_by_value(self):
        node = self.bst.get_node_by_value(100)
        self.assertEqual(node.val, 100)

    def test_get_node_by_value_invalid(self):
        with self.assertRaises(ValueError):
            self.bst.get_node_by_value(201)

    def test_print_in_order_traversal_invalid(self):
        with self.assertRaises(ValueError):
            self.bst.print_in_order_traversal(201)
        with self.assertRaises(ValueError):
            self.bst.print_in_order_traversal('str_test')
        with self.assertRaises(ValueError):
            self.bst.print_in_order_traversal(self.bst.get_node_by_value(201))

    def test_contains(self):
        self.assertTrue(100 in self.bst)
        self.assertFalse(201 in self.bst)

    def test_iot_iterator(self):
        self.assertEqual(list(iter(self.bst)), sorted(list(iter(self.bst))))


if __name__ == "__main__":
    unittest.main()
