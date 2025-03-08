from linked_list_data_structure.doubly_linked_list import DoublyLinkedList

class LinkedDeque(DoublyLinkedList):

    def add_front(self, item):
        self.insert_at_beginning(item)

    def add_rear(self, item):
        self.insert_at_end(item)

    def remove_front(self):
        return self.remove_at_beginning()

    def remove_rear(self):
        return self.remove_at_end()

    def rear(self):
        if self.is_empty():
            raise ValueError('List is empty')
        return self._sentinel_tail.prev.data

    def front(self):
        if self.is_empty():
            raise ValueError('List is empty')
        return self._sentinel_head.next.data

    def clear_deque(self):
        self.__init__()
