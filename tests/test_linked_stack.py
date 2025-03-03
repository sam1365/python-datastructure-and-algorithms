import pytest

from stack.linked_stack import LinkedStack

class TestLinkedStack:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.linked_stack = LinkedStack()

    