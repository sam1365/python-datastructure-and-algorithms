from linked_list_data_structure.single_linked_list import Node

class CircularLinkedList:

    def __init__(self):
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
        else:
            new_node.next = self._rear.next
            self._rear.next = new_node
        self._rear = new_node
        self._size += 1

    def remove_head(self):
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
        if self.is_empty():
            raise Exception('Empty List')
        return self._rear.next.data

