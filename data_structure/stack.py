from .array import Array, _sentinel

class StackError(Exception):
    pass

class Stack:
    def __init__(self, capacity):
        self._data = Array(capacity)
    
    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty() == True:
            raise StackError("stack is empty")
        return self._data.pop()

    def peek(self):
        if self.is_empty() == True:
            raise StackError("stack is empty")
        return self._data[len(self._data) - 1]

    def is_empty(self):
        return len(self._data) == 0 

    def stack_size(self):
        return self._data.array_size()

    def __len__(self):
        return len(self._data)
    
