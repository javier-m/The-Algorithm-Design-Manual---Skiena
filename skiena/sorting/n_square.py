from typing import Sequence
from .item import Item


def insertion_sort(items: Sequence[Item], order=None) -> Sequence[Item]:
    """O(n**2) but can be fast if the inputs are *almost* sorted"""
    comp = lambda x, y: x > y if order == 'max' else x < y
    for i in range(1, len(items)):
        j = i
        while not comp(items[j - 1].key, items[j].key):
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1
            if not j:
                break
    return items
