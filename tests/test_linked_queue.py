import pytest

from queue_data_structure.linked_queue import LinkedQueue


class TestLinkedQueue:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.linked_queue = LinkedQueue()

    