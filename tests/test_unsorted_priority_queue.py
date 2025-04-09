import pytest

from priority_queue_data_structure.priority_queue_data_structure import UnsortedPriorityQueue

class TestUnsortedPriorityQueue:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.priority_queue = UnsortedPriorityQueue()
    