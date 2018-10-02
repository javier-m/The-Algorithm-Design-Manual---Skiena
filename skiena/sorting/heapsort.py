from typing import Sequence, List

from datastructures import Heap


class Item:
    def __init__(self, key: int, content=None):
        self.key = key
        self.content = content


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