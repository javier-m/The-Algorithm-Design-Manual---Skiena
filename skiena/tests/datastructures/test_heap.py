import random

from datastructures import Heap, KeyedItem


def test_insert_min_heap():
    heap = Heap()
    items = [KeyedItem(key=i) for i in range(10)]
    random_items = [item for item in items]
    random.shuffle(random_items)
    for item in random_items:
        heap.insert(item)
    for i in range(10):
        assert heap.extract_root() is items[i]
    assert heap.extract_root() is None


def test_construct_min_heap():
    heap = Heap()
    items = [KeyedItem(key=i) for i in range(10)]
    random_items = [item for item in items]
    random.shuffle(random_items)
    heap.heapify(random_items)
    for i in range(10):
        assert heap.extract_root() is items[i]
    assert heap.extract_root() is None


def test_insert_max_heap():
    heap = Heap(heaptype='max')
    items = [KeyedItem(key=i) for i in range(10)]
    random_items = [item for item in items]
    random.shuffle(random_items)
    for item in random_items:
        heap.insert(item)
    for i in range(10):
        assert heap.extract_root() is items[10 - i - 1]
    assert heap.extract_root() is None


def test_construct_max_heap():
    heap = Heap(heaptype='max')
    items = [KeyedItem(key=i) for i in range(10)]
    random_items = [item for item in items]
    random.shuffle(random_items)
    heap.heapify(random_items)
    for i in range(10):
        assert heap.extract_root() is items[10 - i - 1]
    assert heap.extract_root() is None


def test_construct_empty_heap():
    heap = Heap()
    items = []
    heap.heapify(items)
    assert heap.extract_root() is None


def test_find_root():
    heap = Heap()
    items = [KeyedItem(key=i) for i in range(10)]
    random_items = [item for item in items]
    random.shuffle(random_items)
    heap.heapify(random_items)
    assert heap.find_root() is items[0]


def test_delete_root():
    heap = Heap()
    items = [KeyedItem(key=i) for i in range(10)]
    random_items = [item for item in items]
    random.shuffle(random_items)
    heap.heapify(random_items)
    heap.delete(items[0])
    for i in range(1, 10):
        assert heap.extract_root() is items[i]
    assert heap.extract_root() is None


def test_delete_only_item():
    heap = Heap()
    item = KeyedItem(key=0)
    heap.insert(item)
    heap.delete(item)
    assert heap.extract_root() is None


def test_delete_last():
    heap = Heap()
    items = [KeyedItem(key=i) for i in range(10)]
    heap.heapify(items)
    heap.delete(items[9])
    for i in range(9):
        assert heap.extract_root() is items[i]
    assert heap.extract_root() is None


def test_delete_with_bubble_down():
    heap = Heap()
    items_keys = list(range(5)) + list(range(100, 112))
    items = [KeyedItem(key=i) for i in items_keys]
    heap.heapify(items)
    heap.delete(items[5])
    for i in range(17):
        if i != 5:
            root = heap.extract_root()
            assert root is items[i]
    assert heap.extract_root() is None


def test_delete_with_bubble_up():
    heap = Heap()
    items_keys = (list(range(2))
                  + [100]
                  + list(range(2, 4))
                  + list(range(101, 103))
                  + list(range(4, 8))
                  + list(range(103, 107))
                  + list(range(8, 10)))
    items = [KeyedItem(key=i) for i in items_keys]
    heap.heapify(items)
    heap.delete(items[5])
    for i in range(2):
        assert heap.extract_root() is items[i]
    for i in range(3, 5):
        assert heap.extract_root() is items[i]
    for i in range(7, 11):
        assert heap.extract_root() is items[i]
    for i in range(15, 17):
        assert heap.extract_root() is items[i]
    assert heap.extract_root() is items[2]
    assert heap.extract_root() is items[6]
    for i in range(11, 15):
        assert heap.extract_root() is items[i]
    assert heap.extract_root() is None
