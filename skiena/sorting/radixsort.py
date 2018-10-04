from typing import List
from .item import Item


def radixsort(items: List[Item], base: int=10, order=None) -> List[Item]:
    """Non-comparison-based sorting algorithm
    O(w*n) where w is the word size
    can be faster than n*log(n) sorting algorithms if w is constant size
    otherwise, w is >= log(n) for n different items"""
    def bucket_list(subitems: List[Item], iteration) -> List[List[Item]]:
        nonlocal base
        buckets = [[] for x in range(base)]
        for item in subitems:
            radix = (item.key // base ** iteration) % base
            buckets[radix].append(item)
        return buckets

    def unbucket(buckets: List[List[Item]]) -> List[Item]:
        nonlocal order
        subitems = []
        order_nb = -1 if order == 'max' else 1
        for bucket in buckets[::order_nb]:
            for item in bucket:
                subitems.append(item)
        return subitems

    min_value = min(items, key=lambda it: it.key).key
    value_shift = 0 if min_value > 0 else -min_value
    if value_shift:
        for item in items:
            item.key += value_shift

    max_value = max(items, key=lambda it: it.key).key
    iteration = 0
    while base**iteration <= max_value:
        items = unbucket(bucket_list(items, iteration))
        iteration += 1

    if value_shift:
        for item in items:
            item.key -= value_shift

    return items
