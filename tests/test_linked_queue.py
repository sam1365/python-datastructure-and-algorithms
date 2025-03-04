import pytest

from queue_data_structure.linked_queue import LinkedQueue


class TestLinkedQueue:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.linked_queue = LinkedQueue()

    def test_is_empty(self):
        """Test is_empty."""

        assert self.linked_queue.is_empty() is True

