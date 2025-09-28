from typing import Optional

class LinkedListError(Exception):
    pass

class Node:
    def __init__(self, data, next: Optional["Node"]=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self, value):
        self._head = Node(value)
        self._size = 1

    def append(self, value):
        end_node = self._head
        while end_node.next != None:
            end_node = end_node.next

        end_node.next = Node(value)
        self._size += 1
        return self
    
    def prepend(self, value):
        self._head = Node(value, self._head)
        self._size += 1
        return self

    def insert(self, index, value):
        if index > self._size:
            raise LinkedListError("index out of range")
        
        if index == 0:
            return self.prepend(value)

        current_node = self._head
        for _ in range(index - 1):
            current_node = current_node.next

        new_node = Node(value, current_node.next)
        current_node.next = new_node
        self._size += 1
        return self
    
    def remove(self, index):
        if self.is_empty():
            raise LinkedListError("list is empty")
        if index >= self._size:
            raise LinkedListError("index out of range")

        current_node = self._head
        if index == 0:
            self._head = self._head.next
        elif index + 1 == self._size:
            for _ in range(index - 1):
                current_node = current_node.next
            current_node.next = None
        else:
            for _ in range(index):
                current_node = current_node.next
            current_node.next = current_node.next.next

        self._size -= 1
        return self

    def find(self, value):
        current_node = self._head
        i = 0
        while current_node is not None:
            if current_node.data == value:
                return i
            current_node = current_node.next
            i += 1
        return -1
    
    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        datas = []
        current_node = self._head
        while current_node.next is not None:
            datas.append(current_node.data)
            current_node = current_node.next

        return f"{' -> '.join(map(str, datas))}"
    
li = SinglyLinkedList(1)
print(li)
li.append(2).append(3).append(4).remove(0)
li.insert(0, 1)

print(li)