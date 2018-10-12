import pytest

from graph import Vertex, Edge, Graph
from graph.minimum_spanning_tree import *
from graph.exceptions import *


def test_prim_algorithm():
    vertices = [Vertex() for i in range(9)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1], weight=4),
        Edge(head=vertices[0], tail=vertices[7], weight=8),
        Edge(head=vertices[1], tail=vertices[2], weight=9),
        Edge(head=vertices[1], tail=vertices[7], weight=11),
        Edge(head=vertices[2], tail=vertices[3], weight=7),
        Edge(head=vertices[2], tail=vertices[5], weight=4),
        Edge(head=vertices[2], tail=vertices[8], weight=2),
        Edge(head=vertices[3], tail=vertices[4], weight=9),
        Edge(head=vertices[3], tail=vertices[5], weight=14),
        Edge(head=vertices[4], tail=vertices[5], weight=10),
        Edge(head=vertices[5], tail=vertices[6], weight=2),
        Edge(head=vertices[6], tail=vertices[7], weight=1),
        Edge(head=vertices[6], tail=vertices[8], weight=8),
        Edge(head=vertices[7], tail=vertices[8], weight=7),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    mst = run_prim_algorithm(graph=graph, start=vertices[0])
    tails = [set() for i in range(9)]
    for i in range(9):
        for edgenode in mst.adjacency_lists[vertices[i]].edgenodes:
            tails[i].add(edgenode.tail)
    assert tails[0] == {vertices[1], vertices[7]}
    assert tails[1] == {vertices[0]}
    assert tails[2] == {vertices[3], vertices[5], vertices[8]}
    assert tails[3] == {vertices[2], vertices[4]}
    assert tails[4] == {vertices[3]}
    assert tails[5] == {vertices[2], vertices[6]}
    assert tails[6] == {vertices[5], vertices[7]}
    assert tails[7] == {vertices[0], vertices[6]}
    assert tails[8] == {vertices[2]}


def test_prim_algorithm_with_parallel_edges():
    vertices = [Vertex() for i in range(9)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1], weight=4),
        Edge(head=vertices[0], tail=vertices[7], weight=8),
        Edge(head=vertices[1], tail=vertices[2], weight=9),
        Edge(head=vertices[1], tail=vertices[7], weight=11),
        Edge(head=vertices[2], tail=vertices[3], weight=7),
        Edge(head=vertices[2], tail=vertices[5], weight=4),
        Edge(head=vertices[2], tail=vertices[8], weight=2),
        Edge(head=vertices[3], tail=vertices[4], weight=9),
        Edge(head=vertices[3], tail=vertices[5], weight=14),
        Edge(head=vertices[4], tail=vertices[5], weight=10),
        Edge(head=vertices[5], tail=vertices[6], weight=2),
        Edge(head=vertices[6], tail=vertices[7], weight=1),
        Edge(head=vertices[6], tail=vertices[8], weight=8),
        Edge(head=vertices[7], tail=vertices[8], weight=7),
        Edge(head=vertices[0], tail=vertices[1], weight=100),
        Edge(head=vertices[0], tail=vertices[7], weight=100),
        Edge(head=vertices[1], tail=vertices[2], weight=100),
        Edge(head=vertices[1], tail=vertices[7], weight=1100),
        Edge(head=vertices[2], tail=vertices[3], weight=100),
        Edge(head=vertices[2], tail=vertices[5], weight=100),
        Edge(head=vertices[2], tail=vertices[8], weight=100),
        Edge(head=vertices[3], tail=vertices[4], weight=100),
        Edge(head=vertices[3], tail=vertices[5], weight=1100),
        Edge(head=vertices[4], tail=vertices[5], weight=1100),
        Edge(head=vertices[5], tail=vertices[6], weight=100),
        Edge(head=vertices[6], tail=vertices[7], weight=100),
        Edge(head=vertices[6], tail=vertices[8], weight=100),
        Edge(head=vertices[7], tail=vertices[8], weight=100),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    mst = run_prim_algorithm(graph=graph, start=vertices[0])
    tails = [set() for i in range(9)]
    for i in range(9):
        for edgenode in mst.adjacency_lists[vertices[i]].edgenodes:
            tails[i].add(edgenode.tail)
    assert tails[0] == {vertices[1], vertices[7]}
    assert tails[1] == {vertices[0]}
    assert tails[2] == {vertices[3], vertices[5], vertices[8]}
    assert tails[3] == {vertices[2], vertices[4]}
    assert tails[4] == {vertices[3]}
    assert tails[5] == {vertices[2], vertices[6]}
    assert tails[6] == {vertices[5], vertices[7]}
    assert tails[7] == {vertices[0], vertices[6]}
    assert tails[8] == {vertices[2]}


def test_prim_algorithm_fail_on_directed_graph():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1]),
        Edge(head=vertices[1], tail=vertices[2]),
        Edge(head=vertices[2], tail=vertices[0]),
        Edge(head=vertices[3], tail=vertices[4]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=True)
    with pytest.raises(GraphDirectionTypeError):
        run_prim_algorithm(graph=graph, start=vertices[0])


