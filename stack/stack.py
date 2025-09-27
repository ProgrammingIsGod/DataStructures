from .array import Array

class StackError(Exception):
    pass

class Stack:
    def __init__(self, capacity):
        self._data = Array(capacity)
    
    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty() == True:
            raise IndexError()
        return self._data.pop()

    def peek(self):
        return self._data[len(self._data) - 1]

    def is_empty(self):
        return len(self._data) == 0 

    def __len__(self):
        return len(self._data)