from .array import Array, _sentinel

class QueueError(Exception):
    pass

class Queue:
    def __init__(self, capacity):
        self._data = Array(capacity)
    
    def enqueue(self, value):
        if self.is_full():
            raise QueueError("queue is full")
        self._data.append(value)

        return self
    
    def dequeue(self):
        if self.is_empty():
            raise QueueError("queue is empty")

        first_value = self._data[0]
        for i in range(len(self._data)-1):
            self._data[i] = self._data[i + 1]
        self._data[i + 1] = _sentinel

        return first_value
    
    def peek(self):
        if self.is_empty():
            raise QueueError("queue is empty")
        return self._data[0]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def is_full(self):
        return len(self._data) == self._data.array_size()
    
    def __len__(self):
        return len(self._data)
    
class Circular_Queue:
    def __init__(self, capacity):
        self._data = Array(capacity)
        self._size = 0
        self._front = 0
        self._rear = 0

    def enqueue(self, value):
        if self.is_full():
            raise QueueError("queue is full")
        
        self._data[self._rear] = value
        if self._rear + 1 == self._data.array_size():
            self._rear = 0
        else:
            self._rear += 1
        self._size += 1

        return self
    
    def dequeue(self):
        if self.is_empty():
            raise QueueError("queue is empty")
        
        first_value = self._data[self._front]
        if self._front + 1 == self._data.array_size():
            self._front = 0
        else:
            self._front += 1
        self._size -= 1

        return first_value
        
    def peek(self):
        if self.is_empty():
            raise QueueError("queue is empty")
        return self._data[self._front]
    
    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._data.array_size()
    
    def __len__(self):
        return self._size
