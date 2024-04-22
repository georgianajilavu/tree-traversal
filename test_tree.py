import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    def test_find_existing_data(self):
        tree = Tree()
        tree.add(9)
        tree.add(8)
        tree.add(3)
        tree.add(7)
        tree.add(1)
        tree.add(5)
        tree.add(6)
        self.assertTrue(tree._find(9, tree.getRoot()))

    def test_find_non_existing_data(self):
        tree = Tree()
        tree.add(9)
        tree.add(8)
        tree.add(3)
        tree.add(7)
        tree.add(1)
        tree.add(5)
        tree.add(6)
        self.assertFalse(tree._find(10, tree.getRoot()))

if __name__ == '__main__':
    unittest.main()