def test_kruskal_algorithm():
    vertices = [Vertex() for i in range(9)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1], weight=4),
        Edge(head=vertices[0], tail=vertices[7], weight=8),
        Edge(head=vertices[1], tail=vertices[2], weight=9),
        Edge(head=vertices[1], tail=vertices[7], weight=11),
        Edge(head=vertices[2], tail=vertices[3], weight=7),
        Edge(head=vertices[2], tail=vertices[5], weight=4),
        Edge(head=vertices[2], tail=vertices[8], weight=2),
        Edge(head=vertices[3], tail=vertices[4], weight=9),
        Edge(head=vertices[3], tail=vertices[5], weight=14),
        Edge(head=vertices[4], tail=vertices[5], weight=10),
        Edge(head=vertices[5], tail=vertices[6], weight=2),
        Edge(head=vertices[6], tail=vertices[7], weight=1),
        Edge(head=vertices[6], tail=vertices[8], weight=8),
        Edge(head=vertices[7], tail=vertices[8], weight=7),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    mst = run_kruskal_algorithm(graph=graph)
    tails = [set() for i in range(9)]
    for i in range(9):
        for edgenode in mst.adjacency_lists[vertices[i]].edgenodes:
            tails[i].add(edgenode.tail)
    assert tails[0] == {vertices[1], vertices[7]}
    assert tails[1] == {vertices[0]}
    assert tails[2] == {vertices[3], vertices[5], vertices[8]}
    assert tails[3] == {vertices[2], vertices[4]}
    assert tails[4] == {vertices[3]}
    assert tails[5] == {vertices[2], vertices[6]}
    assert tails[6] == {vertices[5], vertices[7]}
    assert tails[7] == {vertices[0], vertices[6]}
    assert tails[8] == {vertices[2]}


def test_kruskal_algorithm_with_parallel_edges():
    vertices = [Vertex() for i in range(9)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1], weight=4),
        Edge(head=vertices[0], tail=vertices[7], weight=8),
        Edge(head=vertices[1], tail=vertices[2], weight=9),
        Edge(head=vertices[1], tail=vertices[7], weight=11),
        Edge(head=vertices[2], tail=vertices[3], weight=7),
        Edge(head=vertices[2], tail=vertices[5], weight=4),
        Edge(head=vertices[2], tail=vertices[8], weight=2),
        Edge(head=vertices[3], tail=vertices[4], weight=9),
        Edge(head=vertices[3], tail=vertices[5], weight=14),
        Edge(head=vertices[4], tail=vertices[5], weight=10),
        Edge(head=vertices[5], tail=vertices[6], weight=2),
        Edge(head=vertices[6], tail=vertices[7], weight=1),
        Edge(head=vertices[6], tail=vertices[8], weight=8),
        Edge(head=vertices[7], tail=vertices[8], weight=7),
        Edge(head=vertices[0], tail=vertices[1], weight=100),
        Edge(head=vertices[0], tail=vertices[7], weight=100),
        Edge(head=vertices[1], tail=vertices[2], weight=100),
        Edge(head=vertices[1], tail=vertices[7], weight=1100),
        Edge(head=vertices[2], tail=vertices[3], weight=100),
        Edge(head=vertices[2], tail=vertices[5], weight=100),
        Edge(head=vertices[2], tail=vertices[8], weight=100),
        Edge(head=vertices[3], tail=vertices[4], weight=100),
        Edge(head=vertices[3], tail=vertices[5], weight=1100),
        Edge(head=vertices[4], tail=vertices[5], weight=1100),
        Edge(head=vertices[5], tail=vertices[6], weight=100),
        Edge(head=vertices[6], tail=vertices[7], weight=100),
        Edge(head=vertices[6], tail=vertices[8], weight=100),
        Edge(head=vertices[7], tail=vertices[8], weight=100),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    mst = run_kruskal_algorithm(graph=graph)
    tails = [set() for i in range(9)]
    for i in range(9):
        for edgenode in mst.adjacency_lists[vertices[i]].edgenodes:
            tails[i].add(edgenode.tail)
    assert tails[0] == {vertices[1], vertices[7]}
    assert tails[1] == {vertices[0]}
    assert tails[2] == {vertices[3], vertices[5], vertices[8]}
    assert tails[3] == {vertices[2], vertices[4]}
    assert tails[4] == {vertices[3]}
    assert tails[5] == {vertices[2], vertices[6]}
    assert tails[6] == {vertices[5], vertices[7]}
    assert tails[7] == {vertices[0], vertices[6]}
    assert tails[8] == {vertices[2]}


def test_kruskal_algorithm_fail_on_directed_graph():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1]),
        Edge(head=vertices[1], tail=vertices[2]),
        Edge(head=vertices[2], tail=vertices[0]),
        Edge(head=vertices[3], tail=vertices[4]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=True)
    with pytest.raises(GraphDirectionTypeError):
        run_kruskal_algorithm(graph=graph)