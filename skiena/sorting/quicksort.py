from typing import Sequence

import random

from datastructures import KeyedItem, Stack, StackEmptyError


def quicksort(items: Sequence[KeyedItem], order=None) -> None:
    """O(n*log n) expected - O(n**2) worst case"""
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
        if low < high - 1:
            # pick pivot
            pivot_index = random.randint(low, high)
            pivot = items[pivot_index]
            # partition according to pivot with linear scan
            items[high], items[pivot_index] = items[pivot_index], items[high]
            pivot_index = low
            for i in range(low, high):
                item = items[i]
                if comp(item.key, pivot.key):
                    items[i], items[pivot_index] = items[pivot_index], items[i]
                    pivot_index += 1
            items[high], items[pivot_index] = items[pivot_index], items[high]

            if not stack_item.status:
                # sort left of pivot
                stack_item.status = 1
                stack.push(stack_item)
                stack.push(StackItem(low, pivot_index - 1))
            elif stack_item.status == 1:
                # sort right of pivot
                stack_item.status = 2
                stack.push(stack_item)
                stack.push(StackItem(pivot_index + 1, high))
        try:
            stack_item = stack.pop()
        except StackEmptyError:
            break
