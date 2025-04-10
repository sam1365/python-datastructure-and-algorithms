import pytest

from priority_queue_data_structure.priority_queue_data_structure import SortedPriorityQueue

class TestUnsortedPriorityQueue:
    """
    Test Class for testing SortedPriorityQueue
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Initialize an instance of the SortedPriorityQueue class
        for unit testing
        """

        self.priority_queue = SortedPriorityQueue()

    def test_add(self):
        
        assert len(self.priority_queue) == 0
        self.priority_queue.add(1, 'A')
        self.priority_queue.add(2, 'B')
        assert len(self.priority_queue) == 2
        min_item = self.priority_queue.min()
        assert min_item == (1, 'A')

    def test_remove_min(self):
        self.priority_queue.add(1, 'A')
        self.priority_queue.add(2, 'B')
        removed_item = self.priority_queue.remove_min()
        assert removed_item == (1, 'A')