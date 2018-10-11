from sorting import radixsort
from datastructures import KeyedItem


def test_min_radixsort():
    item_1 = KeyedItem(1)
    item_11 = KeyedItem(11)
    item_2 = KeyedItem(2)
    item_22 = KeyedItem(22)
    item_3 = KeyedItem(3)
    sorted_items = [item_1, item_2, item_3, item_11, item_22]
    items = [item_22, item_1, item_11, item_2, item_3]
    assert radixsort(items) == sorted_items


def test_max_radixsort():
    item_1 = KeyedItem(1)
    item_11 = KeyedItem(11)
    item_2 = KeyedItem(2)
    item_22 = KeyedItem(22)
    item_3 = KeyedItem(3)
    sorted_items = [item_22, item_11, item_3, item_2, item_1]
    items = [item_22, item_1, item_11, item_2, item_3]
    assert radixsort(items, order='max') == sorted_items


def test_negative_numbers():
    item_1 = KeyedItem(1)
    item_11 = KeyedItem(-11)
    item_2 = KeyedItem(2)
    item_22 = KeyedItem(22)
    item_3 = KeyedItem(-3)
    sorted_items = [item_11, item_3, item_1, item_2, item_22]
    items = [item_22, item_1, item_11, item_2, item_3]
    assert radixsort(items) == sorted_items
