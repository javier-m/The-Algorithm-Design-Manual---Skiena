from math import inf

from .keyed_item import KeyedItem
from .linked_list import LinkedList, LinkedListNode
from .doubly_linked_list import DoublyLinkedList, DoublyLinkedListNode
from .binary_search_tree import BinarySearchTree


class BaseDictionnary:
    def search(self, key) -> KeyedItem:
        """Given a search key, return a pointer to the element in dic-
        tionary self whose key value is k, if one exists."""
        raise NotImplementedError

    def insert(self, item: KeyedItem):
        raise NotImplementedError

    def delete(self, item: KeyedItem):
        raise NotImplementedError

    def max(self) -> KeyedItem:
        """retrieve item with the largest key"""
        raise NotImplementedError

    def min(self) -> KeyedItem:
        """retrieve item with the smallest key"""
        raise NotImplementedError

    def predecessor(self, item: KeyedItem) -> KeyedItem:
        """retrieve the item whose key is immediately before"""
        raise NotImplementedError

    def successor(self, item: KeyedItem) -> KeyedItem:
        """retrieve the item whose key is immediately after"""
        raise NotImplementedError


class UnsortedArrayBasedDictionnary(BaseDictionnary):
    def __init__(self, size: int=10000):
        self._container = [None] * size
        self._top = None

    def search(self, key) -> KeyedItem:
        """O(n)"""
        if self._top is not None:
            for i in range(self._top + 1):
                item = self._container[i]
                if item.key == key:
                    return item
            raise FileNotFoundError
        raise FileNotFoundError

    def insert(self, item: KeyedItem):
        """O(1)"""
        self._top = self._top + 1 if self._top is not None else 0
        item._index = self._top
        self._container[self._top] = item

    def delete(self, item: KeyedItem):
        """O(n)"""
        if self._top is not None:
            self._container[item._index] = self._container[self._top]
            self._container[item._index]._index = item._index
            self._top = self._top - 1 if self._top else None
            return

    def max(self) -> KeyedItem:
        """O(n)"""
        from math import inf
        if self._top is not None:
            max_key = -inf
            max_item = None
            i = 0
            for i in range(self._top + 1):
                item = self._container[i]
                if item.key > max_key:
                    max_item, max_key = item, item.key
            return max_item
        return None

    def min(self) -> KeyedItem:
        """O(n)"""
        from math import inf
        if self._top is not None:
            min_key = inf
            min_item = None
            i = 0
            for i in range(self._top + 1):
                item = self._container[i]
                if item.key < min_key:
                    min_item, min_key = item, item.key
            return min_item
        return None

    def predecessor(self, item: KeyedItem) -> KeyedItem:
        """O(n)"""
        key = item.key
        predecessor = None
        predecessor_key = -inf
        for i in range(self._top + 1):
            current_item = self._container[i]
            current_key = current_item.key
            if predecessor_key < current_key < key:
                predecessor, predecessor_key = current_item, current_key
        return predecessor

    def successor(self, item: KeyedItem) -> KeyedItem:
        """O(n)"""
        key = item.key
        successor = None
        successor_key = inf
        for i in range(self._top + 1):
            current_item = self._container[i]
            current_key = current_item.key
            if successor_key > current_key > key:
                successor, successor_key = current_item, current_key
        return successor


