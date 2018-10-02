import pytest

from datastructures import Dictionnary
from datastructures.dictionnary import Item


def test_primitives():
    dictionnary = Dictionnary()
    with pytest.raises(NotImplementedError):
        dictionnary.search(key=0)
    with pytest.raises(NotImplementedError):
        dictionnary.insert(Item(0, 0))
    with pytest.raises(NotImplementedError):
        dictionnary.delete(Item(0, 0))
    with pytest.raises(NotImplementedError):
        dictionnary.max()
    with pytest.raises(NotImplementedError):
        dictionnary.min()
    with pytest.raises(NotImplementedError):
        dictionnary.predecessor(Item(0, 0))
    with pytest.raises(NotImplementedError):
        dictionnary.successor(Item(0, 0))


def test_search_unsorted_array():
    dictionnary = Dictionnary(implementation='unsorted_array')
    item = Item(key=0, content=0)
    dictionnary.insert(item)
    assert dictionnary.search(key=0) is item


def test_search_fail_empty_unsorted_array():
    dictionnary = Dictionnary(implementation='unsorted_array')
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=0)


def test_search_fail_unsorted_array():
    dictionnary = Dictionnary(implementation='unsorted_array')
    item = Item(key=0, content=0)
    dictionnary.insert(item)
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=1)


def test_min_max_unsorted_array():
    dictionnary = Dictionnary(implementation='unsorted_array')
    assert dictionnary.min() is None
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.min() is item_0
    assert dictionnary.max() is item_3


def test_predecessor_successor_unsorted_array():
    dictionnary = Dictionnary(implementation='unsorted_array')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.predecessor(item_0) is None
    assert dictionnary.predecessor(item_1) is item_0
    assert dictionnary.predecessor(item_2) is item_1
    assert dictionnary.predecessor(item_3) is item_2
    assert dictionnary.successor(item_0) is item_1
    assert dictionnary.successor(item_1) is item_2
    assert dictionnary.successor(item_2) is item_3
    assert dictionnary.successor(item_3) is None


def test_delete_unsorted_array():
    dictionnary = Dictionnary(implementation='unsorted_array')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    dictionnary.delete(item_0)
    assert dictionnary.min() is item_1
    dictionnary.delete(item_1)
    assert dictionnary.min() is item_2
    dictionnary.delete(item_3)
    assert dictionnary.max() is item_2
    dictionnary.delete(item_2)
    assert dictionnary.min() is None
    assert dictionnary.max() is None


def test_search_sorted_array():
    dictionnary = Dictionnary(implementation='sorted_array')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    item_4 = Item(key=4, content=4)
    dictionnary.insert(item_0)
    assert dictionnary.search(key=0) is item_0
    dictionnary.insert(item_3)
    dictionnary.insert(item_1)
    dictionnary.insert(item_4)
    dictionnary.insert(item_2)
    assert dictionnary.search(key=0) is item_0
    assert dictionnary.search(key=1) is item_1
    assert dictionnary.search(key=2) is item_2
    assert dictionnary.search(key=3) is item_3
    assert dictionnary.search(key=4) is item_4


def test_search_fail_empty_sorted_array():
    dictionnary = Dictionnary(implementation='sorted_array')
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=0)


def test_search_fail_sorted_array():
    dictionnary = Dictionnary(implementation='sorted_array')
    item = Item(key=0, content=0)
    dictionnary.insert(item)
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=1)


def test_min_max_sorted_array():
    dictionnary = Dictionnary(implementation='sorted_array')
    assert dictionnary.min() is None
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.min() is item_0
    assert dictionnary.max() is item_3


def test_predecessor_successor_sorted_array():
    dictionnary = Dictionnary(implementation='sorted_array')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.predecessor(item_0) is None
    assert dictionnary.predecessor(item_1) is item_0
    assert dictionnary.predecessor(item_2) is item_1
    assert dictionnary.predecessor(item_3) is item_2
    assert dictionnary.successor(item_0) is item_1
    assert dictionnary.successor(item_1) is item_2
    assert dictionnary.successor(item_2) is item_3
    assert dictionnary.successor(item_3) is None


