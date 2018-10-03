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
    assert queue.head is None
    assert queue.tail is None
    queue.enqueue('a')
    assert queue.head == 'a'
    assert queue.tail == 'a'
    assert queue.dequeue() == 'a'
    assert queue.head is None
    assert queue.tail is None
    queue.enqueue('b')
    queue.enqueue('c')
    assert queue.head == 'b'
    assert queue.tail == 'c'
    assert queue.dequeue() == 'b'
    assert queue.head == 'c'
    assert queue.tail == 'c'
    queue.enqueue('d')
    assert queue.head == 'c'
    assert queue.tail == 'd'
    assert queue.dequeue() == 'c'
    assert queue.head == 'd'
    assert queue.tail == 'd'
    assert queue.dequeue() == 'd'
    assert queue.head is None
    assert queue.tail is None


def test_array_implementation_empty_queue():
    queue = Queue(implementation='array')
    with pytest.raises(QueueEmptyError):
        queue.dequeue()


def test_linked_list_implementation():
    queue = Queue(implementation='doubly_linked_list')
    assert queue.head is None
    assert queue.tail is None
    queue.enqueue('a')
    assert queue.head == 'a'
    assert queue.tail == 'a'
    assert queue.dequeue() == 'a'
    assert queue.head is None
    assert queue.tail is None
    queue.enqueue('b')
    queue.enqueue('c')
    assert queue.head == 'b'
    assert queue.tail == 'c'
    assert queue.dequeue() == 'b'
    assert queue.head == 'c'
    assert queue.tail == 'c'
    queue.enqueue('d')
    assert queue.head == 'c'
    assert queue.tail == 'd'
    assert queue.dequeue() == 'c'
    assert queue.head == 'd'
    assert queue.tail == 'd'
    assert queue.dequeue() == 'd'
    assert queue.head is None
    assert queue.tail is None


def test_linked_list_implementation_empty_queue():
    queue = Queue(implementation='doubly_linked_list')
    with pytest.raises(QueueEmptyError):
        queue.dequeue()