class SortedArrayBasedDictionnary(BaseDictionnary):
    def __init__(self, size: int=10000):
        self._container = [None] * size
        self._top = None

    def search(self, key) -> KeyedItem:
        """O(log n)"""
        if self._top is not None:
            min_i = 0
            max_i = self._top
            if not max_i and self._container[max_i].key == key:
                return self._container[max_i]
            while min_i < max_i:
                min_key = self._container[min_i].key
                max_key = self._container[max_i].key
                median_i = (max_i + min_i) // 2
                median_key = self._container[median_i].key
                if min_key == key:
                    return self._container[min_i]
                if max_key == key:
                    return self._container[max_i]
                if median_key == key:
                    return self._container[median_i]
                if median_key < key:
                    min_i = median_i
                else:
                    max_i = median_i
            raise FileNotFoundError
        raise FileNotFoundError

    def insert(self, item: KeyedItem):
        """O(n)"""
        if self._top is not None:
            i = 0
            key = item.key
            while i < self._top + 1:
                current_key = self._container[i].key
                if current_key > key:
                    break
                i += 1
            for j in range(self._top, i - 1, -1):
                self._container[j + 1] = self._container[j]
                self._container[j + 1]._index = j + 1
            item._index = i
            self._container[i] = item
            self._top += 1
        else:
            self._top = 0
            self._container[0] = item
            item._index = 0

    def delete(self, item: KeyedItem):
        """O(n)"""
        for i in range(item._index + 1, self._top + 1):
            self._container[i - 1] = self._container[i]
            self._container[i - 1]._index = i - 1
        self._top = self._top - 1 if self._top else None

    def max(self) -> KeyedItem:
        """O(1)"""
        if self._top is not None:
            return self._container[self._top]
        return None

    def min(self) -> KeyedItem:
        """O(1)"""
        if self._top is not None:
            return self._container[0]
        return None

    def predecessor(self, item: KeyedItem) -> KeyedItem:
        """O(1)"""
        index = item._index
        if index:
            return self._container[index - 1]
        return None

    def successor(self, item: KeyedItem) -> KeyedItem:
        """O(1)"""
        index = item._index
        if index < self._top:
            return self._container[index + 1]
        return None


class SinglyUnsortedBasedDictionnary(BaseDictionnary):
    def __init__(self):
        self._container = LinkedList()

    def search(self, key) -> KeyedItem:
        """O(n)"""
        node = self._container.head
        while node:
            if node.item.key == key:
                return node.item
            node = node.next
        raise FileNotFoundError

    def insert(self, item: KeyedItem):
        """O(1)"""
        self._container.insert(item)

    def delete(self, item: KeyedItem):
        """O(n)"""
        key = item.key
        previous_node = None
        item_node = self._container.head
        while item_node:
            if item_node.item.key == key:
                break
            previous_node, item_node = item_node, item_node.next
        if previous_node:
            previous_node.next = item_node.next
        else:
            self._container.head = item_node.next
        if not item_node.next:
            self._container.tail = previous_node

    def max(self) -> KeyedItem:
        """O(n)"""
        from math import inf
        max_key = -inf
        max_item = None
        node = self._container.head
        while node:
            if node.item.key > max_key:
                max_key = node.item.key
                max_item = node.item
            node = node.next
        return max_item

    def min(self) -> KeyedItem:
        """O(n)"""
        from math import inf
        min_key = inf
        min_item = None
        node = self._container.head
        while node:
            if node.item.key < min_key:
                min_key = node.item.key
                min_item = node.item
            node = node.next
        return min_item

    def predecessor(self, item: KeyedItem) -> KeyedItem:
        """O(n)"""
        from math import inf
        key = item.key
        predecessor = None
        predecessor_key = -inf
        current_node = self._container.head
        while current_node:
            current_key = current_node.item.key
            if predecessor_key < current_key < key:
                predecessor, predecessor_key = current_node, current_key
            current_node = current_node.next
        return predecessor.item if predecessor else None

    def successor(self, item: KeyedItem) -> KeyedItem:
        """O(n)"""
        from math import inf
        key = item.key
        successor = None
        successor_key = inf
        current_node = self._container.head
        while current_node:
            current_key = current_node.item.key
            if successor_key > current_key > key:
                successor, successor_key = current_node, current_key
            current_node = current_node.next
        return successor.item if successor else None


