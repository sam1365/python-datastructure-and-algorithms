import pytest

from stack.linked_stack import LinkedStack

class TestLinkedStack:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.linked_stack = LinkedStack()

    def test_is_empty(self):
        """Test is_empty function of LinkedStack class."""

        assert self.linked_stack.is_empty() is True

    def test_push(self):
        """Test push function of LinkedStack class."""

        self.linked_stack.push(29)
        self.linked_stack.push(23)
        assert self.linked_stack.is_empty() is False
        assert len(self.linked_stack) == 2
        assert self.linked_stack.peek() == 23

    def test_pop(self):
        """Test pop function of LinkedStack class."""

        self.linked_stack.push(29)
        self.linked_stack.push(23)
        assert self.linked_stack.is_empty() is False
        assert len(self.linked_stack) == 2
        assert self.linked_stack.pop() == 23

    def test_peek_is_empty(self):
        """Test peek function of LinkedStack class
        when there is an empty instance of the class"""

        with pytest.raises(Exception, match='Stack is empty'):
            self.linked_stack.peek()
