from typing import Sequence, List
from .item import Item

from datastructures import Heap


def heapsort(items: Sequence[Item], order=None) -> List[Item]:
    """O(n*log n)"""
    heap = Heap(heaptype=order)
    heap.construct(items)
    sorted_items = []
    while True:
        item = heap.extract_root()
        if not item:
            break
        sorted_items.append(item)
    return sorted_items
