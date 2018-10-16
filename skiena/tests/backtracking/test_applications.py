from graph import Vertex, Edge, Graph

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


def test_all_paths():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1]),
        Edge(head=vertices[0], tail=vertices[2]),
        Edge(head=vertices[0], tail=vertices[3]),
        Edge(head=vertices[0], tail=vertices[4]),
        Edge(head=vertices[1], tail=vertices[5]),
        Edge(head=vertices[2], tail=vertices[3]),
        Edge(head=vertices[2], tail=vertices[5]),
        Edge(head=vertices[3], tail=vertices[5]),
        Edge(head=vertices[4], tail=vertices[5]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    edge_paths = list(construct_all_paths(graph=graph,
                                     start=vertices[0],
                                     end=vertices[2]))
    paths = []
    for edge_path in edge_paths:
        path = [vertices[0]] + [edge.tail for edge in edge_path]
        paths.append(path)
    assert len(paths) == 7
    actual_paths = [
        [vertices[0], vertices[1], vertices[5], vertices[2]],
        [vertices[0], vertices[1], vertices[5], vertices[3], vertices[2]],
        [vertices[0], vertices[2]],
        [vertices[0], vertices[3], vertices[2]],
        [vertices[0], vertices[3], vertices[5], vertices[2]],
        [vertices[0], vertices[4], vertices[5], vertices[2]],
        [vertices[0], vertices[4], vertices[5], vertices[3], vertices[2]],
    ]
