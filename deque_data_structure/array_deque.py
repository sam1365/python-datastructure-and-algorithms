import math

class ArrayDeque:
    def __init__(self, initial_capacity=10, shrink_factor=4):
        self._front = 0
        self._rear = 0
        self._size = 0
        self._capacity = initial_capacity
        self._shrink_factor = shrink_factor
        self._deque = [None] * self._capacity

    def __len__(self):
        return self._size

    def add_front(self, item):
        if len(self._deque) == self._size:
            self._increase_capacity(2 * self._capacity)

        if self.is_empty():
            self._deque[self._front] = item
        else:
            self._front = (self._front - 1) % len(self._deque)
            if self._front == -1:
                self._front = self._capacity - 1
            self._deque[self._front] = item
        self._size += 1

    def add_rear(self, item):
        if len(self._deque) == self._size:
            self._increase_capacity(2 * self._capacity)

        if self.is_empty():
            self._deque[self._rear] = item
        else:
            self._rear = (self._rear + 1) % len(self._deque)
            self._deque[self._rear] = item

        self._size += 1

    def remove_front(self):
        if self.is_empty():
            raise IndexError('Empty deque')
        self._shrink()
        element = self._deque[self._front]
        if self._size == 1:
            self._front = self._rear = 0
        else:
            self._front = (self._front + 1) % len(self._deque)
        self._deque[self._front] = None
        self._size -= 1
        return element

    def remove_rear(self):
        if self.is_empty():
            raise IndexError('Empty deque')
        self._shrink()
        element = self._deque[self._rear]
        if self._size == 1:
            self._front = self._rear = 0
        else:
            self._front = (self._front - 1) % len(self._deque)
        self._deque[self._rear] = None
        self._size -= 1
        return element

    def is_empty(self):
        return self._size == 0

    def _increase_capacity(self, new_capacity):
        if len(self._deque) > new_capacity:
            raise Exception('Deque is full')

        self._set_deque(new_capacity)

    def _shrink(self):
        if self.is_empty():
            raise Exception('Deque is empty')

        if self._size < (self._capacity / self._shrink_factor):
            factor = self._shrink_factor / 2
            new_capacity = math.ceil(len(self._deque) / factor)
            self._set_deque(new_capacity)

    def _set_deque(self, new_capacity):
        old_deque = self._deque
        self._deque = [None] * new_capacity
        index = self._front
        for i in range(self._size):
            self._deque[i] = old_deque[index]
            index = (index + 1) % len(old_deque)
        self._front = 0
        self._rear = self._size - 1

    def show_deque(self):
        if self.is_empty():
            print('Empty deque')
        for i in range(0, len(self._deque)):
            print(f'[{i}]: {self._deque[i]}')

    def clear_deque(self):
        self.__init__()

    def rear(self):
        return self._deque[self._rear]

    def front(self):
        return self._deque[self._front]
