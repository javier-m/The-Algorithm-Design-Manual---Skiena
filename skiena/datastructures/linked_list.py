class LinkedListNode:
    """linked list node"""
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedList:
    """linked list"""
    def __init__(self):
        # sentinel
        self._nil = LinkedListNode(item=None)
        self._nil.next = self._nil
        self.tail = self._nil

    @property
    def head(self):
        return self._nil.next

    def __iter__(self):
        node = self.head
        while node.item is not None:
            yield node.item
            node = node.next

    def search(self, item) -> LinkedListNode:
        """search in O(n)"""
        node = self.head
        while node is not self._nil:
            if node.item == item:
                return node
            node = node.next
        raise FileNotFoundError

    def insert(self, item):
        """insert in O(1)"""
        item_node = LinkedListNode(item=item, next=self._nil.next)
        self._nil.next = item_node
        # if it is the head item to be inserted
        if self.tail is self._nil:
            self.tail = item_node

    def previous(self, item) -> LinkedListNode:
        """find previous node in O(n)"""
        node = self.head
        while node is not self._nil:
            if node.next.item is item:
                return node
            node = node.next
        return node

    def delete(self, item):
        """delete in O(n)"""
        previous_node = self._nil
        node = self.head
        while node is not self._nil:
            if node.item is item:
                previous_node.next = node.next
                if node is self.tail:
                    self.tail = previous_node
                del node
                return
            previous_node, node = node, node.next
        raise FileNotFoundError
