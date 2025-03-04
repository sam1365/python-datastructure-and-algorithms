from linked_list_data_structure.single_linked_list import Node

class LinkedQueue:

    def __init__(self):
        self._head = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """Check if queue is empty."""

        return self._size == 0

    def enqueue(self, element):
        """Add element to the rear of the queue."""

        new_node = Node(element)
        if self.is_empty():
            self._head = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
        self._rear = new_node
        self._size += 1

    def dequeue(self):
        """Remove and return the first element of the queue."""

        if self.is_empty():
            raise Exception('Queue is empty')
        element = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():
            self._rear = None
        return element

    def peek(self):
        """Return the first element of the queue."""

        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head.element
