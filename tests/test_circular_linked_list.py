import pytest

from linked_list_data_structure.circular_linked_list import CircularLinkedList

class TestCircularLinkedList:

    @pytest.fixture(autouse=True)
    def setup(self):
        """Initialize a circular linked list for unit testing."""

        self.circular_linked_list = CircularLinkedList()

    def test_is_empty(self):
        """Test is_empty method."""

        assert self.circular_linked_list.is_empty() is True

    def test_insert_rear(self):
        """Test insert_rear method to
        inserting new node at the rear."""

        self.circular_linked_list.insert_rear(1)
        self.circular_linked_list.insert_rear(2)
        self.circular_linked_list.insert_rear(3)
        assert self.circular_linked_list.is_empty() is False
        assert len(self.circular_linked_list) == 3
        assert self.circular_linked_list.peek() == 1

    def test_remove_head(self):
        """Test remove_head method to remove node at the head."""

        self.circular_linked_list.insert_rear(11)
        self.circular_linked_list.insert_rear(13)
        self.circular_linked_list.insert_rear(17)
        assert self.circular_linked_list.is_empty() is False
        assert len(self.circular_linked_list) == 3
        assert self.circular_linked_list.remove_head() == 11
        assert len(self.circular_linked_list) == 2
        assert self.circular_linked_list.peek() == 13

    def test_remove_head_for_empty_list(self):
        """Test remove_head for empty list."""

        with pytest.raises(Exception, match='Empty List'):
            self.circular_linked_list.remove_head()
