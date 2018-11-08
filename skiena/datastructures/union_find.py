from typing import Sequence

from .stack import Stack, StackEmptyError


class UnionFindGroup:
    def __init__(self, leader):
        self.leader = leader
        self.size = 1
        self._items = [leader]

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        for item in self._items:
            yield item


class UnionFind:
    def __init__(self, items: Sequence):
        self._items = items
        for item in items:
            item._union_find_group = UnionFindGroup(leader=item)

    def find(self, item) -> UnionFindGroup:
        """O(1)"""
        return item._union_find_group

    def union(self, item_1, item_2):
        """O(n)"""
        large_group, small_group = self.find(item_1), self.find(item_2)
        if large_group is small_group:
            return
        if large_group.size < small_group.size:
            large_group, small_group = small_group, large_group
        large_group.size += small_group.size
        for item in small_group:
            item._union_find_group = large_group
            large_group.add(item)
        del small_group


class LazyUnionFindGroup:
    def __init__(self, item):
        self.item = item
        self.parent = self
        self.rank = 0


class LazyUnionFind:
    """
    Union by rank and path compresion
    forest-based
    m operations takes O(m*alpha(n)) in amortized times
    """
    def __init__(self, items: Sequence):
        self._items = items
        for item in items:
            item._union_find_group = LazyUnionFindGroup(item=item)

    def find(self, item) -> UnionFindGroup:
        """log(n) with path compresion"""
        stack = Stack(implementation='linked_list')
        union_find_group = item._union_find_group
        while union_find_group.parent is not union_find_group:
            stack.push(union_find_group)
            union_find_group = union_find_group.parent
        while True:
            try:
                sub_union_find_group = stack.pop()
                sub_union_find_group.parent = union_find_group
            except StackEmptyError:
                break
        return union_find_group

    def union(self, item_1, item_2):
        """log(n) with union by rank"""
        large_group, small_group = self.find(item_1), self.find(item_2)
        if large_group is small_group:
            return
        if large_group.rank == small_group.rank:
            large_group.rank += 1
        elif large_group.rank < small_group.rank:
            large_group, small_group = small_group, large_group
        small_group.parent = large_group
