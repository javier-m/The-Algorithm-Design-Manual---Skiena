from typing import List

from datastructures import KeyedItem, LinkedList
from .n_square import insertion_sort


def radixsort(items: List[KeyedItem], base: int=10, order=None) -> List[KeyedItem]:
    """Non-comparison-based sorting algorithm
    O(w*n) where w is the word size
    can be faster than n*log(n) sorting algorithms if w is constant size
    otherwise, w is >= log(n) for n different items"""
    def bucket_list(subitems: List[KeyedItem], iteration) -> List[List[KeyedItem]]:
        nonlocal base
        buckets = [[] for x in range(base)]
        for item in subitems:
            radix = (item.key // base ** iteration) % base
            buckets[radix].append(item)
        return buckets

    def unbucket(buckets: List[List[KeyedItem]]) -> List[KeyedItem]:
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


def countsort(items: List[KeyedItem], order=None) -> List[KeyedItem]:
    """Non-comparison-based sorting algorithm
    O(k+n) where k is the nb of different values the inputs can take"""
    min_value = min(items, key=lambda it: it.key).key
    value_shift = 0 if min_value > 0 else -min_value
    if value_shift:
        for item in items:
            item.key += value_shift

    max_value = max(items, key=lambda it: it.key).key

    counter = [0] * (max_value + 1)
    for item in items:
        counter[item.key] += 1
    if order == 'max':
        for i in range(max_value-1, -1, -1):
            counter[i] += counter[i+1]
    else:
        for i in range(max_value):
            counter[i + 1] += counter[i]

    sorted_items = [None] * len(items)
    for i in range(len(items)-1, -1, -1):
        sorted_items[counter[items[i].key] - 1] = items[i]
        counter[items[i].key] -= 1

    if value_shift:
        for item in sorted_items:
            item.key -= value_shift

    return sorted_items


def bucketsort(items: List[KeyedItem], order=None) -> List[KeyedItem]:
    """Non-comparison-based sorting algorithm
    average is theta(n) when the distribution is uniform"""
    min_value = min(items, key=lambda it: it.key).key
    max_value = max(items, key=lambda it: it.key).key
    delta_value = max_value - min_value
    nb_items = len(items)

    buckets = [[] for i in range(len(items))]
    for item in items:
        ind = int((nb_items-1)*(item.key - min_value)/delta_value)
        buckets[ind].append(item)

    sorted_items = []
    if order == 'max':
        buckets.reverse()
    for bucket in buckets:
        insertion_sort(bucket, order=order)
        sorted_items += bucket

    return sorted_items
