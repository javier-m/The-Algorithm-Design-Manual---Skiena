class LinkedListNode:
    """linked list node"""
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedList:
    """linked list"""
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def search(self, item) -> LinkedListNode:
        """search in O(n)"""
        node = self.head
        while node:
            if node.item == item:
                return node
            node = node.next
        raise FileNotFoundError

    def insert(self, item):
        """insert in O(1)"""
        self.head = LinkedListNode(item=item, next=self.head)
        # if it is the head item to be inserted
        if not self.tail:
            self.tail = self.head

    def previous(self, item) -> LinkedListNode:
        """find previous node in O(n)"""
        node = self.head
        while node:
            if node.next and node.next.item == item:
                return node
            node = node.next
        return None

    def delete(self, item):
        """delete in O(n)"""
        previous_node = None
        node = self.head
        while node:
            next_node = node.next
            if node.item == item:
                if previous_node:
                    previous_node.next = next_node
                if node is self.head:
                    self.head = next_node
                if node is self.tail:
                    self.tail = previous_node
                del node
                return
            previous_node, node = node, next_node
        raise FileNotFoundError
