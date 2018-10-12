from typing import Sequence

from .keyed_item import KeyedItem


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

    def extract_root(self) -> KeyedItem:
        if self._top is None:
            return None
        if not self._top:
            self._top = None
            return self._container[0]
        root = self._container[0]
        # take the rightmost item as the root and bubble down
        item = self._container[self._top]
        item._index = 0
        self._container[0] = item
        self._top -= 1
        while 2 * item._index + 1 <= self._top:
            index_child_1 = 2 * item._index + 1
            index_child_2 = 2 * item._index + 2
            child_1 = self._container[index_child_1]
            child_2 = self._container[index_child_2] if index_child_2 <= self._top else None
            if self._comp(child_1.key, item.key):
                if child_2 and self._comp(child_2.key, child_1.key):
                    (self._container[index_child_2],
                     self._container[item._index]) = (self._container[item._index],
                                                      self._container[index_child_2])
                    child_2._index, item._index = item._index, child_2._index
                else:
                    (self._container[index_child_1],
                     self._container[item._index]) = (self._container[item._index],
                                                      self._container[index_child_1])
                    child_1._index, item._index = item._index, child_1._index
            elif child_2 and self._comp(child_2.key, item.key):
                (self._container[index_child_2],
                 self._container[item._index]) = (self._container[item._index],
                                                  self._container[index_child_2])
                child_2._index, item._index = item._index, child_2._index
            else:
                break
        return root

    def insert(self, item: KeyedItem):
        """O(log n)"""
        if self._top is not None:
            # insert at last position
            self._top += 1
            self._container[self._top] = item
            item._index = self._top
            # bubble up
            while item._index:
                parent_index = (item._index - 1) // 2
                parent = self._container[parent_index]
                if self._comp(parent.key, item.key):
                    break
                (self._container[parent_index],
                 self._container[item._index]) = (self._container[item._index],
                                                  self._container[parent_index])
                parent._index, item._index = item._index, parent._index
        else:
            self._top = 0
            self._container[0] = item
            item._index = 0

    def delete(self, item: KeyedItem):
        """O(log n)"""
        # take the rightmost item and place it at the deleted item location
        rightmost_item = self._container[self._top]
        if self._top == 0:
            self._top = None
            return
        if item is rightmost_item:
            self._top -= 1
            return
        self._container[item._index] = rightmost_item
        rightmost_item._index = item._index
        self._top -= 1
        parent_index = (item._index - 1) // 2
        parent = self._container[parent_index]
        index_child_1 = 2 * rightmost_item._index + 1
        child_1 = self._container[index_child_1] if index_child_1 <= self._top else None
        index_child_2 = 2 * rightmost_item._index + 2
        child_2 = self._container[index_child_2] if index_child_2 <= self._top else None
        # compare with parent: bubble-up if necessary
        while rightmost_item._index:
            parent_index = (rightmost_item._index - 1) // 2
            parent = self._container[parent_index]
            if self._comp(parent.key, rightmost_item.key):
                break
            (self._container[parent_index],
             self._container[rightmost_item._index]) = (self._container[rightmost_item._index],
                                                        self._container[parent_index])
            parent._index, rightmost_item._index = rightmost_item._index, parent._index
        # compare with children: bubble-down if necessary
        while 2 * rightmost_item._index + 1 <= self._top:
            index_child_1 = 2 * rightmost_item._index + 1
            index_child_2 = 2 * rightmost_item._index + 2
            child_1 = self._container[index_child_1]
            child_2 = self._container[index_child_2] if index_child_2 <= self._top else None
            if self._comp(child_1.key, rightmost_item.key):
                if child_2 and self._comp(child_2.key, child_1.key):
                    (self._container[index_child_2],
                     self._container[rightmost_item._index]) = (self._container[rightmost_item._index],
                                                                self._container[index_child_2])
                    child_2._index, rightmost_item._index = rightmost_item._index, child_2._index
                else:
                    (self._container[index_child_1],
                     self._container[rightmost_item._index]) = (self._container[rightmost_item._index],
                                                                self._container[index_child_1])
                    child_1._index, rightmost_item._index = rightmost_item._index, child_1._index
            elif child_2 and self._comp(child_2.key, rightmost_item.key):
                (self._container[index_child_2],
                 self._container[rightmost_item._index]) = (self._container[rightmost_item._index],
                                                            self._container[index_child_2])
                child_2._index, rightmost_item._index = rightmost_item._index, child_2._index
            else:
                break

    def heapify(self, items: Sequence[KeyedItem]):
        """O(n)"""
        if not items:
            return
        i = -1
        for item in items:
            i += 1
            self._container[i] = item
            item._index = i
        self._top = i
        for i in range(self._top, -1, -1):
            item = self._container[i]
            while 2 * item._index + 1 <= self._top:
                index_child_1 = 2 * item._index + 1
                index_child_2 = 2 * item._index + 2
                child_1 = self._container[index_child_1]
                child_2 = self._container[index_child_2] if index_child_2 <= self._top else None
                if self._comp(child_1.key, item.key):
                    if child_2 and self._comp(child_2.key, child_1.key):
                        (self._container[index_child_2],
                         self._container[item._index]) = (self._container[item._index],
                                                          self._container[index_child_2])
                        child_2._index, item._index = item._index, child_2._index
                    else:
                        (self._container[index_child_1],
                         self._container[item._index]) = (self._container[item._index],
                                                          self._container[index_child_1])
                        child_1._index, item._index = item._index, child_1._index
                elif child_2 and self._comp(child_2.key, item.key):
                    (self._container[index_child_2],
                     self._container[item._index]) = (self._container[item._index],
                                                      self._container[index_child_2])
                    child_2._index, item._index = item._index, child_2._index
                else:
                    break
