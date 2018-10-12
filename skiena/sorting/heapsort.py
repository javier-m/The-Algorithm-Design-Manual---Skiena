from typing import Sequence, List

from datastructures import KeyedItem, Heap


def heapsort(items: Sequence[KeyedItem], order=None) -> List[KeyedItem]:
    """O(n*log n)"""
    heap = Heap(heaptype=order)
    heap.heapify(items)
    sorted_items = []
    while True:
        item = heap.extract_root()
        if not item:
            break
        sorted_items.append(item)
    return sorted_items
