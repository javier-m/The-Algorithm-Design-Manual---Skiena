from typing import Sequence


class Item:
    def __init__(self, key, content=None):
        self.key = key
        self.content = content


class Heap:
    def __init__(self, heaptype=None):
        self._container = [None] * 10000
        self._top = None
        if heaptype == 'max':
            self._comp = lambda x, y: x > y
            self.heaptype = 'max'
        else:
            self.heaptype = 'min'
            self._comp = lambda x, y: x < y

    def find_root(self):
        """O(1)"""
        if self._top is None:
            return None
        return self._container[0]

    def extract_root(self) -> Item:
        if self._top is None:
            return None
        if not self._top:
            self._top = None
            return self._container[0]
        root = self._container[0]
        # take the rightmost item as the root and bubble down
        index = 0
        item = self._container[self._top]
        self._container[index] = item
        self._top -= 1
        while 2 * index + 1 <= self._top:
            index_child_1 = 2 * index + 1
            index_child_2 = 2 * index + 2
            child_1 = self._container[index_child_1]
            child_2 = self._container[index_child_2] if index_child_2 <= self._top else None
            if self._comp(child_1.key, item.key):
                if child_2 and self._comp(child_2.key, child_1.key):
                    (self._container[index_child_2],
                     self._container[index]) = (self._container[index],
                                                self._container[index_child_2])
                    index = index_child_2
                else:
                    (self._container[index_child_1],
                     self._container[index]) = (self._container[index],
                                                self._container[index_child_1])
                    index = index_child_1
            elif child_2 and self._comp(child_2.key, item.key):
                (self._container[index_child_2],
                 self._container[index]) = (self._container[index],
                                            self._container[index_child_2])
                index = index_child_2
            else:
                break
        return root

    def insert(self, item: Item):
        """O(log n)"""
        if self._top is not None:
            # insert at last position
            self._top += 1
            index = self._top
            self._container[index] = item
            # bubble up
            while index:
                parent_index = (index - 1) // 2
                parent = self._container[parent_index]
                if self._comp(parent.key, item.key):
                    break
                (self._container[parent_index],
                 self._container[index]) = (self._container[index],
                                            self._container[parent_index])
                index = parent_index
        else:
            self._top = 0
            self._container[0] = item

    def construct(self, items: Sequence[Item]):
        """O(n)"""
        if not items:
            return
        for i, item in enumerate(items):
            self._container[i] = item
        self._top = i
        for i in range(self._top, -1, -1):
            index = i
            item = self._container[index]
            while 2 * index + 1 <= self._top:
                index_child_1 = 2 * index + 1
                index_child_2 = 2 * index + 2
                child_1 = self._container[index_child_1]
                child_2 = self._container[index_child_2] if index_child_2 <= self._top else None
                if self._comp(child_1.key, item.key):
                    if child_2 and self._comp(child_2.key, child_1.key):
                        (self._container[index_child_2],
                         self._container[index]) = (self._container[index],
                                                    self._container[index_child_2])
                        index = index_child_2
                    else:
                        (self._container[index_child_1],
                         self._container[index]) = (self._container[index],
                                                    self._container[index_child_1])
                        index = index_child_1
                elif child_2 and self._comp(child_2.key, item.key):
                    (self._container[index_child_2],
                     self._container[index]) = (self._container[index],
                                                self._container[index_child_2])
                    index = index_child_2
                else:
                    break
