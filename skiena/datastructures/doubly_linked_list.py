class DoublyLinkedListNode:
    """doubly linked list node"""
    def __init__(self, item, previous=None, next=None):
        self.item = item
        self.previous = previous
        self.next = next


class DoublyLinkedList:
    """linked list"""
    def __init__(self):
        # sentinel
        self._nil = DoublyLinkedListNode(item=None)
        self._nil.previous = self._nil
        self._nil.next = self._nil

    @property
    def head(self):
        return self._nil.next

    @property
    def tail(self):
        return self._nil.previous

    def search(self, item) -> DoublyLinkedListNode:
        """search in O(n)"""
        node = self.head
        while node is not self._nil:
            if node.item is item:
                return node
            node = node.next
        raise FileNotFoundError

    def insert(self, item):
        """insert in O(1)"""
        item_node = DoublyLinkedListNode(item=item)
        item_node.next = self._nil.next
        item_node.next.previous = item_node
        self._nil.next = item_node
        item_node.previous = self._nil

    def delete(self, item):
        """delete in O(n)"""
        item_node = self.search(item)
        item_node.previous.next = item_node.next
        item_node.next.previous = item_node.previous
        del item_node
