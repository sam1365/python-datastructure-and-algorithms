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

    def test_min(self):
        """
        Test if min method in UnsortedPriorityQueue
        return correct min key
        """

        self.priority_queue.add(4, 'D')
        self.priority_queue.add(5, 'E')
        self.priority_queue.add(1, 'A')
        self.priority_queue.add(2, 'B')
        self.priority_queue.add(3, 'C')
        min = self.priority_queue.min()
        assert min == (1, 'A')

    def test_remove_min(self):
        """
        Test if remove_min method in UnsortedPriorityQueue
        remove correct item with min key
        """

        self.priority_queue.add(4, 'D')
        self.priority_queue.add(5, 'E')
        self.priority_queue.add(1, 'A')
        self.priority_queue.add(2, 'B')
        self.priority_queue.add(3, 'C')
        old_min = self.priority_queue.remove_min()
        assert old_min == (1, 'A')
        min_item = self.priority_queue.min()
        assert min_item == (2, 'B')
