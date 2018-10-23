import pytest

from datastructures import LinkedList


def test_insert():
    linked_list = LinkedList()
    a, b = list('ab')
    assert linked_list.head.item is None
    assert linked_list.tail.item is None
    linked_list.insert(a)
    assert linked_list.head.item is a
    assert linked_list.head.next.item is None
    assert linked_list.tail.item is a
    linked_list.insert(b)
    assert linked_list.head.item is b
    assert linked_list.head.next.item is a
    assert linked_list.tail.item is a


def test_search():
    linked_list = LinkedList()
    abc = a, b, c = list('abc')
    for i in abc:
        linked_list.insert(i)
    assert linked_list.search(a).item is a
    assert linked_list.search(b).item is b
    assert linked_list.search(c).item is c


def test_search_fail():
    linked_list = LinkedList()
    abc = a, b, c = list('abc')
    for i in abc:
        linked_list.insert(i)
    with pytest.raises(FileNotFoundError):
        linked_list.search('d')


def test_previous():
    linked_list = LinkedList()
    abc = a, b, c = list('abc')
    for i in abc:
        linked_list.insert(i)
    assert linked_list.previous(a).item is b
    assert linked_list.previous(b).item is c
    assert linked_list.previous(c).item is None


def test_delete():
    linked_list = LinkedList()
    abc = a, b, c = list('abc')
    for i in abc:
        linked_list.insert(i)
    linked_list.delete(b)
    assert linked_list.head.item is c
    assert linked_list.head.next.item is a
    assert linked_list.tail.item is a
    linked_list.delete(a)
    assert linked_list.head.item is c
    assert linked_list.head.next.item is None
    assert linked_list.tail.item is c
    linked_list.delete(c)
    assert linked_list.head.item is None
    assert linked_list.tail.item is None


def test_delete_fail():
    linked_list = LinkedList()
    for i in 'abc':
        linked_list.insert(i)
    with pytest.raises(FileNotFoundError):
        linked_list.delete('d')


def test_iterate():
    linked_list = LinkedList()
    for i in 'abc':
        linked_list.insert(i)
    j = -1
    for i in linked_list:
        j += 1
        assert i == 'abc'[::-1][j]
