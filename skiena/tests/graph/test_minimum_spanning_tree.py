import pytest

from graph import Vertex, Edge, Graph
from graph.minimum_spanning_tree import *
from graph.exceptions import *


def test_prim_algorithm():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1]),
        Edge(head=vertices[1], tail=vertices[2]),
        Edge(head=vertices[2], tail=vertices[0]),
        Edge(head=vertices[3], tail=vertices[4]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    mst = run_prim_algorithm(graph=graph, start=vertices[0])


def test_prim_algorithm_with_parallel_edges():
    ...


def test_prim_algorithm_fail_on_directed_graph():
    ...
    graph = Graph(vertices=vertices, edges=edges, directed=True)
    with pytest.raises(GraphDirectionTypeError):
        run_prim_algorithm(graph=graph, start=vertices[0])