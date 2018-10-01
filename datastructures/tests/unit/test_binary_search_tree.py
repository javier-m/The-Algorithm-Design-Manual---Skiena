import pytest
import random

from datastructures import BinarySearchTree


def test_insert():
    binary_search_tree = BinarySearchTree()
    assert binary_search_tree.root is None
    binary_search_tree.insert(3)
    binary_search_tree.insert(1)
    binary_search_tree.insert(2)
    binary_search_tree.insert(0)
    binary_search_tree.insert(5)
    binary_search_tree.insert(4)
    binary_search_tree.insert(6)
    node = binary_search_tree.root
    assert (node.value, node.parent, node.left.value, node.right.value) == (3, None, 1, 5)
    node = binary_search_tree.root.left
    assert (node.value, node.parent.value, node.left.value, node.right.value) == (1, 3, 0, 2)
    node = binary_search_tree.root.left.left
    assert (node.value, node.parent.value, node.left, node.right) == (0, 1, None, None)
    node = binary_search_tree.root.left.right
    assert (node.value, node.parent.value, node.left, node.right) == (2, 1, None, None)
    node = binary_search_tree.root.right
    assert (node.value, node.parent.value, node.left.value, node.right.value) == (5, 3, 4, 6)
    node = binary_search_tree.root.right.left
    assert (node.value, node.parent.value, node.left, node.right) == (4, 5, None, None)
    node = binary_search_tree.root.right.right
    assert (node.value, node.parent.value, node.left, node.right) == (6, 5, None, None)


def test_search():
    binary_search_tree = BinarySearchTree()
    N = 10
    seq = list(range(N))
    random.shuffle(seq)
    for i in seq:
        binary_search_tree.insert(i)
    for i in range(N):
        assert binary_search_tree.search(i).value == i


def test_search_fail():
    binary_search_tree = BinarySearchTree()
    N = 10
    seq = list(range(N))
    random.shuffle(seq)
    for i in seq:
        binary_search_tree.insert(i)
    with pytest.raises(FileNotFoundError):
        binary_search_tree.search(N+1)


def test_min_max():
    binary_search_tree = BinarySearchTree()
    assert binary_search_tree.min() is None
    assert binary_search_tree.max() is None
    N = 10
    seq = list(range(N))
    random.shuffle(seq)
    for i in seq:
        binary_search_tree.insert(i)
    assert binary_search_tree.min().value == 0
    assert binary_search_tree.max().value == N-1


def test_traverse():
    binary_search_tree = BinarySearchTree()
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    N = 10
    seq = list(range(N))
    random.shuffle(seq)
    for i in seq:
        binary_search_tree.insert(i)
    binary_search_tree.traverse(action)
    assert traversed_list == list(range(N))


def test_delete_lone_root_node():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(0)
    node = binary_search_tree.search(0)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    assert traversed_list == []


def test_delete_lone_node_left_from_parent_root():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(1)
    binary_search_tree.insert(0)
    binary_search_tree.insert(2)
    node = binary_search_tree.search(0)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    parent_node = binary_search_tree.search(1)
    assert traversed_list == [1, 2]
    assert parent_node.left is None


def test_delete_lone_node_right_from_parent_root():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(1)
    binary_search_tree.insert(0)
    binary_search_tree.insert(2)
    node = binary_search_tree.search(2)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    parent_node = binary_search_tree.search(1)
    assert traversed_list == [0, 1]
    assert parent_node.right is None


def test_delete_lone_node_left_from_parent():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(3)
    binary_search_tree.insert(1)
    binary_search_tree.insert(0)
    binary_search_tree.insert(2)
    node = binary_search_tree.search(1)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    new_node = binary_search_tree.search(2)
    new_child_node = binary_search_tree.search(0)
    assert traversed_list == [0, 2, 3]
    assert binary_search_tree.root.left is new_node
    assert new_node.parent is binary_search_tree.root
    assert new_node.left is new_child_node
    assert new_child_node.parent is new_node
    assert new_node.right is None


def test_delete_lone_node_right_from_parent():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(1)
    binary_search_tree.insert(0)
    binary_search_tree.insert(3)
    binary_search_tree.insert(2)
    binary_search_tree.insert(4)
    binary_search_tree.insert(5)
    node = binary_search_tree.search(3)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    new_node = binary_search_tree.search(4)
    new_left_child_node = binary_search_tree.search(2)
    new_right_child_node = binary_search_tree.search(5)
    assert traversed_list == [0, 1, 2, 4, 5]
    assert binary_search_tree.root.right is new_node
    assert new_node.parent is binary_search_tree.root
    assert new_node.left is new_left_child_node
    assert new_left_child_node.parent is new_node
    assert new_node.right is new_right_child_node
    assert new_right_child_node.parent is new_node


def test_delete_root_node_only_left_child():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(3)
    binary_search_tree.insert(1)
    binary_search_tree.insert(2)
    binary_search_tree.insert(0)
    node = binary_search_tree.search(3)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    new_node = binary_search_tree.search(1)
    assert traversed_list == [0, 1, 2]
    assert new_node is binary_search_tree.root
    assert new_node.parent is None


