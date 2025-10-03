from .array import Array, _sentinel

class DequeError(Exception):
    pass

class Deque:
    def __init__(self, capacity):
        self._data = Array(capacity)
        self._size = 0
        self._front = 0
        self._rear = 0

    def append(self, value):
        if self.is_full():
            raise DequeError("deque is full")
        
        self._data[self._rear] = value
        self._rear = (self._rear + 1) % self.deque_size()
        self._size += 1
        return self

    def append_left(self, value):
        if self.is_full():
            raise DequeError("deque is full")
        
        self._front = (self._front - 1 + self.deque_size()) % self.deque_size()
        self._data[self._front] = value
        self._size += 1
        return self

    def pop(self):
        if self.is_empty():
            raise DequeError("deque is empty")
        
        self._rear = (self._rear - 1 + self.deque_size()) % self.deque_size()
        value = self._data[self._rear]
        self._data[self._rear] = _sentinel
        self._size -= 1
        return value

    def pop_left(self):
        if self.is_empty():
            raise DequeError("deque is empty")
        
        value = self._data[self._front]
        self._data[self._front] = _sentinel
        self._front = (self._front + 1) % self.deque_size()
        self._size -= 1
        return value

    def deque_size(self):
        return self._data.array_size()

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def is_full(self):
        return self._size == self._data.array_size()