import pytest

from priority_queue_data_structure.priority_queue_data_structure import UnsortedPriorityQueue

class TestUnsortedPriorityQueue:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.priority_queue = UnsortedPriorityQueue()

    def test_add(self):
        assert len(self.priority_queue) == 0
        self.priority_queue.add(1, 'A')
        assert len(self.priority_queue) == 1
