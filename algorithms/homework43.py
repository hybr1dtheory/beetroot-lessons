"""This module represents my implementation of AVL binary tree"""


class Node:
    """Class represents each node in the tree"""
    def __init__(self, data):
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None
        self.height: int = 1


class MyAVLTree:
    """My AVL tree with printing method"""
    def __init__(self):
        self.root = None

    def insert(self, data):
        """method defines a recursive function for inserting new element and call it"""
        def nested_insert(node, n_data):
            if node is None:
                return Node(n_data)
            if n_data < node.data:
                node.left = nested_insert(node.left, n_data)
            else:
                node.right = nested_insert(node.right, n_data)
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
            return self._balance(node)
        self.root = nested_insert(self.root, data)

    def delete(self, data):
        """method defines a recursive function for deleting element"""
        def nested_delete(node, n_data):
            if node is None:
                return None
            if n_data < node.data:
                node.left = nested_delete(node.left, n_data)
            elif n_data > node.data:
                node.right = nested_delete(node.right, n_data)
            else:
                # Found node to delete
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                # Delete node with two children and find minimum value in right subtree
                min_node = node.right
                while min_node.left is not None:
                    min_node = min_node.left
                # Replace value of the deleted node
                node.data = min_node.data
                # Delete minimum value from right subtree
                node.right = nested_delete(node.right, min_node.data)
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
            return self._balance(node)
        self.root = nested_delete(self.root, data)

    @staticmethod
    def get_height(node: Node) -> int:
        """Safety getting node height if node is none"""
        return node.height if node else 0

    def _left_rotate(self, node: Node) -> Node:
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        right_child.height = max(self.get_height(right_child.left), self.get_height(right_child.right)) + 1
        return right_child

    def _right_rotate(self, node: Node) -> Node:
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        left_child.height = max(self.get_height(left_child.left), self.get_height(left_child.right)) + 1
        return left_child

    def _get_balance_factor(self, node: Node) -> int:
        """Safety getting balance factor needed for balancing"""
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def _balance(self, node: Node) -> Node:
        balance_factor = self._get_balance_factor(node)
        # Right rotation
        if balance_factor > 1 and self._get_balance_factor(node.right) >= 0:
            return self._left_rotate(node)
        # Left rotation
        if balance_factor < -1 and self._get_balance_factor(node.left) <= 0:
            return self._right_rotate(node)
        # Right-left rotation
        if balance_factor > 1 and self._get_balance_factor(node.right) < 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        # Left-right rotation
        if balance_factor < -1 and self._get_balance_factor(node.left) > 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        return node

    def print_tree(self, node=None, level=0):
        """print binary tree/subtree with 90 deg. rotation"""
        if node is None:
            node = self.root
        if node.right:
            self.print_tree(node.right, level + node.right.height)
        print(' ' * 4 * level + str(node.data))
        if node.left:
            self.print_tree(node.left, level + node.left.height)


if __name__ == "__main__":
    tree = MyAVLTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)
    tree.insert(12)
    tree.insert(20)
    tree.insert(11)
    tree.print_tree()
