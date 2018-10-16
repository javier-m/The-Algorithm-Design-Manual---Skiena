from typing import Sequence, List, Any, Iterator

from .backtracking import backtrack


def construct_all_subsets(myset: Sequence[Any]) -> Sequence[List[Any]]:
    mylist = list(myset)
    nb_items = len(mylist)

    def is_a_solution(a: list, k: int, inputs: None):
        nonlocal nb_items
        return nb_items == k + 1

    def construct_candidates(a: list, k: int, inputs: None) -> Iterator:
        yield False
        yield True

    for belongs_to_subset in backtrack(a=[None] * nb_items,
                                       is_a_solution=is_a_solution,
                                       construct_candidates=construct_candidates):
        yield [x for i, x in enumerate(mylist) if belongs_to_subset[i]]
