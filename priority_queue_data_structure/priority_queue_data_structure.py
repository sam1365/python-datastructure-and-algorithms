from linked_list_data_structure.positional_list import PositionalList

class BasePriorityQueue:
    """
    Abstract base  class for priority queue.
    """

    class _Item:
        """
        Private class to store priority queue items.
        """

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0

class UnsortedPriorityQueue(BasePriorityQueue):
    """
    An implementation of min-oriented Priority Queue data structure
    with unsorted list.
    """

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def _find_min(self):
        """
        Find minimum  item in the priority queue.
        """

        if self.is_empty():
            raise ValueError("Priority queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def add(self, key, value):
        """
        Add a key, value pair as new item to the priority queue.
        """

        new_item = self._Item(key, value)
        self._data.add_last(new_item)

    def min(self):
        """
        Return tuple with  minimum key.
        """

        p = self._find_min()
        item =  p.element()
        return (item._key, item._value)

    def remove_min(self):
        """
        Remove item with minimum key from the priority queue
        and return tuple created  by the removed item.
        """

        p = self._find_min()
        item = self._data.remove(p)
        return (item._key, item._value)
