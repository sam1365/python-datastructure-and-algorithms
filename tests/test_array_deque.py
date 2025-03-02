import pytest

from deque_data_structure.array_deque import ArrayDeque


class TestArrayDeque:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.array_deque = ArrayDeque()