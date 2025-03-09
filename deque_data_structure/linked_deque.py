from linked_list_data_structure.doubly_linked_list import DoublyLinkedList

class LinkedDeque(DoublyLinkedList):
    """Implementation of Deque Data Structure By using doubly linked list.

    Methods:
        add_front(item): Add an item to the front of the deque.
        add_rear(item): Add an item to the rear of the deque.
        remove_front(): Remove an item from the front of the deque.
        remove_rear(): Remove an item from the rear of the deque.
        front(): Return the front item of the deque.
        rear(): Return the rear item of the deque.
        clear_deque(): Clear the deque.
    """

    def add_front(self, item):
        """Add an item to the front of the deque.

        Args:
            item: The item to add to the front of the deque.
        """

        self.insert_at_beginning(item)

    def add_rear(self, item):
        """Add an item to the rear of the deque.

        Args:
            item: The item to add to the rear of the deque.
        """

        self.insert_at_end(item)

    def remove_front(self):
        """Remove an item from the front of the deque if it is not empty.

        Raises:
            ValueError: If the deque is empty.

        Returns:
            item: The item removed from the front of the deque.
        """

        return self.remove_at_beginning()

    def remove_rear(self):
        """Remove an item from the rear of the deque if it is not empty.

        Raises:
            ValueError: If the deque is empty.

        Returns:
            item: The item removed from the rear of the deque.
        """

        return self.remove_at_end()

    def rear(self):
        """Return the rear item of the deque if it is not empty.

        Raises:
            ValueError: If the deque is empty.

        Returns:
            item: The item of rear node of the deque.
        """

        if self.is_empty():
            raise ValueError('List is empty')
        return self._sentinel_tail.prev.data

    def front(self):
        """Return the front item of the deque if it is not empty.

        Raises:
            ValueError: If the deque is empty.

        Returns:
            item: The item of front node of the deque if it is not empty.
        """

        if self.is_empty():
            raise ValueError('List is empty')
        return self._sentinel_head.next.data

    def clear_deque(self):
        """Clear the deque."""

        self.__init__()
