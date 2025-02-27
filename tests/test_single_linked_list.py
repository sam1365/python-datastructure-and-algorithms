import pytest
from linked_list_data_structure.single_linked_list import SingleLinkedList

class TestSingleLinkedList:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.sll = SingleLinkedList()

    def test_is_empty(self):
        """Test is empty list."""
        assert self.sll.is_empty() is True

    def test_insert_node_to_head(self):
        """Test inserting node at the head of the list."""

        self.sll.insert_node_to_head(11)

        assert self.sll.head() == 11
        assert self.sll.tail() == 11
        assert len(self.sll) == 1

    def test_insert_node_to_tail(self):
        """Test inserting nodes at the tail of the list."""

        self.sll.insert_node_to_tail(11)
        self.sll.insert_node_to_tail(13)
        self.sll.insert_node_to_tail(17)

        assert self.sll.head() == 11
        assert self.sll.tail() == 17
        assert len(self.sll) == 3

    def test_remove_head(self):
        """Test remove head node of the list."""

        self.sll.insert_node_to_head(11)
        self.sll.insert_node_to_head(13)
        self.sll.insert_node_to_head(17)

        assert self.sll.remove_head() == 17
        assert self.sll.head() == 13
        assert len(self.sll) == 2