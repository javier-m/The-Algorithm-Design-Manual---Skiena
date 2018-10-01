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
