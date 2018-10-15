import pytest

from graph import Vertex, Edge, Graph
from graph.shortest_path import *
from graph.exceptions import *


def test_dijkstra_algorithm():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1], weight=4),
        Edge(head=vertices[0], tail=vertices[2], weight=2),
        Edge(head=vertices[1], tail=vertices[2], weight=1),
        Edge(head=vertices[1], tail=vertices[3], weight=5),
        Edge(head=vertices[2], tail=vertices[3], weight=8),
        Edge(head=vertices[2], tail=vertices[4], weight=10),
        Edge(head=vertices[3], tail=vertices[4], weight=2),
        Edge(head=vertices[3], tail=vertices[5], weight=6),
        Edge(head=vertices[4], tail=vertices[5], weight=5),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    shortest_paths = run_dijkstra_algorithm(graph=graph, source=vertices[0])
    for i in range(6):
        assert shortest_paths[vertices[i]].source is vertices[0]
        assert shortest_paths[vertices[i]].destination is vertices[i]
    assert shortest_paths[vertices[0]].last_hop is None
    assert shortest_paths[vertices[0]].distance == 0
    assert shortest_paths[vertices[1]].last_hop.head is vertices[2]
    assert shortest_paths[vertices[1]].distance == 3
    assert shortest_paths[vertices[2]].last_hop.head is vertices[0]
    assert shortest_paths[vertices[2]].distance == 2
    assert shortest_paths[vertices[3]].last_hop.head is vertices[1]
    assert shortest_paths[vertices[3]].distance == 8
    assert shortest_paths[vertices[4]].last_hop.head is vertices[3]
    assert shortest_paths[vertices[4]].distance == 10
    assert shortest_paths[vertices[5]].last_hop.head is vertices[3]
    assert shortest_paths[vertices[5]].distance == 14


def test_dijkstra_algorithm_with_parallel_edge():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1], weight=4),
        Edge(head=vertices[0], tail=vertices[2], weight=3),
        Edge(head=vertices[0], tail=vertices[2], weight=2),
        Edge(head=vertices[1], tail=vertices[2], weight=1),
        Edge(head=vertices[1], tail=vertices[3], weight=5),
        Edge(head=vertices[2], tail=vertices[3], weight=8),
        Edge(head=vertices[2], tail=vertices[3], weight=9),
        Edge(head=vertices[2], tail=vertices[4], weight=10),
        Edge(head=vertices[3], tail=vertices[4], weight=2),
        Edge(head=vertices[3], tail=vertices[5], weight=6),
        Edge(head=vertices[4], tail=vertices[5], weight=5),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    shortest_paths = run_dijkstra_algorithm(graph=graph, source=vertices[0])
    for i in range(6):
        assert shortest_paths[vertices[i]].source is vertices[0]
        assert shortest_paths[vertices[i]].destination is vertices[i]
    assert shortest_paths[vertices[0]].last_hop is None
    assert shortest_paths[vertices[0]].distance == 0
    assert shortest_paths[vertices[1]].last_hop.head is vertices[2]
    assert shortest_paths[vertices[1]].distance == 3
    assert shortest_paths[vertices[2]].last_hop.head is vertices[0]
    assert shortest_paths[vertices[2]].distance == 2
    assert shortest_paths[vertices[3]].last_hop.head is vertices[1]
    assert shortest_paths[vertices[3]].distance == 8
    assert shortest_paths[vertices[4]].last_hop.head is vertices[3]
    assert shortest_paths[vertices[4]].distance == 10
    assert shortest_paths[vertices[5]].last_hop.head is vertices[3]
    assert shortest_paths[vertices[5]].distance == 14


def test_dijkstra_algorithm_fail_on_negative_edge_costs_from_source():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1], weight=4),
        Edge(head=vertices[0], tail=vertices[2], weight=-2),
        Edge(head=vertices[1], tail=vertices[2], weight=1),
        Edge(head=vertices[1], tail=vertices[3], weight=5),
        Edge(head=vertices[2], tail=vertices[3], weight=8),
        Edge(head=vertices[2], tail=vertices[4], weight=10),
        Edge(head=vertices[3], tail=vertices[4], weight=2),
        Edge(head=vertices[3], tail=vertices[5], weight=6),
        Edge(head=vertices[4], tail=vertices[5], weight=5),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    with pytest.raises(GraphTypeError):
        run_dijkstra_algorithm(graph=graph, source=vertices[0])


def test_dijkstra_algorithm_fail_on_negative_edge_costs():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1], weight=4),
        Edge(head=vertices[0], tail=vertices[2], weight=2),
        Edge(head=vertices[1], tail=vertices[2], weight=1),
        Edge(head=vertices[1], tail=vertices[3], weight=5),
        Edge(head=vertices[2], tail=vertices[3], weight=8),
        Edge(head=vertices[2], tail=vertices[4], weight=10),
        Edge(head=vertices[3], tail=vertices[4], weight=-2),
        Edge(head=vertices[3], tail=vertices[5], weight=6),
        Edge(head=vertices[4], tail=vertices[5], weight=5),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    with pytest.raises(GraphTypeError):
        run_dijkstra_algorithm(graph=graph, source=vertices[0])
