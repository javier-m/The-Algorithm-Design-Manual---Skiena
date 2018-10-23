class DoublyLinkedListNode:
    """doubly linked list node"""
    def __init__(self, item, previous=None, next=None):
        self.item = item
        self.previous = previous
        self.next = next


class DoublyLinkedList:
    """linked list"""
    def __init__(self):
        self.head = None
        self.tail = None

    def search(self, item) -> DoublyLinkedListNode:
        """search in O(n)"""
        node = self.head
        while node:
            if node.item == item:
                return node
            node = node.next
        raise FileNotFoundError

    def insert(self, item):
        """insert in O(1)"""
        former_head = self.head
        self.head = DoublyLinkedListNode(item=item, next=former_head)
        # if it is the head item to be inserted
        if not former_head:
            self.tail = self.head
        else:
            former_head.previous = self.head

    def delete(self, item):
        """delete in O(n)"""
        node = self.search(item)
        previous_node = node.previous
        next_node = node.next
        if previous_node:
            previous_node.next = next_node
        else:
            self.head = next_node
        if next_node:
            next_node.previous = previous_node
        else:
            self.tail = previous_node
        del node
