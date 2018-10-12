import random

from sorting import insertion_sort
from datastructures import KeyedItem


def test_min_insertion_sort():
    sorted_items = [KeyedItem(key=i) for i in range(100)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert insertion_sort(items) == sorted_items


def test_max_insertion_sort():
    sorted_items = [KeyedItem(key=i) for i in range(99, -1, -1)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert insertion_sort(items, order='max') == sorted_items
