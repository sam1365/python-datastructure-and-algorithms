import math

class ArrayQueue:
    def __init__(self, initial_capacity=10, shrink_factor=4):
        self._queue = [None] * initial_capacity
        self._size = 0
        self._front = 0
        self._rear = 0
        self._shrink_factor = shrink_factor

    def __len__(self):
        return self._size

    def enqueue(self, value):
        if len(self._queue) == self._size:
            self._increase_capacity(self._size * 2)
        if self.is_empty():
            self._queue[self._front] = value
        else:
            self._rear = (self._front + self._size) % len(self._queue)
            self._queue[self._rear] = value
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        element = self._queue[self._front]
        self._queue[self._front] = None
        self._front = (self._front + 1) % len(self._queue)
        self._size -= 1
        self._shrink()
        return element

    def peek(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._queue[self._front]

    def is_empty(self):
        return self._size == 0

    def _increase_capacity(self, new_capacity):
        if len(self._queue) > new_capacity:
            raise Exception('Queue is full')

        self._set_queue(new_capacity)

    def _shrink(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        if self._size < (len(self._queue) / self._shrink_factor):
            factor = self._shrink_factor / 2
            new_capacity = math.ceil(len(self._queue) / factor)
            self._set_queue(new_capacity)

    def _set_queue(self, new_capacity):
        old_queue = self._queue
        self._queue = [None] * new_capacity
        index = self._front
        for i in range(self._size):
            self._queue[i] = old_queue[index]
            index = (index + 1) % len(old_queue)
        self._front = 0
        self._rear = self._size - 1