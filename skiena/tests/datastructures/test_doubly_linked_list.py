import pytest

from datastructures import DoublyLinkedList


def test_insert():
    doubly_linked_list = DoublyLinkedList()
    a, b = list('ab')
    assert doubly_linked_list.head.item is None
    assert doubly_linked_list.tail.item is None
    doubly_linked_list.insert(a)
    assert doubly_linked_list.head.item is a
    assert doubly_linked_list.head.previous.item is None
    assert doubly_linked_list.head.next.item is None
    assert doubly_linked_list.tail.item is a
    assert doubly_linked_list.tail.previous.item is None
    assert doubly_linked_list.tail.next.item is None
    doubly_linked_list.insert(b)
    assert doubly_linked_list.head.item is b
    assert doubly_linked_list.head.previous.item is None
    assert doubly_linked_list.head.next.item is a
    assert doubly_linked_list.tail.item is a
    assert doubly_linked_list.tail.previous.item is b
    assert doubly_linked_list.tail.next.item is None


def test_search():
    doubly_linked_list = DoublyLinkedList()
    abc = a, b, c = list('abc')
    for i in abc:
        doubly_linked_list.insert(i)
    assert doubly_linked_list.search(a).item is a
    assert doubly_linked_list.search(b).item is b
    assert doubly_linked_list.search(c).item is c


def test_search_fail():
    doubly_linked_list = DoublyLinkedList()
    for i in 'abc':
        doubly_linked_list.insert(i)
    with pytest.raises(FileNotFoundError):
        doubly_linked_list.search('d')


def test_delete():
    doubly_linked_list = DoublyLinkedList()
    abc = a, b, c = list('abc')
    for i in abc:
        doubly_linked_list.insert(i)
    doubly_linked_list.delete(b)
    assert doubly_linked_list.head.item is c
    assert doubly_linked_list.head.previous.item is None
    assert doubly_linked_list.head.next.item is a
    assert doubly_linked_list.tail.item is a
    assert doubly_linked_list.tail.previous.item is c
    assert doubly_linked_list.tail.next.item is None
    doubly_linked_list.delete(a)
    assert doubly_linked_list.head.item is c
    assert doubly_linked_list.head.previous.item is None
    assert doubly_linked_list.head.next.item is None
    assert doubly_linked_list.tail.item is c
    assert doubly_linked_list.tail.previous.item is None
    assert doubly_linked_list.tail.next.item is None
    doubly_linked_list.delete(c)
    assert doubly_linked_list.head.item is None
    assert doubly_linked_list.tail.item is None


def test_delete_fail():
    doubly_linked_list = DoublyLinkedList()
    for i in 'abc':
        doubly_linked_list.insert(i)
    with pytest.raises(FileNotFoundError):
        doubly_linked_list.delete('d')
