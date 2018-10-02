import pytest

from datastructures import DoublyLinkedList


def test_insert():
    doubly_linked_list = DoublyLinkedList()
    assert doubly_linked_list.first is None
    assert doubly_linked_list.last is None
    doubly_linked_list.insert('a')
    assert doubly_linked_list.first.item == 'a'
    assert doubly_linked_list.first.previous is None
    assert doubly_linked_list.first.next is None
    assert doubly_linked_list.last.item == 'a'
    assert doubly_linked_list.last.previous is None
    assert doubly_linked_list.last.next is None
    doubly_linked_list.insert('b')
    assert doubly_linked_list.first.item == 'b'
    assert doubly_linked_list.first.previous is None
    assert doubly_linked_list.first.next.item == 'a'
    assert doubly_linked_list.last.item == 'a'
    assert doubly_linked_list.last.previous.item == 'b'
    assert doubly_linked_list.last.next is None


def test_search():
    doubly_linked_list = DoublyLinkedList()
    for i in 'abc':
        doubly_linked_list.insert(i)
    assert doubly_linked_list.search('a').item == 'a'
    assert doubly_linked_list.search('b').item == 'b'
    assert doubly_linked_list.search('c').item == 'c'


def test_search_fail():
    doubly_linked_list = DoublyLinkedList()
    for i in 'abc':
        doubly_linked_list.insert(i)
    with pytest.raises(FileNotFoundError):
        doubly_linked_list.search('d')


def test_delete():
    doubly_linked_list = DoublyLinkedList()
    for i in 'abc':
        doubly_linked_list.insert(i)
    doubly_linked_list.delete('b')
    assert doubly_linked_list.first.item == 'c'
    assert doubly_linked_list.first.previous is None
    assert doubly_linked_list.first.next.item == 'a'
    assert doubly_linked_list.last.item == 'a'
    assert doubly_linked_list.last.previous.item == 'c'
    assert doubly_linked_list.last.next is None
    doubly_linked_list.delete('a')
    assert doubly_linked_list.first.item == 'c'
    assert doubly_linked_list.first.previous is None
    assert doubly_linked_list.first.next is None
    assert doubly_linked_list.last.item == 'c'
    assert doubly_linked_list.last.previous is None
    assert doubly_linked_list.last.next is None
    doubly_linked_list.delete('c')
    assert doubly_linked_list.first is None
    assert doubly_linked_list.last is None


def test_delete_fail():
    doubly_linked_list = DoublyLinkedList()
    for i in 'abc':
        doubly_linked_list.insert(i)
    with pytest.raises(FileNotFoundError):
        doubly_linked_list.delete('d')
