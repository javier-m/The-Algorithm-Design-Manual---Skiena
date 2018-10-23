from .doubly_linked_list import DoublyLinkedList


class QueueEmptyError(Exception):
    pass


class BaseQueue:
    @property
    def head(self):
        raise NotImplementedError

    @property
    def tail(self):
        raise NotImplementedError

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

    @property
    def head(self):
        if self._first is None or self._first > self._last:
            return None
        return self._container[self._first]

    @property
    def tail(self):
        if self._first is None or self._first > self._last:
            return None
        return self._container[self._last]

    def enqueue(self, item):
        if self._first is None:
            self._first = self._last = 0
            self._container[0] = item
            return
        self._last = self._last + 1
        self._container[self._last] = item

    def dequeue(self):
        if self._first is not None:
            item = self._container[self._first]
            self._first = self._first + 1 if self._first < self._last else None
            return item
        raise QueueEmptyError


class DoublyLinkedListBasedQueue(BaseQueue):
    """Queue implementation based on linked list"""
    def __init__(self):
        self._container = DoublyLinkedList()

    @property
    def head(self):
        return self._container.tail.item

    @property
    def tail(self):
        return self._container.head.item

    def enqueue(self, item):
        self._container.insert(item)

    def dequeue(self):
        last_node = self._container.tail
        if last_node is not self._container._nil:
            item = last_node.item
            last_node.previous.next = last_node.next
            last_node.next.previous = last_node.previous
            del last_node
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

    @property
    def head(self):
        return self._queue.head

    @property
    def tail(self):
        return self._queue.tail

    def enqueue(self, item):
        self._queue.enqueue(item)

    def dequeue(self):
        return self._queue.dequeue()
