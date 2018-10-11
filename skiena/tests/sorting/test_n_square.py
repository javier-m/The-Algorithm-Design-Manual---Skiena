from sorting import insertion_sort
from datastructures import KeyedItem


def test_min_insertion_sort():
    item_0 = KeyedItem(0)
    item_1 = KeyedItem(1)
    item_2 = KeyedItem(2)
    item_3 = KeyedItem(3)
    sorted_items = [item_0, item_1, item_2, item_3]
    items = [item_2, item_1, item_3, item_0]
    assert insertion_sort(items) == sorted_items


def test_max_insertion_sort():
    item_0 = KeyedItem(0)
    item_1 = KeyedItem(1)
    item_2 = KeyedItem(2)
    item_3 = KeyedItem(3)
    sorted_items = [item_3, item_2, item_1, item_0]
    items = [item_2, item_1, item_3, item_0]
    assert insertion_sort(items, order='max') == sorted_items
