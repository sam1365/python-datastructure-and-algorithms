from linked_list_data_structure.single_linked_list import Node

class LinkedQueue:
    """Implementation of Queue data structure by linked list.
    Attributes:
        _head: The first node in the queue.
        _rear: The last node in the queue.
        _size: The size of the queue.
    Methods
        is_empty: Check if queue is empty.
        enqueue: Add element to the rear of the queue.
        dequeue: Remove and return the first element of the queue.
        peek: Return the first element of the queue.
     """

    def __init__(self):
        """Initialize an empty queue."""

        self._head = None
        self._rear = None
        self._size = 0

    def __len__(self):
        """Return the size of the queue."""

        return self._size

    def is_empty(self):
        """Check if queue is empty."""

        return self._size == 0

    def enqueue(self, element):
        """Add element to the rear of the queue.

        Args:
            element: Element to be added to the rear of the queue.
        """

        new_node = Node(element)
        if self.is_empty():
            self._head = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
        self._rear = new_node
        self._size += 1

    def dequeue(self):
        """Remove and return the first element of the queue.

        Raises:
            Exception: If queue is empty.

        Returns:
            The first(front) element of the queue.
        """

        if self.is_empty():
            raise Exception('Queue is empty')
        element = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():
            self._rear = None
        return element

    def peek(self):
        """Return the first(head) element of the queue.

        Raises:
            Exception: If queue is empty.

        Returns:
            The first(front) element of the queue.
        """

        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head.data
