import pytest

from datastructures import Queue, QueueEmptyError


def test_primitives():
    queue = Queue()
    with pytest.raises(NotImplementedError):
        queue.head
    with pytest.raises(NotImplementedError):
        queue.tail
    with pytest.raises(NotImplementedError):
        queue.enqueue('a')
    with pytest.raises(NotImplementedError):
        queue.dequeue()


def test_array_implementation():
    queue = Queue(implementation='array')
    a, b, c, d = list('abcd')
    assert queue.head is None
    assert queue.tail is None
    queue.enqueue(a)
    assert queue.head is a
    assert queue.tail is a
    assert queue.dequeue() is a
    assert queue.head is None
    assert queue.tail is None
    queue.enqueue(b)
    queue.enqueue(c)
    assert queue.head is b
    assert queue.tail is c
    assert queue.dequeue() is b
    assert queue.head is c
    assert queue.tail is c
    queue.enqueue(d)
    assert queue.head is c
    assert queue.tail is d
    assert queue.dequeue() is c
    assert queue.head is d
    assert queue.tail is d
    assert queue.dequeue() is d
    assert queue.head is None
    assert queue.tail is None


def test_array_implementation_empty_queue():
    queue = Queue(implementation='array')
    with pytest.raises(QueueEmptyError):
        queue.dequeue()


def test_linked_list_implementation():
    queue = Queue(implementation='doubly_linked_list')
    a, b, c, d = list('abcd')
    assert queue.head is None
    assert queue.tail is None
    queue.enqueue(a)
    assert queue.head is a
    assert queue.tail is a
    assert queue.dequeue() is a
    assert queue.head is None
    assert queue.tail is None
    queue.enqueue(b)
    queue.enqueue(c)
    assert queue.head is b
    assert queue.tail is c
    assert queue.dequeue() is b
    assert queue.head is c
    assert queue.tail is c
    queue.enqueue(d)
    assert queue.head is c
    assert queue.tail is d
    assert queue.dequeue() is c
    assert queue.head is d
    assert queue.tail is d
    assert queue.dequeue() is d
    assert queue.head is None
    assert queue.tail is None


def test_linked_list_implementation_empty_queue():
    queue = Queue(implementation='doubly_linked_list')
    with pytest.raises(QueueEmptyError):
        queue.dequeue()
