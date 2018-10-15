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


def test_floyd_warshall_algorithm():
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
    shortest_paths = run_floyd_warshall_algorithm(graph=graph)
    assert shortest_paths[vertices[0]][vertices[1]] == 3
    assert shortest_paths[vertices[0]][vertices[2]] == 2
    assert shortest_paths[vertices[0]][vertices[3]] == 8
    assert shortest_paths[vertices[0]][vertices[4]] == 10
    assert shortest_paths[vertices[0]][vertices[5]] == 14
    assert shortest_paths[vertices[1]][vertices[2]] == 1
    assert shortest_paths[vertices[1]][vertices[3]] == 5
    assert shortest_paths[vertices[1]][vertices[4]] == 7
    assert shortest_paths[vertices[1]][vertices[5]] == 11
    assert shortest_paths[vertices[2]][vertices[3]] == 6
    assert shortest_paths[vertices[2]][vertices[4]] == 8
    assert shortest_paths[vertices[2]][vertices[5]] == 12
    assert shortest_paths[vertices[3]][vertices[4]] == 2
    assert shortest_paths[vertices[3]][vertices[5]] == 6
    assert shortest_paths[vertices[4]][vertices[5]] == 5
    for i in range(6):
        assert shortest_paths[vertices[i]][vertices[i]] == 0
    for i in range(5):
        for j in range(i+1, 6):
            assert shortest_paths[vertices[i]][vertices[j]] == shortest_paths[vertices[j]][vertices[i]]


def test_floyd_warshall_algorithm_with_parallel_edges():
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
    shortest_paths = run_floyd_warshall_algorithm(graph=graph)
    assert shortest_paths[vertices[0]][vertices[1]] == 3
    assert shortest_paths[vertices[0]][vertices[2]] == 2
    assert shortest_paths[vertices[0]][vertices[3]] == 8
    assert shortest_paths[vertices[0]][vertices[4]] == 10
    assert shortest_paths[vertices[0]][vertices[5]] == 14
    assert shortest_paths[vertices[1]][vertices[2]] == 1
    assert shortest_paths[vertices[1]][vertices[3]] == 5
    assert shortest_paths[vertices[1]][vertices[4]] == 7
    assert shortest_paths[vertices[1]][vertices[5]] == 11
    assert shortest_paths[vertices[2]][vertices[3]] == 6
    assert shortest_paths[vertices[2]][vertices[4]] == 8
    assert shortest_paths[vertices[2]][vertices[5]] == 12
    assert shortest_paths[vertices[3]][vertices[4]] == 2
    assert shortest_paths[vertices[3]][vertices[5]] == 6
    assert shortest_paths[vertices[4]][vertices[5]] == 5
    for i in range(6):
        assert shortest_paths[vertices[i]][vertices[i]] == 0
    for i in range(5):
        for j in range(i+1, 6):
            assert shortest_paths[vertices[i]][vertices[j]] == shortest_paths[vertices[j]][vertices[i]]


def test_floyd_warshall_fail_on_negative_edge_costs():
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
        run_floyd_warshall_algorithm(graph=graph)


def test_network_flow():
    vertices = [Vertex() for i in range(7)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1], weight=5),
        Edge(head=vertices[0], tail=vertices[2], weight=12),
        Edge(head=vertices[1], tail=vertices[3], weight=9),
        Edge(head=vertices[1], tail=vertices[5], weight=7),
        Edge(head=vertices[2], tail=vertices[3], weight=4),
        Edge(head=vertices[2], tail=vertices[4], weight=7),
        Edge(head=vertices[3], tail=vertices[4], weight=3),
        Edge(head=vertices[3], tail=vertices[5], weight=3),
        Edge(head=vertices[4], tail=vertices[6], weight=2),
        Edge(head=vertices[5], tail=vertices[6], weight=5),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    flow, graph = find_network_flow(graph=graph, source=vertices[0], sink=vertices[6])
    assert flow == 7
