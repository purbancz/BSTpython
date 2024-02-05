from random import randint


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BST:
    def __init__(self):
        self.root = None
        self.__nodes = {}

    def get_node_by_value(self, key):
        if key in self.__nodes:
            return self.__nodes[key]
        else:
            raise ValueError("No such node found in BST")

    def insert(self, key):
        if not hasattr(key, "__lt__"):
            raise ValueError("Keys must be comparable")
        if key not in self:
            if self.root is None:
                self.root = Node(key)
                self.__nodes[key] = self.root
            else:
                try:
                    self._insert_helper(self.root, key)
                except TypeError:
                    raise ValueError("New keys must be comparable with other keys in the BST")

    def _insert_helper(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
                self.__nodes[key] = node.left
            else:
                self._insert_helper(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
                self.__nodes[key] = node.right
            else:
                self._insert_helper(node.right, key)

    def __iter__(self):
        return BstIotIterator(self)

    def __contains__(self, key):
        return key in self.__nodes

    def print_in_order_traversal(self, start_node=None):
        print(" ".join(str(val) for val in BstIotIterator(self, start_node)))


class BstIotIterator:

    def __init__(self, bst, start_node=None):
        self.stack = []
        if start_node is None:
            start_node = bst.root
        elif isinstance(start_node, Node):
            pass
        else:
            start_node = bst.get_node_by_value(start_node)
        self._go_left(start_node)

    def _go_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        if node.right is not None:
            self._go_left(node.right)
        return node.val

    def __iter__(self):
        return self


if __name__ == "__main__":
    bst = BST()

    try:
        for _ in range(20):
            bst.insert(randint(0, 99))
        bst.insert(100)
        for _ in range(20):
            bst.insert(randint(101, 200))
        # bst.insert("str_test")  # Should raise error
    except ValueError as e:
        print(e)

    try:
        bst.print_in_order_traversal()
        bst.print_in_order_traversal(100)
        bst.print_in_order_traversal(bst.get_node_by_value(100))
        # bst.print_in_order_traversal(201)  # Should raise error
        # bst.print_in_order_traversal(bst.get_node_by_value(201))  # Should raise error
        # bst.print_in_order_traversal("str_test")  # Should raise error
    except ValueError as e:
        print(e)
