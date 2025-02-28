import pytest
from queue_data_structure.array_queue import ArrayQueue

class TestArrayQueue:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.array_queue = ArrayQueue()

    def test_is_empty(self):
        assert self.array_queue.is_empty() is True

    def test_enqueue(self):
        """Test enqueue elements in the array queue."""

        self.array_queue.enqueue(1)
        self.array_queue.enqueue(2)

        assert self.array_queue.is_empty() is False
        assert len(self.array_queue) == 2
        assert self.array_queue.peek() == 1

    def test_dequeue(self):
        """Test enqueue elements in the array queue."""

        self.array_queue.enqueue(1)
        self.array_queue.enqueue(2)
        self.array_queue.enqueue(3)
        assert self.array_queue.dequeue() == 1
        assert self.array_queue.is_empty() is False
        assert len(self.array_queue) == 2
        assert self.array_queue.peek() == 2

    def test_peak(self):
        """Test peak in the array queue."""

        self.array_queue.enqueue(1)
        assert self.array_queue.peek() == 1

        self.array_queue.enqueue(2)
        assert self.array_queue.peek() == 1

    def test_peak_is_empty(self):
        """Test peak when queue is empty in the array queue."""
        with pytest.raises(Exception, match='Queue is empty') as e:
            self.array_queue.peek()