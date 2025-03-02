from linked_list_data_structure.single_linked_list import Node

class LinkedStack:
    """Stack implementation using linked list.

    Attributes:
        _head (Node): The last node in the stack.
        _size (int): The size of the stack.
    Methods:
        push(value): Add a node to as the new head of the stack.
        pop(): Removes and returns the head from the top of the stack.
        peek(): Returns the node data from the head of the stack.
        __len__(): Returns the size of the stack.
        is_empty(): Returns whether the stack is empty.
    """

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, value):
        self._head = Node(value, self._head)
        self._size += 1

    def peek(self):
        if self._head is None:
            raise Exception('Stack is empty')
        return self._head.data

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        head_data = self._head.data
        self._head = self._head.next
        self._size -= 1
        return head_data
