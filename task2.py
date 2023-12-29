"""
На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
 Объяснить плюсы и минусы каждой реализации.

"""
"""
1. Списки слишком медленные для этой задачи, так как вставка и удаление элемента с начала требует сдвига всех
прочих элементов по одному, на это уходит О(n) времени.

"""


class My_queue:

    def __init__(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def add(self, value):
        self.elements.append(value)

    def get(self):
        if len(self.elements) == 0:
            raise IndexError
        return self.elements.pop(0)


"""
    2. Использовал связанные списки. Здесь работает все за константное время 
    enqueue O(1)
    dequeue O(1)
    peek O(1)
    size O(1)
"""

from abc import ABC, abstractmethod


class Iqueue(ABC):

    @abstractmethod
    def enqueue(self):
        raise NotImplementedError

    @abstractmethod
    def dequeue(self):
        raise NotImplementedError

    @abstractmethod
    def peek(self):
        raise NotImplementedError

    @abstractmethod
    def size(self):
        raise NotImplementedError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class FIFOQueue(Iqueue):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, item):
        if self.size == 0:
            node = Node(
                value=item
            )
            self.tail = self.head = node
        else:

            self.tail.next = Node(value=item)
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError
        node = self.head
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return node.value

    def peek(self):
        if self.size == 0:
            raise IndexError
        return self.head.value

    def size(self):
        return self.size
