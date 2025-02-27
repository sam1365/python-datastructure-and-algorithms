import pytest
from linked_list_data_structure.single_linked_list import SingleLinkedList

class TestSingleLinkedList:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.sll = SingleLinkedList()

    def test_insert_node_to_head(self):
        """Test inserting node at the head of the list."""

        self.sll.insert_node_to_head(11)

        assert self.sll.head() == 11
        assert self.sll.tail() == 11
        assert len(self.sll) == 1