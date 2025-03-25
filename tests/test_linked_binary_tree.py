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

    def  test_replace(self):
        assert self.linked_binary_tree.root() is None
        self.linked_binary_tree.add_root(17)
        assert self.linked_binary_tree.root() is not None
        self.linked_binary_tree.replace(self.linked_binary_tree.root(), 13)
        assert self.linked_binary_tree.root().element() == 13