from math import inf

from .linked_list import LinkedList, LinkedListNode
from .doubly_linked_list import DoublyLinkedList, DoublyLinkedListNode
from .binary_search_tree import BinarySearchTree


class Item:
    def __init__(self, key, content):
        self.key = key
        self.content = content


class BaseDictionnary:
    def search(self, key) -> Item:
        """Given a search key, return a pointer to the element in dic-
        tionary self whose key value is k, if one exists."""
        raise NotImplementedError

    def insert(self, item: Item):
        raise NotImplementedError

    def delete(self, item: Item):
        raise NotImplementedError

    def max(self) -> Item:
        """retrieve item with the largest key"""
        raise NotImplementedError

    def min(self) -> Item:
        """retrieve item with the smallest key"""
        raise NotImplementedError

    def predecessor(self, item: Item) -> Item:
        """retrieve the item whose key is immediately before"""
        raise NotImplementedError

    def successor(self, item: Item) -> Item:
        """retrieve the item whose key is immediately after"""
        raise NotImplementedError


class UnsortedArrayBasedDictionnary(BaseDictionnary):
    def __init__(self, size: int=10000):
        self._container = [None] * size
        self._top = None

    def search(self, key) -> Item:
        """O(n)"""
        if self._top is not None:
            for i in range(self._top + 1):
                item = self._container[i]
                if item.key == key:
                    return item
            raise FileNotFoundError
        raise FileNotFoundError

    def insert(self, item: Item):
        """O(1)"""
        self._top = self._top + 1 if self._top is not None else 0
        item.index = self._top
        self._container[self._top] = item

    def delete(self, item: Item):
        """O(n)"""
        if self._top is not None:
            self._container[item.index] = self._container[self._top]
            self._container[item.index].index = item.index
            self._top = self._top - 1 if self._top else None
            return

    def max(self) -> Item:
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

    def min(self) -> Item:
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

    def predecessor(self, item: Item) -> Item:
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

    def successor(self, item: Item) -> Item:
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

    def search(self, key) -> Item:
        """O(log n)"""
        if self._top is not None:
            min_i = 0
            max_i = self._top
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

    def insert(self, item: Item):
        """O(n)"""
        if self._top is not None:
            i = 0
            key = item.key
            current_key = self._container[i].key
            while (i < self._top + 1
                   and current_key < key):
                i += 1
                current_key = self._container[i].key
            for j in range(self._top, i - 1, -1):
                self._container[j + 1] = self._container[j]
                self._container[j + 1].index = j + 1
            item.index = i
            self._container[i] = item
            self._top += 1
        else:
            self._top = 0
            self._container = item
            item.index = 0

    def delete(self, item: Item):
        """O(n)"""
        if self._top is not None:
            for i in range(self._top + 1):
                if self._container[i] is item:
                    self._container[i] = self._container[self._top]
                    self._top = self._top - 1 if self._top else None
                    return

    def max(self) -> Item:
        """O(1)"""
        if self._top is not None:
            return self._container[self._top]
        return None

    def min(self) -> Item:
        """O(1)"""
        if self._top is not None:
            return self._container[0]
        return None

    def predecessor(self, item: Item) -> Item:
        """O(1)"""
        if self._top is not None:
            index = item.index
            if index:
                return self._container[index - 1]
            return None
        return None

    def successor(self, item: Item) -> Item:
        """O(1)"""
        if self._top is not None:
            index = item.index
            if index < self._top:
                return self._container[index + 1]
            return None
        return None


class SinglyUnsortedBasedDictionnary(BaseDictionnary):
    def __init__(self):
        self._container = LinkedList()

    def search(self, key) -> Item:
        """O(n)"""
        node = self._container.first
        while node:
            if node.item.key == key:
                return node.item
            node = node.next
        raise FileNotFoundError

    def insert(self, item: Item):
        """O(1)"""
        self._container.insert(item)

    def delete(self, item: Item):
        """O(n) - item is actually a node"""
        predecessor = self.predecessor(item)
        predecessor.next = item.next

    def max(self) -> Item:
        """O(n)"""
        from math import inf
        max_key = -inf
        max_item = None
        node = self._container.first
        while node:
            if node.item.key > max_key:
                max_key = node.item.key
                max_item = node.item
            node = node.next
        return max_item

    def min(self) -> Item:
        """O(n)"""
        from math import inf
        min_key = inf
        min_item = None
        node = self._container.first
        while node:
            if node.item.key < min_key:
                min_key = node.item.key
                min_item = node.item
            node = node.next
        return min_item

    def predecessor(self, item) -> Item:
        """O(n) - item is actually a node"""
        from math import inf
        key = item.item.key
        predecessor = None
        predecessor_key = -inf
        current_node = self._container.first
        while current_node:
            current_key = current_node.item.key
            if predecessor_key < current_key < key:
                predecessor, predecessor_key = current_node, current_key
        return predecessor

    def successor(self, item) -> Item:
        """O(n) - item is actually a node"""
        from math import inf
        key = item.item.key
        successor = None
        successor_key = inf
        current_node = self._container.first
        while current_node:
            current_key = current_node.item.key
            if successor_key > current_key > key:
                successor, successor_key = current_node, current_key
        return successor


