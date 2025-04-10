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

