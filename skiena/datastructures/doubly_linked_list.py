class DoublyLinkedListNode:
    """doubly linked list node"""
    def __init__(self, item, previous=None, next=None):
        self.item = item
        self.previous = previous
        self.next = next


class DoublyLinkedList:
    """linked list"""
    def __init__(self):
        self.first = None
        self.last = None

    def search(self, item) -> DoublyLinkedListNode:
        """search in O(n)"""
        node = self.first
        while node:
            if node.item == item:
                return node
            node = node.next
        raise FileNotFoundError

    def insert(self, item):
        """insert in O(1)"""
        former_first = self.first
        self.first = DoublyLinkedListNode(item=item, next=former_first)
        # if it is the first item to be inserted
        if not former_first:
            self.last = self.first
        else:
            former_first.previous = self.first

    def delete(self, item):
        """delete in O(n)"""
        node = self.search(item)
        previous_node = node.previous
        next_node = node.next
        if previous_node:
            previous_node.next = next_node
        else:
            self.first = next_node
        if next_node:
            next_node.previous = previous_node
        else:
            self.last = previous_node
        del node