def test_delete_sorted_array():
    dictionnary = Dictionnary(implementation='sorted_array')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    dictionnary.delete(item_0)
    assert dictionnary.min() is item_1
    dictionnary.delete(item_1)
    assert dictionnary.min() is item_2
    dictionnary.delete(item_3)
    assert dictionnary.max() is item_2
    dictionnary.delete(item_2)
    assert dictionnary.min() is None
    assert dictionnary.max() is None


def test_search_singly_unsorted():
    dictionnary = Dictionnary(implementation='singly_unsorted')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    item_4 = Item(key=4, content=4)
    dictionnary.insert(item_0)
    assert dictionnary.search(key=0) is item_0
    dictionnary.insert(item_3)
    dictionnary.insert(item_1)
    dictionnary.insert(item_4)
    dictionnary.insert(item_2)
    assert dictionnary.search(key=0) is item_0
    assert dictionnary.search(key=1) is item_1
    assert dictionnary.search(key=2) is item_2
    assert dictionnary.search(key=3) is item_3
    assert dictionnary.search(key=4) is item_4


def test_search_fail_empty_singly_unsorted():
    dictionnary = Dictionnary(implementation='singly_unsorted')
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=0)


def test_search_fail_singly_unsorted():
    dictionnary = Dictionnary(implementation='singly_unsorted')
    item = Item(key=0, content=0)
    dictionnary.insert(item)
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=1)


def test_min_max_singly_unsorted():
    dictionnary = Dictionnary(implementation='singly_unsorted')
    assert dictionnary.min() is None
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.min() is item_0
    assert dictionnary.max() is item_3


def test_predecessor_successor_singly_unsorted():
    dictionnary = Dictionnary(implementation='singly_unsorted')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.predecessor(item_0) is None
    assert dictionnary.predecessor(item_1) is item_0
    assert dictionnary.predecessor(item_2) is item_1
    assert dictionnary.predecessor(item_3) is item_2
    assert dictionnary.successor(item_0) is item_1
    assert dictionnary.successor(item_1) is item_2
    assert dictionnary.successor(item_2) is item_3
    assert dictionnary.successor(item_3) is None


def test_delete_singly_unsorted():
    dictionnary = Dictionnary(implementation='singly_unsorted')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    dictionnary.delete(item_0)
    assert dictionnary.min() is item_1
    dictionnary.delete(item_1)
    assert dictionnary.min() is item_2
    dictionnary.delete(item_3)
    assert dictionnary.max() is item_2
    dictionnary.delete(item_2)
    assert dictionnary.min() is None
    assert dictionnary.max() is None


def test_search_doubly_unsorted():
    dictionnary = Dictionnary(implementation='doubly_unsorted')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    item_4 = Item(key=4, content=4)
    dictionnary.insert(item_0)
    assert dictionnary.search(key=0) is item_0
    dictionnary.insert(item_3)
    dictionnary.insert(item_1)
    dictionnary.insert(item_4)
    dictionnary.insert(item_2)
    assert dictionnary.search(key=0) is item_0
    assert dictionnary.search(key=1) is item_1
    assert dictionnary.search(key=2) is item_2
    assert dictionnary.search(key=3) is item_3
    assert dictionnary.search(key=4) is item_4


def test_search_fail_empty_doubly_unsorted():
    dictionnary = Dictionnary(implementation='doubly_unsorted')
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=0)


def test_search_fail_doubly_unsorted():
    dictionnary = Dictionnary(implementation='doubly_unsorted')
    item = Item(key=0, content=0)
    dictionnary.insert(item)
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=1)


def test_min_max_doubly_unsorted():
    dictionnary = Dictionnary(implementation='doubly_unsorted')
    assert dictionnary.min() is None
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.min() is item_0
    assert dictionnary.max() is item_3