class DoublyUnsortedBasedDictionnary(BaseDictionnary):
    def __init__(self):
        self._container = DoublyLinkedList()

    def search(self, key) -> KeyedItem:
        """O(n)"""
        return SinglyUnsortedBasedDictionnary.search(self, key)

    def insert(self, item: KeyedItem):
        """O(1)"""
        SinglyUnsortedBasedDictionnary.insert(self, item)
        item.node = self._container.head

    def delete(self, item: KeyedItem):
        """O(1)"""
        previous_node, next_node = item.node.previous, item.node.next
        if previous_node:
            previous_node.next = next_node
        else:
            self._container.head = next_node
        if next_node:
            next_node.previous = previous_node
        else:
            self._container.tail = previous_node

    def max(self) -> KeyedItem:
        """O(n)"""
        return SinglyUnsortedBasedDictionnary.max(self)

    def min(self) -> KeyedItem:
        """O(n)"""
        return SinglyUnsortedBasedDictionnary.min(self)

    def predecessor(self, item: KeyedItem) -> KeyedItem:
        """O(n)"""
        return SinglyUnsortedBasedDictionnary.predecessor(self, item)

    def successor(self, item: KeyedItem) -> KeyedItem:
        """O(n)"""
        return SinglyUnsortedBasedDictionnary.successor(self, item)


class SinglySortedBasedDictionnary(BaseDictionnary):
    def __init__(self):
        self._container = LinkedList()

    def search(self, key) -> KeyedItem:
        """O(n)"""
        node = self._container.head
        while node:
            if node.item.key == key:
                return node.item
            node = node.next
        raise FileNotFoundError

    def insert(self, item: KeyedItem):
        """O(n)"""
        key = item.key
        previous_node = None
        current_node = self._container.head
        while current_node:
            if current_node.item.key > key:
                break
            previous_node, current_node = current_node, current_node.next
        inserted_node = LinkedListNode(item=item, next=current_node)
        item.node = inserted_node
        if previous_node:
            previous_node.next = inserted_node
        else:
            self._container.head = inserted_node
        if not current_node:
            self._container.tail = inserted_node

    def delete(self, item: KeyedItem):
        """O(n)"""
        item_predecessor = self.predecessor(item)
        item_successor = self.successor(item)
        node_predecessor = item_predecessor.node if item_predecessor else None
        node_successor = item_successor.node if item_successor else None
        if node_predecessor:
            node_predecessor.next = node_successor
        else:
            self._container.head = node_successor
        if not node_successor:
            self._container.tail = node_predecessor

    def max(self) -> KeyedItem:
        """O(1)"""
        return self._container.tail.item if self._container.tail else None

    def min(self) -> KeyedItem:
        """O(1)"""
        return self._container.head.item if self._container.head else None

    def predecessor(self, item: KeyedItem) -> KeyedItem:
        """O(n)"""
        predecessor = None
        current_node = self._container.head
        while current_node.item is not item:
            predecessor, current_node = current_node, current_node.next
        return predecessor.item if predecessor else None

    def successor(self, item: KeyedItem) -> KeyedItem:
        """O(1)"""
        return item.node.next.item if item.node.next else None


class DoublySortedBasedDictionnary(BaseDictionnary):
    def __init__(self):
        self._container = DoublyLinkedList()

    def search(self, key) -> KeyedItem:
        """O(n)"""
        return SinglySortedBasedDictionnary.search(self, key)

    def insert(self, item: KeyedItem):
        """O(n)"""
        key = item.key
        previous_node = None
        current_node = self._container.head
        while current_node:
            if current_node.item.key > key:
                break
            previous_node, current_node = current_node, current_node.next
        inserted_node = DoublyLinkedListNode(item=item,
                                             previous=previous_node,
                                             next=current_node)
        item.node = inserted_node
        if previous_node:
            previous_node.next = inserted_node
        else:
            self._container.head = inserted_node
        if current_node:
            current_node.previous = inserted_node
        else:
            self._container.tail = inserted_node

    def delete(self, item: KeyedItem):
        """O(1)"""
        item_predecessor = self.predecessor(item)
        node_precedessor = item_predecessor.node if item_predecessor else None
        item_successor = self.successor(item)
        node_successor = item_successor.node if item_successor else None
        if node_precedessor:
            node_precedessor.next = node_successor
        else:
            self._container.head = node_successor
        if node_successor:
            node_successor.previous = node_precedessor
        else:
            self._container.tail = node_precedessor

    def max(self) -> KeyedItem:
        """O(1)"""
        return SinglySortedBasedDictionnary.max(self)

    def min(self) -> KeyedItem:
        """O(1)"""
        return SinglySortedBasedDictionnary.min(self)

    def predecessor(self, item: KeyedItem) -> KeyedItem:
        """O(1)"""
        return item.node.previous.item if item.node.previous else None

    def successor(self, item: KeyedItem) -> KeyedItem:
        """O(1)"""
        return SinglySortedBasedDictionnary.successor(self, item)


