import pytest

from datastructures import Stack, StackEmptyError


def test_primitives():
    stack = Stack()
    with pytest.raises(NotImplementedError):
        stack.push('a')
    with pytest.raises(NotImplementedError):
        stack.pop()


def test_array_implementation():
    stack = Stack(implementation='array')
    stack.push('a')
    assert stack.pop() == 'a'
    stack.push('b')
    stack.push('c')
    assert stack.pop() == 'c'
    stack.push('d')
    assert stack.pop() == 'd'
    assert stack.pop() == 'b'


def test_array_implementation_empty_stack():
    stack = Stack(implementation='array')
    with pytest.raises(StackEmptyError):
        stack.pop()


def test_linked_list_implementation():
    stack = Stack(implementation='linked_list')
    stack.push('a')
    assert stack.pop() == 'a'
    stack.push('b')
    stack.push('c')
    assert stack.pop() == 'c'
    stack.push('d')
    assert stack.pop() == 'd'
    assert stack.pop() == 'b'


def test_linked_list_implementation_empty_stack():
    stack = Stack(implementation='linked_list')
    with pytest.raises(StackEmptyError):
        stack.pop()
