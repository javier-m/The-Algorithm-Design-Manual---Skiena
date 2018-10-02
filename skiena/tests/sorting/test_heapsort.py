from sorting import heapsort
from sorting.heapsort import Item


def test_min_heapsort():
    item_0 = Item(0)
    item_1 = Item(1)
    item_2 = Item(2)
    item_3 = Item(3)
    sorted_items = [item_0, item_1, item_2, item_3]
    items = [item_2, item_1, item_3, item_0]
    assert heapsort(items) == sorted_items


def test_max_heapsort():
    item_0 = Item(0)
    item_1 = Item(1)
    item_2 = Item(2)
    item_3 = Item(3)
    sorted_items = [item_3, item_2, item_1, item_0,]
    items = [item_2, item_1, item_3, item_0]
    assert heapsort(items, order='max') == sorted_items
