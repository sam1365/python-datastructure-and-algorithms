import pytest

from stack.linked_stack import LinkedStack

class TestLinkedStack:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.linked_stack = LinkedStack()

    def test_is_empty(self):
        assert self.linked_stack.is_empty() is True