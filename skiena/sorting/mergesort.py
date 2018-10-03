from typing import Sequence
from .item import Item

from datastructures import Stack, StackEmptyError, Queue


def mergesort(items: Sequence[Item], order=None) -> None:
    """O(n*log n)"""
    comp = lambda x, y: x > y if order == 'max' else x < y
    stack = Stack(implementation='linked_list')

    class StackItem:
        def __init__(self, low, high, status=0):
            self.low = low
            self.high = high
            self.status = status

    stack_item = StackItem(0, len(items) - 1)

    while True:
        low = stack_item.low
        high = stack_item.high
        if low != high:
            median = (low + high) // 2
            if not stack_item.status:
                # sort left
                stack_item.status = 1
                stack.push(stack_item)
                stack.push(StackItem(low, median))
            elif stack_item.status == 1:
                # sort right
                stack_item.status = 2
                stack.push(stack_item)
                stack.push(StackItem(median + 1, high))
            else:
                # merge
                left_queue = Queue(implementation='doubly_linked_list')
                for i in range(low, median+1):
                    left_queue.enqueue(items[i])
                right_queue = Queue(implementation='doubly_linked_list')
                for i in range(median+1, high+1):
                    right_queue.enqueue(items[i])
                for i in range(low, high + 1):
                    if not left_queue.head:
                        items[i] = right_queue.dequeue()
                    elif not right_queue.head:
                        items[i] = left_queue.dequeue()
                    else:
                        if comp(left_queue.head.key, right_queue.head.key):
                            items[i] = left_queue.dequeue()
                        else:
                            items[i] = right_queue.dequeue()
        try:
            stack_item = stack.pop()
        except StackEmptyError:
            break
