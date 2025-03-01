import pytest

from stack.array_stack import ArrayStack

class TestArrayStack:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.array_stack = ArrayStack()

    def test_is_empty(self):
        """Test is_empty function in the array stack."""
        assert self.array_stack.is_empty() is True

    def test_push(self):
        self.array_stack.push(1)
        self.array_stack.push(2)
        self.array_stack.push(3)
        self.array_stack.push(5)
        assert self.array_stack.is_empty() is False
        assert self.array_stack.peek() == 5
    def test_pop(self):
        self.array_stack.push(1)
        self.array_stack.push(2)
        self.array_stack.push(3)
        assert self.array_stack.pop() == 3
        assert len(self.array_stack) == 2