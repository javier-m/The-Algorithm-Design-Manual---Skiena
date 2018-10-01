from .linked_list import LinkedList


class StackEmptyError(Exception):
    pass


class BaseStack:
    def push(self, item):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError


class ArrayBasedStack(BaseStack):
    """Stack implementation based on array"""
    def __init__(self, size=10000):
        self._container = [None] * size
        self._top = None

    def push(self, item):
        self._top = self._top + 1 if self._top is not None else 0
        self._container[self._top] = item

    def pop(self):
        top = self._top
        if top is not None:
            self._top = top - 1 if top else None
            return self._container[top]
        raise StackEmptyError


class LinkedListBasedStack(BaseStack):
    """Stack implementation based on linked list"""
    def __init__(self):
        self._container = LinkedList()

    def push(self, item):
        self._container.insert(item)

    def pop(self):
        if self._container.first:
            node = self._container.first
            next_node = node.next
            self._container.first = next_node
            return node.item
        raise StackEmptyError


class Stack:
    """Stack implentation based on either array or linked list"""
    def __init__(self, implementation=None):
        if implementation == 'array':
            self._stack = ArrayBasedStack()
        elif implementation == 'linked_list':
            self._stack = LinkedListBasedStack()
        else:
            self._stack = BaseStack()
        self.implementation = implementation

    def push(self, item):
        self._stack.push(item)

    def pop(self):
        return self._stack.pop()
