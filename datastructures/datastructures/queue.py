from .doubly_linked_list import DoublyLinkedList


class QueueEmptyError(Exception):
    pass


class BaseQueue:
    def enqueue(self, item):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError


class ArrayBasedQueue(BaseQueue):
    """Queue implementation based on array"""
    def __init__(self, size=10000):
        self._container = [None] * size
        self._first = None
        self._last = None

    def enqueue(self, item):
        self._last = self._last + 1 if self._last is not None else 0
        self._container[self._last] = item
        # if first item to be enqueued
        if self._first is None:
            self._first = 0

    def dequeue(self):
        if (self._first is not None
           and self._first <= self._last):
            item = self._container[self._first]
            self._first += 1
            return item
        raise QueueEmptyError


class DoublyLinkedListBasedQueue(BaseQueue):
    """Queue implementation based on linked list"""
    def __init__(self):
        self._container = DoublyLinkedList()

    def enqueue(self, item):
        self._container.insert(item)

    def dequeue(self):
        last_node = self._container.last
        if last_node:
            item = last_node.item
            self._container.last = last_node.previous
            if self._container.last:
                self._container.last.next = None
            else:
                self._container.first = None
            return item
        raise QueueEmptyError


class Queue:
    """Queue implentation based on either array or linked list"""
    def __init__(self, implementation=None):
        if implementation == 'array':
            self._queue = ArrayBasedQueue()
        elif implementation == 'doubly_linked_list':
            self._queue = DoublyLinkedListBasedQueue()
        else:
            self._queue = BaseQueue()
        self.implementation = implementation

    def enqueue(self, item):
        self._queue.enqueue(item)

    def dequeue(self):
        return self._queue.dequeue()
