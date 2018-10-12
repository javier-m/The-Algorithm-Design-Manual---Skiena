import random

from sorting import heapsort
from datastructures import KeyedItem


def test_min_heapsort():
    sorted_items = [KeyedItem(key=i) for i in range(100)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert heapsort(items) == sorted_items


def test_max_heapsort():
    sorted_items = [KeyedItem(key=i) for i in range(99, -1, -1)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert heapsort(items, order='max') == sorted_items
