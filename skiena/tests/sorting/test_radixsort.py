import random

from sorting import radixsort
from datastructures import KeyedItem


def test_min_radixsort():
    sorted_items = [KeyedItem(key=i) for i in range(100)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert radixsort(items) == sorted_items


def test_max_radixsort():
    sorted_items = [KeyedItem(key=i) for i in range(99, -1, -1)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert radixsort(items, order='max') == sorted_items


def test_negative_numbers():
    sorted_items = [KeyedItem(key=i) for i in range(-100, 100)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert radixsort(items) == sorted_items
