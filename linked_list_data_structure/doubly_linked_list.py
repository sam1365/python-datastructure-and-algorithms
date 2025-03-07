class DoublyLinkedNode:

    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        self._sentinel_head = DoublyLinkedNode(None, None, None)
        self._sentinel_tail = DoublyLinkedNode(None, None, None)
        self._sentinel_head.next = self._sentinel_tail
        self._sentinel_tail.prev = self._sentinel_head
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between_nodes(self, data, previous_node, next_node):
        new_node = DoublyLinkedNode(data, previous_node, next_node)
        previous_node.next = new_node
        next_node.prev = new_node
        self._size += 1

    def _remove_node(self, node):
        if self.is_empty():
            raise ValueError("List is empty")

        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node
        self._size -= 1
        return node.data

    def insert_at_beginning(self, data):
        self._insert_between_nodes(data, self._sentinel_head, self._sentinel_head.next)

    def insert_at_end(self, data):
        self._insert_between_nodes(data, self._sentinel_tail.prev, self._sentinel_tail)

    def remove_at_beginning(self):
        if self.is_empty():
            raise ValueError("List is empty")
        return self._remove_node(self._sentinel_head.next)


    def remove_at_end(self):
        if self.is_empty():
            raise ValueError("List is empty")
        return self._remove_node(self._sentinel_tail.prev)
