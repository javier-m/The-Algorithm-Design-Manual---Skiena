from backtracking.applications import *


def test_subset_construction():
    nb_items = 3
    nb_subsets = 2**3
    a = range(nb_items)
    subsets = list(construct_all_subsets(a))
    assert len(subsets) == nb_subsets
    actual_subsets = [
        [],
        [0], [1], [2],
        [0, 1], [0, 2], [1, 2],
        [0, 1, 2]
    ]
    for subset in subsets:
        assert subset in actual_subsets


def test_permutation_construction():
    nb_items = 3
    nb_permutations = 1
    for i in range(nb_items):
        nb_permutations *= (i+1)
    a = range(nb_items)
    permutations = list(construct_all_permutations(a))
    assert len(permutations) == nb_permutations
    actual_permutations = [
        [0, 1, 2],
        [0, 2, 1],
        [1, 0, 2],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0],
    ]
    for permutation in permutations:
        assert permutation in actual_permutations
