import random

from sorting import quicksort
from datastructures import KeyedItem


def test_min_quicksort():
    sorted_items = [KeyedItem(key=i) for i in range(100)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    quicksort(items)
    assert items == sorted_items


def test_max_quicksort():
    sorted_items = [KeyedItem(key=i) for i in range(99, -1, -1)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    quicksort(items, order='max')
    assert items == sorted_items
