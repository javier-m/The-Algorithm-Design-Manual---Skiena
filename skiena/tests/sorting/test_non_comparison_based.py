import random

from sorting import radixsort, countsort, bucketsort
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


def test_negative_numbers_radixsort():
    sorted_items = [KeyedItem(key=i) for i in range(-100, 100)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert radixsort(items) == sorted_items


def test_min_countsort():
    sorted_items = [KeyedItem(key=i) for i in range(100)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert countsort(items) == sorted_items


def test_max_countsort():
    sorted_items = [KeyedItem(key=i) for i in range(99, -1, -1)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert countsort(items, order='max') == sorted_items


def test_negative_numbers_countsort():
    sorted_items = [KeyedItem(key=i) for i in range(-100, 100)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert countsort(items) == sorted_items


def test_min_bucketsort():
    sorted_items = [KeyedItem(key=i) for i in range(100)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert bucketsort(items) == sorted_items


def test_max_bucketsort():
    sorted_items = [KeyedItem(key=i) for i in range(99, -1, -1)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    assert bucketsort(items, order='max') == sorted_items
