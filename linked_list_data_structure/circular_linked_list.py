from linked_list_data_structure.single_linked_list import Node

class CircularLinkedList:
    """Implementation of Circular Linked List data structure.
    Attributes:
        _rear: The last node in the list.
        _size: The size of the list.
    Methods
        __init__: Initialize the circular linked list.
         __len__: Return the size of the list.
         is_empty: Check if list is empty.
         insert_rear: Insert a new node in the circular linked list.
         remove_head: Remove first node(head ) of the list.
         peek: Return the first node(head) of the list.
     """

    def __init__(self):
        """Initialize the circular linked list."""

        self._rear = None
        self._size = 0

    def __len__(self):
        """Return the size of the list."""

        return self._size

    def is_empty(self):
        """Check if list is empty."""

        return self._size == 0

    def insert_rear(self, data):
        """Insert a new node at the end of the circular linked list and
        then link it to the first node of the list.

        Args:
            data: Data to add to the rear of the list.
        """

        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
        else:
            new_node.next = self._rear.next
            self._rear.next = new_node
        self._rear = new_node
        self._size += 1

    def remove_head(self):
        """Remove first node(head) of the list and return its data.

        Raises:
            Exception: If the list is empty.
        Returns:
            First node(head) data of the list.
        """

        if self.is_empty():
            raise Exception('Empty List')

        pop_node = self._rear.next
        if self._size == 1:
            self._rear = None
        else:
            self._rear.next = pop_node.next
        self._size -= 1
        return pop_node.data

    def peek(self):
        """Return data of first node(head) of the list

        Raises:
            Exception: If the list is empty.

        Returns:
            Data of first node(head) of the list.
        """

        if self.is_empty():
            raise Exception('Empty List')
        return self._rear.next.data

