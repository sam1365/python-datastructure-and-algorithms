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