class BalancedTreeBasedDictionnary(BaseDictionnary):
    def __init__(self):
        self._container = BinarySearchTree()

    def search(self, key) -> KeyedItem:
        """O(log n)"""
        return self._container.search(value=key).content

    def insert(self, item: KeyedItem):
        """O(log n)"""
        self._container.insert(value=item.key, content=item)

    def delete(self, item: KeyedItem):
        """O(log n)"""
        node = self._container.search(value=item.key)
        self._container.delete(node)

    def max(self) -> KeyedItem:
        """O(log n)"""
        max_node = self._container.max()
        return max_node.content if max_node else None

    def min(self) -> KeyedItem:
        """O(log n)"""
        min_node = self._container.min()
        return min_node.content if min_node else None

    def predecessor(self, item: KeyedItem) -> KeyedItem:
        """O(log n)"""
        node = self._container.search(value=item.key)
        if node.left:
            # find rightmost node on the left subtree
            predecessor = node.left
            while predecessor.right:
                predecessor = predecessor.right
            return predecessor.content
        else:
            # find first ancestor whose left child is on a different subtree
            ancestor = node.parent
            while ancestor and ancestor.left is node:
                node = ancestor
                ancestor = node.parent
            return ancestor.content if ancestor else None

    def successor(self, item: KeyedItem) -> KeyedItem:
        """O(log n)"""
        node = self._container.search(value=item.key)
        if node.right:
            # find leftmost node on the right subtree
            predecessor = node.right
            while predecessor.left:
                predecessor = predecessor.left
            return predecessor.content
        else:
            # find first ancestor whose right child is on a different subtree
            ancestor = node.parent
            while ancestor and ancestor.right is node:
                node = ancestor
                ancestor = node.parent
            return ancestor.content if ancestor else None


class Dictionnary:
    def __init__(self, implementation=None):
        if implementation == 'unsorted_array':
            self._dict = UnsortedArrayBasedDictionnary()
        elif implementation == 'sorted_array':
            self._dict = SortedArrayBasedDictionnary()
        elif implementation == 'singly_unsorted':
            self._dict = SinglyUnsortedBasedDictionnary()
        elif implementation == 'doubly_unsorted':
            self._dict = DoublyUnsortedBasedDictionnary()
        elif implementation == 'singly_sorted':
            self._dict = SinglySortedBasedDictionnary()
        elif implementation == 'doubly_sorted':
            self._dict = DoublySortedBasedDictionnary()
        elif implementation == 'balanced_tree':
            self._dict = BalancedTreeBasedDictionnary()
        else:
            self._dict = BaseDictionnary()
        self.implementation = implementation

    def search(self, key) -> KeyedItem:
        """Given a search key, return a pointer to the element in dic-
        tionary self whose key value is k, if one exists."""
        return self._dict.search(key)

    def insert(self, item: KeyedItem):
        self._dict.insert(item)

    def delete(self, item: KeyedItem):
        self._dict.delete(item)

    def max(self) -> KeyedItem:
        """retrieve item with the largest key"""
        return self._dict.max()

    def min(self) -> KeyedItem:
        """retrieve item with the smallest key"""
        return self._dict.min()

    def predecessor(self, item: KeyedItem) -> KeyedItem:
        """retrieve the item whose key is immediately before"""
        return self._dict.predecessor(item)

    def successor(self, item: KeyedItem) -> KeyedItem:
        """retrieve the item whose key is immediately after"""
        return self._dict.successor(item)
