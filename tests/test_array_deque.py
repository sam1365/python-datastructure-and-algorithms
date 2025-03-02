import pytest

from deque_data_structure.array_deque import ArrayDeque


class TestArrayDeque:

    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up an instance of ArrayDeque class for test methods."""

        self.array_deque = ArrayDeque()

    def test_is_empty(self):
        """Test the deque is empty."""

        assert self.array_deque.is_empty() is True

    def test_add_front(self):
        """Test add data to the front."""

        self.array_deque.add_front(1)
        self.array_deque.add_front(2)
        assert len(self.array_deque) == 2
        assert self.array_deque.front() == 2

    def test_add_rear(self):
        """Test add data to the rear."""

        self.array_deque.add_rear(13)
        self.array_deque.add_rear(11)
        assert len(self.array_deque) == 2
        assert self.array_deque.rear() == 11

    def test_remove_front(self):
        """Test remove data from front."""

        self.array_deque.add_front(17)
        self.array_deque.add_front(11)
        assert self.array_deque.remove_front() == 11
        assert len(self.array_deque) == 1

    def test_remove_front_is_empty(self):
        """Test remove at front from an empty deque."""

        with pytest.raises(IndexError, match='Empty deque'):
            self.array_deque.remove_front()

    def test_remove_rear(self):
        """Test remove data from rear."""

        self.array_deque.add_rear(17)
        self.array_deque.add_rear(11)
        assert self.array_deque.remove_rear() == 11
        assert len(self.array_deque) == 1

    def test_remove_rear_is_empty(self):
        """Test remove at rear from an empty deque."""

        with pytest.raises(IndexError, match='Empty deque'):
            self.array_deque.remove_rear()

    def test_increase_capacity(self):
        """Test increase the deque capacity."""

        for i in range(13):
            self.array_deque.add_front(i)
        assert len(self.array_deque) == 13

    def test_shrink(self):
        """Test shrink the deque capacity."""

        for i in range(20):
            self.array_deque.add_front(i)

        for i in range(17):
            self.array_deque.remove_front()
        assert len(self.array_deque) == 3

    def test_clear_deque(self):
        """Test clear the deque."""

        for i in range(3):
            self.array_deque.add_front(i)
        assert len(self.array_deque) == 3
        self.array_deque.clear_deque()
        assert len(self.array_deque) == 0