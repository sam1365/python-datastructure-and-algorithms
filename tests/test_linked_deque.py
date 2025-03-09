import pytest

from deque_data_structure.linked_deque import LinkedDeque

class TestLinkedDeque:

    @pytest.fixture(autouse=True)
    def setup(self):
        """Initialize a linked deque for unit testing."""

        self.linked_deque = LinkedDeque()

    def test_is_empty(self):
        """Test is_empty method."""

        assert self.linked_deque.is_empty() is True

    def test_add_front(self):
        """Test add_front method to add front node to deque."""

        assert self.linked_deque.is_empty() is True
        self.linked_deque.add_front(21)
        assert self.linked_deque.is_empty() is False
        assert len(self.linked_deque) == 1
        assert self.linked_deque.front() == 21

    def test_add_rear(self):
        """Test add_rear method to add rear node to deque."""

        assert self.linked_deque.is_empty() is True
        self.linked_deque.add_rear(21)
        self.linked_deque.add_rear(23)
        assert self.linked_deque.is_empty() is False
        assert len(self.linked_deque) == 2
        assert self.linked_deque.rear() == 23

    def test_remove_front(self):
        """Test remove_front method to remove front node from deque."""

        assert self.linked_deque.is_empty() is True
        self.linked_deque.add_front(21)
        self.linked_deque.add_front(23)
        self.linked_deque.add_front(27)
        assert self.linked_deque.remove_front() == 27
        assert self.linked_deque.is_empty() is False
        assert len(self.linked_deque) == 2
        assert self.linked_deque.front() == 23

    def test_remove_rear(self):
        """Test remove_rear method to remove rear node from deque."""

        assert self.linked_deque.is_empty() is True
        self.linked_deque.add_rear(21)
        self.linked_deque.add_rear(23)
        self.linked_deque.add_rear(27)
        assert self.linked_deque.remove_rear() == 27
        assert self.linked_deque.is_empty() is False
        assert len(self.linked_deque) == 2
        assert self.linked_deque.front() == 21

    def test_clear_deque(self):
        """Test clear_deque method to clear deque."""

        assert self.linked_deque.is_empty() is True
        self.linked_deque.add_rear(21)
        self.linked_deque.add_rear(23)
        assert self.linked_deque.is_empty() is False
        assert len(self.linked_deque) == 2
        self.linked_deque.clear_deque()
        assert self.linked_deque.is_empty() is True
