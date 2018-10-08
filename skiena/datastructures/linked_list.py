class LinkedListNode:
    """linked list node"""
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedList:
    """linked list"""
    def __init__(self):
        self.first = None
        self.last = None

    def __iter__(self):
        node = self.first
        while node:
            yield node.item
            node = node.next

    def search(self, item):
        """search in O(n)"""
        node = self.first
        while node:
            if node.item == item:
                return node
            node = node.next
        raise FileNotFoundError

    def insert(self, item):
        """insert in O(1)"""
        self.first = LinkedListNode(item=item, next=self.first)
        # if it is the first item to be inserted
        if not self.last:
            self.last = self.first

    def previous(self, item):
        """find previous node in O(n)"""
        node = self.first
        while node:
            if node.next and node.next.item == item:
                return node
            node = node.next
        return None

    def delete(self, item):
        """delete in O(n)"""
        previous_node = None
        node = self.first
        while node:
            next_node = node.next
            if node.item == item:
                if previous_node:
                    previous_node.next = next_node
                if node is self.first:
                    self.first = next_node
                if node is self.last:
                    self.last = previous_node
                del node
                return
            previous_node, node = node, next_node
        raise FileNotFoundError
