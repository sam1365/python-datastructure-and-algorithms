import pytest
from queue_data_structure.array_queue import ArrayQueue

class TestArrayQueue:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.array_queue = ArrayQueue()

    def test_is_empty(self):
        assert self.array_queue.is_empty() is True
