import pytest

from linked_list_data_structure.circular_linked_list import CircularLinkedList

class TestCircularLinkedList:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.circular_linked_list = CircularLinkedList()

    def test_is_empty(self):
        assert self.circular_linked_list.is_empty() is True

    def test_insert_rear(self):
        self.circular_linked_list.insert_rear(1)
        self.circular_linked_list.insert_rear(2)
        self.circular_linked_list.insert_rear(3)
        assert self.circular_linked_list.is_empty() is False
        assert len(self.circular_linked_list) == 3
        assert self.circular_linked_list.peek() == 1

    def test_remove_head(self):
        self.circular_linked_list.insert_rear(11)
        self.circular_linked_list.insert_rear(13)
        self.circular_linked_list.insert_rear(17)
        assert self.circular_linked_list.is_empty() is False
        assert len(self.circular_linked_list) == 3
        assert self.circular_linked_list.remove_head() == 11
        assert len(self.circular_linked_list) == 2
        assert self.circular_linked_list.peek() == 13

    def test_remove_head_for_empty_list(self):
        with pytest.raises(Exception, match='Empty List'):
            self.circular_linked_list.remove_head()