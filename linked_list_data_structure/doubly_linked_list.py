class DoublyLinkedNode:
    """Doubly Linked Node

    Attributes:
        data: data of node
        next: next node of node
        prev: previous node of node
    Methods:
        __init__(self, data): Initialize the node with given data
    """

    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class BaseDoubleLinkedList:
    """Base Class for Doubly Linked List Data Structure

    Attributes:
        _sentinel_head: sentinel head of doubly linked list
        _sentinel_tail: sentinel tail of doubly linked list
        _size: size of linked doubly list

    Methods:
        __init__(self): Initialize the doubly linked list
        __len__(self): Return the length of the doubly linked list
        is_empty(self): Check if doubly linked list is empty
        _insert_between_nodes(self, data, previous_node, next_node):
            Create new node for data and insert it between previous node and next node
        _remove_node(self, node): Remove node from doubly linked list
    """

    def __init__(self):
        """Initialize the doubly linked list"""

        self._sentinel_head = DoublyLinkedNode(None, None, None)
        self._sentinel_tail = DoublyLinkedNode(None, None, None)
        self._sentinel_head.next = self._sentinel_tail
        self._sentinel_tail.prev = self._sentinel_head
        self._size = 0

    def __len__(self):
        """Return the length of the doubly linked list"""

        return self._size

    def is_empty(self):
        """Check if doubly linked list is empty"""

        return self._size == 0

    def _insert_between_nodes(self, data, previous_node, next_node):
        """Create new node  and insert it between two nodes of doubly linked list

        Args:
            data: data of new node
            previous_node: previous node of new node
            next_node: next node of new node
        """

        new_node = DoublyLinkedNode(data, previous_node, next_node)
        previous_node.next = new_node
        next_node.prev = new_node
        self._size += 1

    def _remove_node(self, node):
        """Remove node from doubly linked list

        Raises:
            ValueError: If List is empty.

        Returns:
            The data of removed node.
        """

        if self.is_empty():
            raise ValueError("List is empty")

        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node
        self._size -= 1
        return node.data

class DoublyLinkedList(BaseDoubleLinkedList):
    """Doubly Linked List Data Structure

    Methods:
        insert_at_beginning(self, data): Insert data at the beginning of doubly linked list
        insert_at_end(self, data): Insert data at the end of doubly linked list
        remove_at_beginning(self, node): Remove node at the beginning of doubly linked list
        remove_at_end(self, node): Remove node at the end of doubly linked list
    """

    def insert_at_beginning(self, data):
        """Insert data at the beginning of doubly linked list"""

        self._insert_between_nodes(data, self._sentinel_head, self._sentinel_head.next)

    def insert_at_end(self, data):
        """Insert data at the end of doubly linked list"""

        self._insert_between_nodes(data, self._sentinel_tail.prev, self._sentinel_tail)

    def remove_at_beginning(self):
        """Remove node at the beginning of doubly linked list
        Raises:
            ValueError: If List is empty.

        Returns:
            The data of removed node.
        """

        if self.is_empty():
            raise ValueError("List is empty")
        return self._remove_node(self._sentinel_head.next)


    def remove_at_end(self):
        """Remove node at the end of doubly linked list
        Raises:
            ValueError: If List is empty.

        Returns:
            The data of removed node.
        """

        if self.is_empty():
            raise ValueError("List is empty")
        return self._remove_node(self._sentinel_tail.prev)
