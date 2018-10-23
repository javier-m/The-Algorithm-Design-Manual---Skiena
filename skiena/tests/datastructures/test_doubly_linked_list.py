import pytest

from datastructures import DoublyLinkedList


def test_insert():
    doubly_linked_list = DoublyLinkedList()
    assert doubly_linked_list.head is None
    assert doubly_linked_list.tail is None
    doubly_linked_list.insert('a')
    assert doubly_linked_list.head.item == 'a'
    assert doubly_linked_list.head.previous is None
    assert doubly_linked_list.head.next is None
    assert doubly_linked_list.tail.item == 'a'
    assert doubly_linked_list.tail.previous is None
    assert doubly_linked_list.tail.next is None
    doubly_linked_list.insert('b')
    assert doubly_linked_list.head.item == 'b'
    assert doubly_linked_list.head.previous is None
    assert doubly_linked_list.head.next.item == 'a'
    assert doubly_linked_list.tail.item == 'a'
    assert doubly_linked_list.tail.previous.item == 'b'
    assert doubly_linked_list.tail.next is None


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
    assert doubly_linked_list.head.item == 'c'
    assert doubly_linked_list.head.previous is None
    assert doubly_linked_list.head.next.item == 'a'
    assert doubly_linked_list.tail.item == 'a'
    assert doubly_linked_list.tail.previous.item == 'c'
    assert doubly_linked_list.tail.next is None
    doubly_linked_list.delete('a')
    assert doubly_linked_list.head.item == 'c'
    assert doubly_linked_list.head.previous is None
    assert doubly_linked_list.head.next is None
    assert doubly_linked_list.tail.item == 'c'
    assert doubly_linked_list.tail.previous is None
    assert doubly_linked_list.tail.next is None
    doubly_linked_list.delete('c')
    assert doubly_linked_list.head is None
    assert doubly_linked_list.tail is None


def test_delete_fail():
    doubly_linked_list = DoublyLinkedList()
    for i in 'abc':
        doubly_linked_list.insert(i)
    with pytest.raises(FileNotFoundError):
        doubly_linked_list.delete('d')