class DoublyUnsortedBasedDictionnary(BaseDictionnary):
    def __init__(self):
        self._container = DoublyLinkedList()

    def search(self, key) -> Item:
        """O(n)"""
        SinglyUnsortedBasedDictionnary.search(self, key)

    def insert(self, item: Item):
        """O(1)"""
        SinglyUnsortedBasedDictionnary.insert(self, item)

    def delete(self, item: Item):
        """O(1) - item is actually a node"""
        predecessor, successor = item.previous, item.next
        if predecessor:
            predecessor.next = successor
        if successor:
            successor.previous = predecessor

    def max(self) -> Item:
        """O(n)"""
        return SinglyUnsortedBasedDictionnary.max(self)

    def min(self) -> Item:
        """O(n)"""
        return SinglyUnsortedBasedDictionnary.min(self)

    def predecessor(self, item) -> Item:
        """O(n) - item is actually a node"""
        return SinglyUnsortedBasedDictionnary.predecessor(self)

    def successor(self, item) -> Item:
        """O(n) - item is actually a node"""
        return SinglyUnsortedBasedDictionnary.successor(self)


class SinglySortedBasedDictionnary(BaseDictionnary):
    def __init__(self):
        self._container = LinkedList()

    def search(self, key) -> Item:
        """O(n)"""
        node = self.container.first
        while node:
            if node.item.key == key:
                return node.item
            node = node.next
        raise FileNotFoundError

    def insert(self, item: Item):
        """O(n)"""
        key = item.key
        previous_node = None
        current_node = self._container.first
        while current_node:
            if current_node.item.key > key:
                break
            previous_node, current_node = current_node, current_node.next
        inserted_node = LinkedListNode(item=item, next=current_node)
        if previous_node:
            previous_node.next = inserted_node
        else:
            self._container.first = inserted_node
        if not current_node:
            self._container.last = inserted_node

    def delete(self, item: Item):
        """O(n) - item is actually a node"""
        predecessor = self.predecessor(item)
        if predecessor:
            predecessor.next = item.next

    def max(self) -> Item:
        """O(1)"""
        return self._container.last

    def min(self) -> Item:
        """O(1)"""
        return self._container.first

    def predecessor(self, item) -> Item:
        """O(n) - item is actually a node"""
        predecessor = None
        current_node = self._container.first
        while current_node is not item:
            predecessor, current_node = current_node, current_node.next
        return predecessor

    def successor(self, item) -> Item:
        """O(1) - item is actually a node"""
        return item.next


class DoublySortedBasedDictionnary(BaseDictionnary):
    def __init__(self):
        self._container = DoublyLinkedList()

    def search(self, key) -> Item:
        """O(n)"""
        return SinglySortedBasedDictionnary.search(self, key)

    def insert(self, item: Item):
        """O(n)"""
        key = item.key
        previous_node = None
        current_node = self._container.first
        while current_node:
            if current_node.item.key > key:
                break
            previous_node, current_node = current_node, current_node.next
        inserted_node = DoublyLinkedListNode(item=item,
                                             previous=previous_node,
                                             next=current_node)
        if previous_node:
            previous_node.next = inserted_node
        else:
            self._container.first = inserted_node
        if current_node:
            current_node.previous = inserted_node
        else:
            self._container.last = inserted_node

    def delete(self, item: Item):
        """O(1) - item is actually a node"""
        predecessor = self.predecessor(item)
        successor = self.successor(item)
        if predecessor:
            predecessor.next = successor
        if successor:
            successor.previous = predecessor

    def max(self) -> Item:
        """O(1)"""
        return self._container.last

    def min(self) -> Item:
        """O(1)"""
        return self._container.first

    def predecessor(self, item: Item) -> Item:
        """O(1) - item is actually a node"""
        return item.previous

    def successor(self, item: Item) -> Item:
        """O(1) - item is actually a node"""
        return item.next


class BalancedTreeBasedDictionnary(BaseDictionnary):
    def __init__(self):
        self._container = BinarySearchTree()

    def search(self, key) -> Item:
        """O(log n)"""
        self._container.search(value=key).content
        raise FileNotFoundError

    def insert(self, item: Item):
        """O(log n)"""
        self._container.insert(value=item.key, content=item)

    def delete(self, item: Item):
        """O(log n)"""
        node = self._container.search(value=item.key)
        self._container.delete(node)

    def max(self) -> Item:
        """O(log n)"""
        return self._container.max().content

    def min(self) -> Item:
        """O(log n)"""
        return self._container.min().content

    def predecessor(self, item: Item) -> Item:
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

    def successor(self, item: Item) -> Item:
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

    def search(self, key) -> Item:
        """Given a search key, return a pointer to the element in dic-
        tionary self whose key value is k, if one exists."""
        return self._dict.search(key)

    def insert(self, item: Item):
        self._dict.insert(item)

    def delete(self, item: Item):
        self._dict.delete(item)

    def max(self) -> Item:
        """retrieve item with the largest key"""
        return self._dict.max()

    def min(self) -> Item:
        """retrieve item with the smallest key"""
        return self._dict.min()

    def predecessor(self, item: Item) -> Item:
        """retrieve the item whose key is immediately before"""
        return self._dict.predecessor(item)

    def successor(self, item: Item) -> Item:
        """retrieve the item whose key is immediately after"""
        return self._dict.successor(item)
