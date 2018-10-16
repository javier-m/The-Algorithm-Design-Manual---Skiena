from backtracking.applications import *


def test_subset_construction():
    nb_items = 3
    a = range(nb_items)
    subsets = list(construct_all_subsets(a))
    assert len(subsets) == 2**nb_items
    actual_subsets = [
        [],
        [0], [1], [2],
        [0, 1], [0, 2], [1, 2],
        [0, 1, 2]
    ]
    for subset in subsets:
        assert subset in actual_subsets
