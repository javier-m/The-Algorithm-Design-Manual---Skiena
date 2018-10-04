from sorting import Item, radixsort


def test_min_radixsort():
    item_1 = Item(1)
    item_11 = Item(11)
    item_2 = Item(2)
    item_22 = Item(22)
    item_3 = Item(3)
    sorted_items = [item_1, item_2, item_3, item_11, item_22]
    items = [item_22, item_1, item_11, item_2, item_3]
    assert radixsort(items) == sorted_items


def test_max_radixsort():
    item_1 = Item(1)
    item_11 = Item(11)
    item_2 = Item(2)
    item_22 = Item(22)
    item_3 = Item(3)
    sorted_items = [item_22, item_11, item_3, item_2, item_1]
    items = [item_22, item_1, item_11, item_2, item_3]
    assert radixsort(items, order='max') == sorted_items


def test_negative_numbers():
    item_1 = Item(1)
    item_11 = Item(-11)
    item_2 = Item(2)
    item_22 = Item(22)
    item_3 = Item(-3)
    sorted_items = [item_11, item_3, item_1, item_2, item_22]
    items = [item_22, item_1, item_11, item_2, item_3]
    assert radixsort(items) == sorted_items
