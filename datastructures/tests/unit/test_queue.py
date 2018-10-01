import pytest

from datastructures import Queue, QueueEmptyError


def test_primitives():
    queue = Queue()
    with pytest.raises(NotImplementedError):
        queue.enqueue('a')
    with pytest.raises(NotImplementedError):
        queue.dequeue()


def test_array_implementation():
    queue = Queue(implementation='array')
    queue.enqueue('a')
    assert queue.dequeue() == 'a'
    queue.enqueue('b')
    queue.enqueue('c')
    assert queue.dequeue() == 'b'
    queue.enqueue('d')
    assert queue.dequeue() == 'c'
    assert queue.dequeue() == 'd'


def test_array_implementation_empty_queue():
    queue = Queue(implementation='array')
    with pytest.raises(QueueEmptyError):
        queue.dequeue()


def test_linked_list_implementation():
    queue = Queue(implementation='doubly_linked_list')
    queue.enqueue('a')
    assert queue.dequeue() == 'a'
    queue.enqueue('b')
    queue.enqueue('c')
    assert queue.dequeue() == 'b'
    queue.enqueue('d')
    assert queue.dequeue() == 'c'
    assert queue.dequeue() == 'd'


def test_linked_list_implementation_empty_queue():
    queue = Queue(implementation='doubly_linked_list')
    with pytest.raises(QueueEmptyError):
        queue.dequeue()
