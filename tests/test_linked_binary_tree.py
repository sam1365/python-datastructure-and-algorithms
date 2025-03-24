import pytest

from tree_data_structure.binary_tree import LinkedBinaryTree


class TestLinkedBinaryTree:

    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up an instance of LinkedBinaryTree for test methods."""

        self.linked_binary_tree = LinkedBinaryTree()

    def test_is_empty(self):
        """Test the binary tree is empty."""

        assert self.linked_binary_tree.is_empty() is True
