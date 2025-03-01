import pytest

from stack.array_stack import ArrayStack

class TestArrayStack:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.array_stack = ArrayStack()

    def test_is_empty(self):
        """Test is_empty function in the array stack."""
        assert self.array_stack.is_empty() is True