class Node:
    def __init__(self, data, next_node=None):
        self.next = next_node
        self.data = data

class SingleLinkedList:
    """
    Single linked list data structure

    Attributes:
        _head (Node): The first node of the list.
        _tail (Node): The last node of the list.
        _size (int): The number of nodes in the list.

    Methods:
        __len__(): Returns the number of nodes in the list.
        is_empty(): Checks if the list is empty.
        insert_node_to_head(data): Inserts a new node at the head.
        insert_node_to_tail(data): Inserts a new node at the tail.
        head(): Returns the data of the head node.
        tail(): Returns the data of the tail node.
        remove_head(): Removes and returns the head node's data.
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Returns the number of nodes in the list."""

        return self._size

    def is_empty(self):
        """Checks if the list is empty."""

        return self._size == 0

    def insert_node_to_head(self, data):
        """Inserts a node at the head of the list."""

        if self.is_empty():
            new_node = Node(data)
            self._head = self._tail = new_node
        else:
            self._head = Node(data, self._head)
        self._size += 1

    def insert_node_to_tail(self, data):
        """Inserts a node at the tail of the list."""

        new_node = Node(data)
        if self.is_empty():
            self._head = self._tail = new_node
        self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def head(self):
        """Returns data of the head node in the list"""

        if self.is_empty():
            raise ValueError('List is empty')
        return self._head.data

    def tail(self):
        """Returns data of the tail node in the list"""

        if self.is_empty():
            raise ValueError('List is empty')
        return self._tail.data

    def remove_head(self):
        """Removes the head node and returns its data from the list"""

        if self.is_empty():
            raise ValueError('List is empty')
        head_data = self._head.data
        if self._size == 1:
            self._head = None
        else:
            self._head = self._head.next
        self._size -= 1
        return head_data
