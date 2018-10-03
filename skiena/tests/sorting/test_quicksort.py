from sorting import Item, quicksort


def test_min_quicksort():
    item_0 = Item(0)
    item_1 = Item(1)
    item_2 = Item(2)
    item_3 = Item(3)
    sorted_items = [item_0, item_1, item_2, item_3]
    items = [item_2, item_1, item_3, item_0]
    quicksort(items)
    assert items == sorted_items


def test_max_quicksort():
    item_0 = Item(0)
    item_1 = Item(1)
    item_2 = Item(2)
    item_3 = Item(3)
    sorted_items = [item_3, item_2, item_1, item_0]
    items = [item_2, item_1, item_3, item_0]
    quicksort(items, order='max')
    assert items == sorted_items
