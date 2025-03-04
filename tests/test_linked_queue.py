import pytest

from queue_data_structure.linked_queue import LinkedQueue


class TestLinkedQueue:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.linked_queue = LinkedQueue()

    def test_is_empty(self):
        """Test is_empty."""

        assert self.linked_queue.is_empty() is True

    def test_enqueue(self):
        """Test enqueue method for adding elements to the queue."""

        self.linked_queue.enqueue(1)
        self.linked_queue.enqueue(2)
        self.linked_queue.enqueue(3)
        assert self.linked_queue.peek() == 1
        assert self.linked_queue.is_empty() is False
        assert len(self.linked_queue) == 3

    def test_dequeue(self):
        """Test dequeue method for deleting an element from the queue."""
        self.linked_queue.enqueue(17)
        self.linked_queue.enqueue(13)
        self.linked_queue.enqueue(11)
        assert self.linked_queue.peek() == 17
        assert self.linked_queue.dequeue() == 17
        assert len(self.linked_queue) == 2

    def test_dequeue_is_empty(self):
        """Test dequeue method for deleting element from an empty queue."""
        with pytest.raises(Exception, match='Queue is empty'):
            self.linked_queue.dequeue()