def test_delete_only_left_child_left_from_parent():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(4)
    binary_search_tree.insert(3)
    binary_search_tree.insert(2)
    binary_search_tree.insert(0)
    binary_search_tree.insert(1)
    node = binary_search_tree.search(3)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    new_node = binary_search_tree.search(2)
    new_node_parent = binary_search_tree.search(4)
    assert traversed_list == [0, 1, 2, 4]
    assert new_node.parent is new_node_parent
    assert new_node_parent.left is new_node


def test_delete_only_left_child_right_from_parent():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(0)
    binary_search_tree.insert(4)
    binary_search_tree.insert(2)
    binary_search_tree.insert(1)
    binary_search_tree.insert(3)
    node = binary_search_tree.search(4)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    new_node = binary_search_tree.search(2)
    new_node_parent = binary_search_tree.search(0)
    assert traversed_list == [0, 1, 2, 3]
    assert new_node.parent is new_node_parent
    assert new_node_parent.right is new_node


def test_delete_root_node_only_right_child():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(0)
    binary_search_tree.insert(2)
    binary_search_tree.insert(1)
    binary_search_tree.insert(3)
    node = binary_search_tree.search(0)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    new_node = binary_search_tree.search(2)
    assert traversed_list == [1, 2, 3]
    assert new_node is binary_search_tree.root
    assert new_node.parent is None


def test_delete_only_right_child_left_from_parent():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(4)
    binary_search_tree.insert(0)
    binary_search_tree.insert(2)
    binary_search_tree.insert(1)
    binary_search_tree.insert(3)
    node = binary_search_tree.search(0)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    new_node = binary_search_tree.search(2)
    new_node_parent = binary_search_tree.search(4)
    assert traversed_list == [1, 2, 3, 4]
    assert new_node.parent is new_node_parent
    assert new_node_parent.left is new_node


def test_delete_only_right_child_right_from_parent():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(0)
    binary_search_tree.insert(1)
    binary_search_tree.insert(3)
    binary_search_tree.insert(2)
    binary_search_tree.insert(4)
    node = binary_search_tree.search(1)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    new_node = binary_search_tree.search(3)
    new_node_parent = binary_search_tree.search(0)
    assert traversed_list == [0, 2, 3, 4]
    assert new_node.parent is new_node_parent
    assert new_node_parent.right is new_node


def test_delete_root_node_lone_leftmost_rightsubtree_child():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(1)
    binary_search_tree.insert(0)
    binary_search_tree.insert(3)
    binary_search_tree.insert(2)
    binary_search_tree.insert(4)
    node = binary_search_tree.search(1)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    new_node = binary_search_tree.search(2)
    new_child_node = binary_search_tree.search(0)
    assert traversed_list == [0, 2, 3, 4]
    assert new_node is binary_search_tree.root
    assert new_node.parent is None
    assert new_node.left is new_child_node
    assert new_child_node.parent is new_node


def test_delete_lone_leftmost_rightsubtree_child():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(1)
    binary_search_tree.insert(0)
    binary_search_tree.insert(3)
    binary_search_tree.insert(2)
    binary_search_tree.insert(5)
    binary_search_tree.insert(4)
    binary_search_tree.insert(6)
    node = binary_search_tree.search(3)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    new_node = binary_search_tree.search(4)
    new_child_node = binary_search_tree.search(2)
    assert traversed_list == [0, 1, 2, 4, 5, 6]
    assert new_node.parent is binary_search_tree.root
    assert binary_search_tree.root.right is new_node
    assert new_node.left is new_child_node
    assert new_child_node.parent is new_node


def test_delete_root_node_leftmost_rightsubtree_child_with_right_child():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(1)
    binary_search_tree.insert(0)
    binary_search_tree.insert(4)
    binary_search_tree.insert(2)
    binary_search_tree.insert(3)
    binary_search_tree.insert(5)
    node = binary_search_tree.search(1)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    new_node = binary_search_tree.search(2)
    new_child_node = binary_search_tree.search(0)
    assert traversed_list == [0, 2, 3, 4, 5]
    assert new_node is binary_search_tree.root
    assert new_node.parent is None
    assert new_node.left is new_child_node
    assert new_child_node.parent is new_node


def test_delete_lone_leftmost_rightsubtree_child_with_right_child():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(1)
    binary_search_tree.insert(0)
    binary_search_tree.insert(3)
    binary_search_tree.insert(2)
    binary_search_tree.insert(6)
    binary_search_tree.insert(4)
    binary_search_tree.insert(5)
    binary_search_tree.insert(7)
    node = binary_search_tree.search(3)
    binary_search_tree.delete(node)
    traversed_list = []
    action = lambda node: traversed_list.append(node.value)
    binary_search_tree.traverse(action)
    new_node = binary_search_tree.search(4)
    new_left_child_node = binary_search_tree.search(2)
    new_right_child_node = binary_search_tree.search(6)
    new_left_of_right_child_node = binary_search_tree.search(5)
    assert traversed_list == [0, 1, 2, 4, 5, 6, 7]
    assert new_node.parent is binary_search_tree.root
    assert binary_search_tree.root.right is new_node
    assert new_node.left is new_left_child_node
    assert new_left_child_node.parent is new_node
    assert new_node.right is new_right_child_node
    assert new_right_child_node.parent is new_node
    assert new_right_child_node.left is new_left_of_right_child_node
    assert new_left_of_right_child_node.parent is new_right_child_node