def test_predecessor_successor_doubly_unsorted():
    dictionnary = Dictionnary(implementation='doubly_unsorted')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.predecessor(item_0) is None
    assert dictionnary.predecessor(item_1) is item_0
    assert dictionnary.predecessor(item_2) is item_1
    assert dictionnary.predecessor(item_3) is item_2
    assert dictionnary.successor(item_0) is item_1
    assert dictionnary.successor(item_1) is item_2
    assert dictionnary.successor(item_2) is item_3
    assert dictionnary.successor(item_3) is None


def test_delete_doubly_unsorted():
    dictionnary = Dictionnary(implementation='doubly_unsorted')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    dictionnary.delete(item_0)
    assert dictionnary.min() is item_1
    dictionnary.delete(item_1)
    assert dictionnary.min() is item_2
    dictionnary.delete(item_3)
    assert dictionnary.max() is item_2
    dictionnary.delete(item_2)
    assert dictionnary.min() is None
    assert dictionnary.max() is None


def test_search_singly_sorted():
    dictionnary = Dictionnary(implementation='singly_sorted')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    item_4 = Item(key=4, content=4)
    dictionnary.insert(item_0)
    assert dictionnary.search(key=0) is item_0
    dictionnary.insert(item_3)
    dictionnary.insert(item_1)
    dictionnary.insert(item_4)
    dictionnary.insert(item_2)
    assert dictionnary.search(key=0) is item_0
    assert dictionnary.search(key=1) is item_1
    assert dictionnary.search(key=2) is item_2
    assert dictionnary.search(key=3) is item_3
    assert dictionnary.search(key=4) is item_4


def test_search_fail_empty_singly_sorted():
    dictionnary = Dictionnary(implementation='singly_sorted')
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=0)


def test_search_fail_singly_sorted():
    dictionnary = Dictionnary(implementation='singly_sorted')
    item = Item(key=0, content=0)
    dictionnary.insert(item)
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=1)


def test_min_max_singly_sorted():
    dictionnary = Dictionnary(implementation='singly_sorted')
    assert dictionnary.min() is None
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.min() is item_0
    assert dictionnary.max() is item_3


def test_predecessor_successor_singly_sorted():
    dictionnary = Dictionnary(implementation='singly_sorted')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.predecessor(item_0) is None
    assert dictionnary.predecessor(item_1) is item_0
    assert dictionnary.predecessor(item_2) is item_1
    assert dictionnary.predecessor(item_3) is item_2
    assert dictionnary.successor(item_0) is item_1
    assert dictionnary.successor(item_1) is item_2
    assert dictionnary.successor(item_2) is item_3
    assert dictionnary.successor(item_3) is None


def test_delete_singly_sorted():
    dictionnary = Dictionnary(implementation='singly_sorted')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    dictionnary.delete(item_0)
    assert dictionnary.min() is item_1
    dictionnary.delete(item_1)
    assert dictionnary.min() is item_2
    dictionnary.delete(item_3)
    assert dictionnary.max() is item_2
    dictionnary.delete(item_2)
    assert dictionnary.min() is None
    assert dictionnary.max() is None


def test_search_doubly_sorted():
    dictionnary = Dictionnary(implementation='doubly_sorted')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    item_4 = Item(key=4, content=4)
    dictionnary.insert(item_0)
    assert dictionnary.search(key=0) is item_0
    dictionnary.insert(item_3)
    dictionnary.insert(item_1)
    dictionnary.insert(item_4)
    dictionnary.insert(item_2)
    assert dictionnary.search(key=0) is item_0
    assert dictionnary.search(key=1) is item_1
    assert dictionnary.search(key=2) is item_2
    assert dictionnary.search(key=3) is item_3
    assert dictionnary.search(key=4) is item_4


def test_search_fail_empty_doubly_sorted():
    dictionnary = Dictionnary(implementation='doubly_sorted')
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=0)


