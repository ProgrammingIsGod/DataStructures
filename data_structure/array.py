_sentinel = object()

class Array:
    def __init__(self, capacity):
        self._capacity = capacity
        self._size = 0
        self._data = [_sentinel] * capacity

    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        self._data[index] = value
        if self._size - 1 < index:
            self._size = index + 1

    def delete(self, index):
        self._data[index] = _sentinel
        self._size -= 1

    def __len__(self):
        return self._size

    def array_size(self):
        return self._capacity

    def append(self, value):
        self._data[self._size] = value    # _size는 길이이기 때문에 인덱스로는 맨 뒤가 됨
        self._size += 1
    
    def insert(self, index, value):
        for i in range(self._capacity - 1, index, -1):
            self[i] = self[i - 1]
        self[index] = value

        if self._size + 1 > self._capacity:
            pass
        else:
            self._size += 1

    def pop(self):
        last_value = self._data[self._size - 1]
        self._data[self._size - 1] = _sentinel
        self._size -= 1
        return last_value
    
    def remove(self, index):
        for i in range(index, self._size - 1):
            self[i] = self[i + 1]
        self[i + 1] = _sentinel

        if self._size - 1 < 0:
            pass
        else:
            self._size -= 1

    def __repr__(self):
        return f"[ {', '.join("null" if data is _sentinel else str(data) for data in self._data)} ]"

