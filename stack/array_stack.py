class ArrayStack:
    """
    A stack implementation using an array(list) as underlying data structure.

    Attributes:
        _stack (list): The internal list used to store stack elements.

    Methods:
        push(element): Add an item to the top of the stack.
        pop(): Removes and returns the item from the top of the stack.
        peek(): Returns the item from the top of the stack.
        __len__(): Returns the size of the stack.
        is_empty(): Returns whether the stack is empty.
    """

    def __init__(self):
        self._stack = []

    def __len__(self):
        """Return the size of the stack."""

        return len(self._stack)

    def pop(self):
        """Remove and return the item from the top of the stack."""

        if len(self._stack) == 0:
            raise Exception("Stack is empty")
        else:
            return self._stack.pop()

    def push(self, item):
        """Add an item to the top of the stack."""

        self._stack.append(item)

    def peek(self):
        """Return the item from the top of the stack."""

        if len(self._stack) == 0:
            raise Exception("Stack is empty")
        else:
            return self._stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""

        return len(self._stack) == 0