def test_search_fail_doubly_sorted():
    dictionnary = Dictionnary(implementation='doubly_sorted')
    item = Item(key=0, content=0)
    dictionnary.insert(item)
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=1)


def test_min_max_doubly_sorted():
    dictionnary = Dictionnary(implementation='doubly_sorted')
    assert dictionnary.min() is None
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.min() is item_0
    assert dictionnary.max() is item_3


def test_predecessor_successor_doubly_sorted():
    dictionnary = Dictionnary(implementation='doubly_sorted')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.predecessor(item_0) is None
    assert dictionnary.predecessor(item_1) is item_0
    assert dictionnary.predecessor(item_2) is item_1
    assert dictionnary.predecessor(item_3) is item_2
    assert dictionnary.successor(item_0) is item_1
    assert dictionnary.successor(item_1) is item_2
    assert dictionnary.successor(item_2) is item_3
    assert dictionnary.successor(item_3) is None


def test_delete_doubly_sorted():
    dictionnary = Dictionnary(implementation='doubly_sorted')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    dictionnary.delete(item_0)
    assert dictionnary.min() is item_1
    dictionnary.delete(item_1)
    assert dictionnary.min() is item_2
    dictionnary.delete(item_3)
    assert dictionnary.max() is item_2
    dictionnary.delete(item_2)
    assert dictionnary.min() is None
    assert dictionnary.max() is None


def test_search_balanced_tree():
    dictionnary = Dictionnary(implementation='balanced_tree')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    item_4 = Item(key=4, content=4)
    dictionnary.insert(item_0)
    assert dictionnary.search(key=0) is item_0
    dictionnary.insert(item_3)
    dictionnary.insert(item_1)
    dictionnary.insert(item_4)
    dictionnary.insert(item_2)
    assert dictionnary.search(key=0) is item_0
    assert dictionnary.search(key=1) is item_1
    assert dictionnary.search(key=2) is item_2
    assert dictionnary.search(key=3) is item_3
    assert dictionnary.search(key=4) is item_4


def test_search_fail_empty_balanced_tree():
    dictionnary = Dictionnary(implementation='balanced_tree')
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=0)


def test_search_fail_balanced_tree():
    dictionnary = Dictionnary(implementation='balanced_tree')
    item = Item(key=0, content=0)
    dictionnary.insert(item)
    with pytest.raises(FileNotFoundError):
        dictionnary.search(key=1)


def test_min_max_balanced_tree():
    dictionnary = Dictionnary(implementation='balanced_tree')
    assert dictionnary.min() is None
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.min() is item_0
    assert dictionnary.max() is item_3


def test_predecessor_successor_balanced_tree():
    dictionnary = Dictionnary(implementation='balanced_tree')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    assert dictionnary.predecessor(item_0) is None
    assert dictionnary.predecessor(item_1) is item_0
    assert dictionnary.predecessor(item_2) is item_1
    assert dictionnary.predecessor(item_3) is item_2
    assert dictionnary.successor(item_0) is item_1
    assert dictionnary.successor(item_1) is item_2
    assert dictionnary.successor(item_2) is item_3
    assert dictionnary.successor(item_3) is None


def test_delete_balanced_tree():
    dictionnary = Dictionnary(implementation='balanced_tree')
    item_0 = Item(key=0, content=0)
    item_1 = Item(key=1, content=1)
    item_2 = Item(key=2, content=2)
    item_3 = Item(key=3, content=3)
    dictionnary.insert(item_0)
    dictionnary.insert(item_1)
    dictionnary.insert(item_2)
    dictionnary.insert(item_3)
    dictionnary.delete(item_0)
    assert dictionnary.min() is item_1
    dictionnary.delete(item_1)
    assert dictionnary.min() is item_2
    dictionnary.delete(item_3)
    assert dictionnary.max() is item_2
    dictionnary.delete(item_2)
    assert dictionnary.min() is None
    assert dictionnary.max() is None
