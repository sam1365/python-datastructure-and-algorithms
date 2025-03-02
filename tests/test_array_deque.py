import pytest

from deque_data_structure.array_deque import ArrayDeque


class TestArrayDeque:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.array_deque = ArrayDeque()

    def test_is_empty(self):
        assert self.array_deque.is_empty() is True

    def test_add_front(self):
        self.array_deque.add_front(1)
        self.array_deque.add_front(2)
        assert len(self.array_deque) == 2
        assert self.array_deque.front() == 2
