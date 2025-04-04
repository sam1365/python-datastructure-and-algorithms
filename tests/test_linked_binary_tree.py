import pytest

from tree_data_structure.binary_tree import (LinkedBinaryTree,
                                             BinaryTreePosition,
                                             )


class TestLinkedBinaryTree:

    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up an instance of LinkedBinaryTree for test methods."""

        self.linked_binary_tree = LinkedBinaryTree()

    def test_is_empty(self):
        """Test the binary tree is empty."""

        assert self.linked_binary_tree.is_empty() is True

    def test_add_root(self):
        self.linked_binary_tree.add_root(17)
        assert self.linked_binary_tree.is_empty() is False
        assert self.linked_binary_tree.root() is not None
        assert isinstance(self.linked_binary_tree.root(), BinaryTreePosition)

    def test_root(self):
        assert self.linked_binary_tree.root() is None
        self.linked_binary_tree.add_root(17)
        assert self.linked_binary_tree.root() is not None
        assert isinstance(self.linked_binary_tree.root(), BinaryTreePosition)

    def test_add_left(self):
        assert self.linked_binary_tree.root() is None
        self.linked_binary_tree.add_root(17)
        assert self.linked_binary_tree.root() is not None
        self.linked_binary_tree.add_left(self.linked_binary_tree.root(), 19)
        assert self.linked_binary_tree.left(self.linked_binary_tree.root()) is not None
        assert isinstance(self.linked_binary_tree.left(self.linked_binary_tree.root()),
                          BinaryTreePosition)
        assert self.linked_binary_tree.left(self.linked_binary_tree.root()).element() == 19

    def test_add_right(self):
        assert self.linked_binary_tree.root() is None
        self.linked_binary_tree.add_root(17)
        assert self.linked_binary_tree.root() is not None
        self.linked_binary_tree.add_right(self.linked_binary_tree.root(), 23)
        assert self.linked_binary_tree.right(self.linked_binary_tree.root()) is not None
        assert isinstance(self.linked_binary_tree.right(self.linked_binary_tree.root()),
                          BinaryTreePosition)
        assert self.linked_binary_tree.right(self.linked_binary_tree.root()).element() == 23

    def test_replace(self):
        assert self.linked_binary_tree.root() is None
        self.linked_binary_tree.add_root(17)
        assert self.linked_binary_tree.root() is not None
        self.linked_binary_tree.replace(self.linked_binary_tree.root(), 13)
        assert self.linked_binary_tree.root().element() == 13

    def test_parent(self):
        assert self.linked_binary_tree.root() is None
        self.linked_binary_tree.add_root(17)
        assert self.linked_binary_tree.root() is not None
        self.linked_binary_tree.add_left(self.linked_binary_tree.root(), 23)
        self.linked_binary_tree.add_right(self.linked_binary_tree.root(), 11)
        self.linked_binary_tree.number_of_children(self.linked_binary_tree.root()) == 2
        assert self.linked_binary_tree.left(self.linked_binary_tree.root()).element() == 23
        assert isinstance(self.linked_binary_tree.left(self.linked_binary_tree.root()), BinaryTreePosition)
        assert self.linked_binary_tree.parent(self.linked_binary_tree.left(self.linked_binary_tree.root())) is not None
        assert self.linked_binary_tree.parent(self.linked_binary_tree.right(self.linked_binary_tree.root())) is not None

    def test_delete_leaf(self):
        assert self.linked_binary_tree.root() is None
        self.linked_binary_tree.add_root(17)
        assert self.linked_binary_tree.root() is not None
        self.linked_binary_tree.add_left(self.linked_binary_tree.root(), 23)
        self.linked_binary_tree.add_left(
            self.linked_binary_tree.left(self.linked_binary_tree.root()),
            27
        )
        assert self.linked_binary_tree.left(
            self.linked_binary_tree.left(self.linked_binary_tree.root())).element() == 27
        assert self.linked_binary_tree.number_of_children(
            self.linked_binary_tree.left(
                self.linked_binary_tree.left(self.linked_binary_tree.root()))
        ) == 0
        assert self.linked_binary_tree.delete(
            self.linked_binary_tree.left(
                self.linked_binary_tree.left(self.linked_binary_tree.root()))
        ) == 27

    def test_delete_inner_node(self):
        assert self.linked_binary_tree.root() is None
        self.linked_binary_tree.add_root(17)
        assert self.linked_binary_tree.root() is not None
        self.linked_binary_tree.add_left(self.linked_binary_tree.root(), 23)
        self.linked_binary_tree.add_left(
            self.linked_binary_tree.left(self.linked_binary_tree.root()),
            27
        )
        assert self.linked_binary_tree.left(
            self.linked_binary_tree.left(self.linked_binary_tree.root())).element() == 27
        assert self.linked_binary_tree.number_of_children(
            self.linked_binary_tree.left(
                self.linked_binary_tree.left(self.linked_binary_tree.root()))
        ) == 0
        assert self.linked_binary_tree.delete(
                self.linked_binary_tree.left(self.linked_binary_tree.root())
        ) == 23
        assert self.linked_binary_tree.left(self.linked_binary_tree.root()).element() == 27

    def test_delete_parent_with_two_children(self):
        """Test of deleting a node with two children."""

        assert self.linked_binary_tree.root() is None
        self.linked_binary_tree.add_root(17)
        assert self.linked_binary_tree.root() is not None
        self.linked_binary_tree.add_left(self.linked_binary_tree.root(), 23)
        self.linked_binary_tree.add_right((self.linked_binary_tree.root()),
            27
        )
        with pytest.raises(Exception, match='Position has two children'):
            self.linked_binary_tree.delete(self.linked_binary_tree.root())

    def test_attach_working(self):
        """Test attaching two trees to a node"""

        tree1 = LinkedBinaryTree()
        tree2 = LinkedBinaryTree()
        self.linked_binary_tree.add_root(1)
        tree1.add_root(2)
        tree2.add_root(3)
        self.linked_binary_tree.attach(self.linked_binary_tree.root(), tree1, tree2)
        assert self.linked_binary_tree.left(self.linked_binary_tree.root()).element() == 2
        assert self.linked_binary_tree.right(self.linked_binary_tree.root()).element() == 3

    def test_attach_non_leaf(self):
        """Test attaching two trees to a non leaf node"""

        tree1 = LinkedBinaryTree()
        tree2 = LinkedBinaryTree()
        self.linked_binary_tree.add_root(1)
        self.linked_binary_tree.add_right(self.linked_binary_tree.root(),
                                          5)
        tree1.add_root(2)
        tree2.add_root(3)
        with pytest.raises(Exception, match='Position must be leaf'):
            self.linked_binary_tree.attach(self.linked_binary_tree.root(), tree1, tree2)

    def test_attach_different_tree_types(self):
        """Test attaching two trees of different types to a node of the binary tree"""
        class OtherBinaryTree(LinkedBinaryTree):
            pass

        tree1 = OtherBinaryTree()
        tree2 = LinkedBinaryTree()

        self.linked_binary_tree.add_root(1)
        tree1.add_root(2)
        tree2.add_root(3)

        with pytest.raises(Exception, match='Trees must have same type'):
            self.linked_binary_tree.attach(self.linked_binary_tree.root(), tree1, tree2)

    def test_preorder(self):
        """Test preorder traversal of a binary tree"""

        self.linked_binary_tree.add_root(1)
        left = self.linked_binary_tree.add_left(self.linked_binary_tree.root(), 2)
        right = self.linked_binary_tree.add_right(self.linked_binary_tree.root(), 3)
        self.linked_binary_tree.add_left(left, 5)
        self.linked_binary_tree.add_right(left, 7)

        preorder_result = [p.element() for p in self.linked_binary_tree.preorder()]
        assert preorder_result == [1, 2, 5, 7, 3]

    def test_postorder(self):
        """Test postorder traversal of a binary tree"""

        self.linked_binary_tree.add_root(1)
        left = self.linked_binary_tree.add_left(self.linked_binary_tree.root(), 2)
        right = self.linked_binary_tree.add_right(self.linked_binary_tree.root(), 3)
        self.linked_binary_tree.add_left(left, 5)
        self.linked_binary_tree.add_right(left, 7)

        postorder_result = [p.element() for p in self.linked_binary_tree.postorder()]
        assert postorder_result == [5, 7, 2, 3, 1]

    def test_breadthfirst(self):
        """Test breadth-first traversal of a binary tree"""

        self.linked_binary_tree.add_root(1)
        left = self.linked_binary_tree.add_left(self.linked_binary_tree.root(), 2)
        right = self.linked_binary_tree.add_right(self.linked_binary_tree.root(), 3)
        self.linked_binary_tree.add_left(left, 5)
        self.linked_binary_tree.add_right(left, 7)
        breadthfirst_result = [p.element() for p in self.linked_binary_tree.breadthfirst()]
        assert breadthfirst_result == [1, 2, 3, 5, 7]

    def test_inorder(self):
        """Test inorder traversal of a binary tree"""

        self.linked_binary_tree.add_root(1)
        left = self.linked_binary_tree.add_left(self.linked_binary_tree.root(), 2)
        right = self.linked_binary_tree.add_right(self.linked_binary_tree.root(), 3)
        self.linked_binary_tree.add_left(left, 5)
        self.linked_binary_tree.add_right(left, 7)
        inorder_result = [p.element() for p in self.linked_binary_tree.inorder()]
        assert inorder_result == [5, 2, 7, 1, 3]
