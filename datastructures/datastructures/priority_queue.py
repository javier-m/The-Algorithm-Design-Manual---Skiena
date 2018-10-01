class Item:
    def __init__(self, key, content):
        self.key = key
        self.content = content


class BasePriorityQueue:
    def insert(self, item: Item):
        raise NotImplementedError

    def find_min(self) -> Item:
        raise NotImplementedError

    def delete_min(self):
        raise NotImplementedError


class UnsortedArrayBasedPriorityQueue(BasePriorityQueue):
    """Queue implementation based on array"""
    def __init__(self, size=10000):
        self._container = [None] * size
        self._top = None
        self._item_min_index = None

    def insert(self, item: Item):
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

    def find_min(self) -> Item:
        """O(1)"""
        return self._container[self._item_min_index] if self._item_min_index is not None else None

    def delete_min(self):
        """O(n)"""
        from math import inf
        if self._item_min_index is None:
            return
        if self._item_min_index != self._top:
            self._container[self._item_min_index] = self._container[self._top]
        self._top -= 1
        min_key = inf
        for i, item in enumerate(self._container):
            if item.key < min_key:
                self._item_min_index = i
                min_key = item.key


class SortedArrayBasedPriorityQueue(BasePriorityQueue):
    def __init__(self, size=10000):
        self._container = [None] * size
        self._top = None

    def insert(self, item: Item):
        """O(n)"""
        if self._top is None:
            self._top = 0
            self._container[0] = item
            return
        i = 0
        while i <= self._top:
            if self._container[i].key > item.key:
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

    def find_min(self) -> Item:
        """O(1)"""
        return self._container[self._top]

    def delete_min(self):
        """O(1)"""
        if self._top is None:
            return
        if not self._top:
            self._top = None
        else:
            self._top -= 1


class BalancedTreeBasedPriorityQueue(BasePriorityQueue):
    pass


class PriorityQueue:
    def __init__(self, implementation):
        if implementation == 'unsorted_array':
            self._priority_queue = UnsortedArrayBasedPriorityQueue()
        elif implementation == 'sorted_array':
            self._priority_queue = SortedArrayBasedPriorityQueue()
        elif implementation == 'balanced_tree':
            self._priority_queue = BalancedTreeBasedPriorityQueue()
        else:
            self._priority_queue = BasePriorityQueue()
        self.implementation = implementation

    def insert(self, item: Item):
        self._priority_queue.insert(item)

    def find_min(self):
        return self._priority_queue.find_min()

    def delete_min(self):
        self._priority_queue.delete_min()
