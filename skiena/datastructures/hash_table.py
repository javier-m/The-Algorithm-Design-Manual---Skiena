from functools import reduce

from .linked_list import LinkedList


ALPHA = 10


class Item:
    def __init__(self, key: int, content, m):
        self.key = key
        self.content = content
        self._hash = reduce(
            lambda acc, x: ALPHA ** (len(str(key)) - 1 + x[0]) * int(x[1]),
            enumerate(str(key))) % m

    @property
    def hash(self) -> int:
        return self._hash


class HashTable:
    def __init__(self, m: int=31):
        self._container = [LinkedList() for i in range(m)]
        self._m = m

    def search(self, key) -> Item:
        """O(n/m) expected - O(n) worst case"""
        raise NotImplementedError

    def insert(self, item: Item):
        """O(1)"""
        item = Item(key=item.key, content=item.content, m=self._m)
        self._container[item.hash].insert(item)
        item.node = self._container[item.hash].head

    def delete(self, item: Item):
        """O(1)"""
        self._container[item.hash].delete(item.node)

    def max(self) -> Item:
        """O(n+m)"""
        """retrieve item with the largest key"""
        raise NotImplementedError

    def min(self) -> Item:
        """O(n+m)"""
        """retrieve item with the smallest key"""
        raise NotImplementedError

    def predecessor(self, item: Item) -> Item:
        """O(n+m)"""
        """retrieve the item whose key is immediately before"""
        raise NotImplementedError

    def successor(self, item: Item) -> Item:
        """O(n+m)"""
        """retrieve the item whose key is immediately after"""
        raise NotImplementedError