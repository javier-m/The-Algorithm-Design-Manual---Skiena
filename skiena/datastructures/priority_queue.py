from .keyed_item import KeyedItem
from .binary_search_tree import BinarySearchTree
from .heap import Heap


class BasePriorityQueue:
    def insert(self, item: KeyedItem):
        raise NotImplementedError

    def find_min(self) -> KeyedItem:
        raise NotImplementedError

    def delete_min(self):
        raise NotImplementedError


class UnsortedArrayBasedPriorityQueue(BasePriorityQueue):
    """Queue implementation based on array"""
    def __init__(self, size=10000):
        self._container = [None] * size
        self._top = None
        self._item_min_index = None

    def insert(self, item: KeyedItem):
        """O(1)"""
        if self._top is None:
            self._top = 0
            self._container[0] = item
            self._item_min_index = 0
            return
        self._top += 1
        self._container[self._top] = item
        if self._container[self._item_min_index].key > item.key:
            self._item_min_index = self._top

    def find_min(self) -> KeyedItem:
        """O(1)"""
        return self._container[self._item_min_index] if self._item_min_index is not None else None

    def delete_min(self):
        """O(n)"""
        from math import inf
        if self._item_min_index is None:
            return
        if self._item_min_index != self._top:
            self._container[self._item_min_index] = self._container[self._top]
        self._top = self._top - 1 if self._top - 1 >= 0 else None
        if self._top is None:
            self._item_min_index = None
        elif not self._top:
            self._item_min_index = 0
        else:
            min_key = inf
            i = 0
            while i <= self._top:
                item = self._container[i]
                if item.key < min_key:
                    self._item_min_index = i
                    min_key = item.key
                i += 1


class SortedArrayBasedPriorityQueue(BasePriorityQueue):
    def __init__(self, size=10000):
        self._container = [None] * size
        self._top = None

    def insert(self, item: KeyedItem):
        """O(n)"""
        if self._top is None:
            self._top = 0
            self._container[0] = item
            return
        i = 0
        while i <= self._top:
            if self._container[i].key < item.key:
                break
            i += 1
        if i > self._top:
            self._top += 1
            self._container[self._top] = item
        else:
            for j in range(self._top, i-1, -1):
                self._container[j+1] = self._container[j]
            self._container[i] = item
            self._top += 1

    def find_min(self) -> KeyedItem:
        """O(1)"""
        return self._container[self._top] if self._top is not None else None

    def delete_min(self):
        """O(1)"""
        if self._top is None:
            return
        if not self._top:
            self._top = None
        else:
            self._top -= 1


class BalancedTreeBasedPriorityQueue(BasePriorityQueue):
    def __init__(self):
        self._container = BinarySearchTree()
        self._min_item = None

    def insert(self, item: KeyedItem):
        """O(log n)"""
        self._container.insert(value=item.key, content=item)
        if not self._min_item:
            self._min_item = item
            return
        if self._min_item.key > item.key:
            self._min_item = item

    def find_min(self) -> KeyedItem:
        """O(1)"""
        return self._min_item

    def delete_min(self):
        """O(log n)"""
        if self._min_item:
            min_node = self._container.min()
            self._container.delete(min_node)
            min_node = self._container.min()
            if min_node:
                self._min_item = min_node.content
            else:
                self._min_item = None


class HeapBasedPriorityQueue(BasePriorityQueue):
    def __init__(self):
        self._container = Heap(heaptype='min')

    def insert(self, item: KeyedItem):
        """O(log n)"""
        self._container.insert(item=item)

    def find_min(self) -> KeyedItem:
        """O(1)"""
        return self._container.find_root()

    def delete_min(self):
        """O(log n)"""
        self._container.extract_root()


class PriorityQueue:
    def __init__(self, implementation=None):
        if implementation == 'unsorted_array':
            self._priority_queue = UnsortedArrayBasedPriorityQueue()
        elif implementation == 'sorted_array':
            self._priority_queue = SortedArrayBasedPriorityQueue()
        elif implementation == 'balanced_tree':
            self._priority_queue = BalancedTreeBasedPriorityQueue()
        elif implementation == 'heap':
            self._priority_queue = HeapBasedPriorityQueue()
        else:
            self._priority_queue = BasePriorityQueue()
        self.implementation = implementation

    def insert(self, item: KeyedItem):
        self._priority_queue.insert(item)

    def find_min(self) -> KeyedItem:
        return self._priority_queue.find_min()

    def delete_min(self):
        self._priority_queue.delete_min()
