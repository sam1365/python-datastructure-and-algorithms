import pytest

from linked_list_data_structure.doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.doubly_linked_list = DoublyLinkedList()

    def test_is_empty(self):
        assert self.doubly_linked_list.is_empty() is True

    def test_insert_at_beginning(self):
        assert self.doubly_linked_list.is_empty() is True
        self.doubly_linked_list.insert_at_beginning(5)
        assert self.doubly_linked_list.is_empty() is False
        assert len(self.doubly_linked_list) == 1

    def test_insert_at_end(self):
        assert self.doubly_linked_list.is_empty() is True
        self.doubly_linked_list.insert_at_end(27)
        assert self.doubly_linked_list.is_empty() is False
        assert len(self.doubly_linked_list) == 1

    def test_remove_at_beginning(self):
        assert self.doubly_linked_list.is_empty() is True
        self.doubly_linked_list.insert_at_beginning(27)
        self.doubly_linked_list.insert_at_beginning(23)
        self.doubly_linked_list.insert_at_beginning(19)
        assert len(self.doubly_linked_list) == 3
        assert self.doubly_linked_list.is_empty() is False
        assert self.doubly_linked_list.remove_at_beginning() == 19
        assert len(self.doubly_linked_list) == 2

    def test_remove_at_end(self):
        assert self.doubly_linked_list.is_empty() is True
        self.doubly_linked_list.insert_at_end(27)
        self.doubly_linked_list.insert_at_end(23)
        self.doubly_linked_list.insert_at_beginning(19)
        assert self.doubly_linked_list.is_empty() is False
        assert len(self.doubly_linked_list) == 3
        assert self.doubly_linked_list.remove_at_end() == 23
        assert len(self.doubly_linked_list) == 2