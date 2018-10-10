import pytest

from graph import Vertex, Edge, Graph
from graph.applications import *


def test_connected_components():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(start=vertices[0], end=vertices[1]),
        Edge(start=vertices[1], end=vertices[2]),
        Edge(start=vertices[2], end=vertices[0]),
        Edge(start=vertices[3], end=vertices[4]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    connected_components = find_connected_components(graph)
    assert len(connected_components) == 3
    assert {v for v in connected_components[0].adjacency_lists} == {v for v in vertices[:3]}
    assert {v for v in connected_components[1].adjacency_lists} == {v for v in vertices[3:5]}
    assert {v for v in connected_components[2].adjacency_lists} == {vertices[5]}


def test_cycle_found():
    vertices = [Vertex() for i in range(5)]
    edges = [
        Edge(start=vertices[0], end=vertices[1]),
        Edge(start=vertices[1], end=vertices[2]),
        Edge(start=vertices[1], end=vertices[4]),
        Edge(start=vertices[2], end=vertices[3]),
        Edge(start=vertices[3], end=vertices[1]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    cycle_path = find_cycles(graph)

    class PathLogger:
        def __init__(self):
            self.path = []

        def __call__(self, vertex: Vertex):
            self.path.append(vertex)

    path_logger = PathLogger()
    cycle_path.bfs(start=vertices[1], process_vertex_early=path_logger)
    assert len(path_logger.path) == 3
    assert {v for v in vertices[1:4]} == {v for v in path_logger.path}


def test_no_cycle_found():
    vertices = [Vertex() for i in range(7)]
    edges = [
        Edge(start=vertices[0], end=vertices[1]),
        Edge(start=vertices[0], end=vertices[2]),
        Edge(start=vertices[1], end=vertices[3]),
        Edge(start=vertices[1], end=vertices[4]),
        Edge(start=vertices[2], end=vertices[5]),
        Edge(start=vertices[2], end=vertices[6]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    cycle_path = find_cycles(graph)
    assert cycle_path is None


def test_topological_sorting():
    vertices = [Vertex() for i in range(9)]
    edges = [
        Edge(start=vertices[0], end=vertices[6]),
        Edge(start=vertices[0], end=vertices[7]),
        Edge(start=vertices[6], end=vertices[3]),
        Edge(start=vertices[7], end=vertices[3]),
        Edge(start=vertices[3], end=vertices[4]),
        Edge(start=vertices[3], end=vertices[5]),
        Edge(start=vertices[1], end=vertices[8]),
        Edge(start=vertices[8], end=vertices[2]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=True)
    sorted_vertices = topological_sorting(graph)
    assert sorted_vertices.index(vertices[0]) < sorted_vertices.index(vertices[6])
    assert sorted_vertices.index(vertices[0]) < sorted_vertices.index(vertices[7])
    assert sorted_vertices.index(vertices[6]) < sorted_vertices.index(vertices[3])
    assert sorted_vertices.index(vertices[7]) < sorted_vertices.index(vertices[3])
    assert sorted_vertices.index(vertices[3]) < sorted_vertices.index(vertices[4])
    assert sorted_vertices.index(vertices[3]) < sorted_vertices.index(vertices[5])
    assert sorted_vertices.index(vertices[1]) < sorted_vertices.index(vertices[8])
    assert sorted_vertices.index(vertices[8]) < sorted_vertices.index(vertices[2])


def test_topological_sorting_fail_with_cycle():
    vertices = [Vertex() for i in range(9)]
    edges = [
        Edge(start=vertices[0], end=vertices[6]),
        Edge(start=vertices[0], end=vertices[7]),
        Edge(start=vertices[6], end=vertices[3]),
        Edge(start=vertices[7], end=vertices[3]),
        Edge(start=vertices[3], end=vertices[4]),
        Edge(start=vertices[3], end=vertices[5]),
        Edge(start=vertices[1], end=vertices[8]),
        Edge(start=vertices[8], end=vertices[2]),
        Edge(start=vertices[5], end=vertices[0]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=True)
    with pytest.raises(NotDAG):
        topological_sorting(graph)


def test_topological_sorting_fail_on_undirected_graph():
    vertices = [Vertex() for i in range(3)]
    edges = [
        Edge(start=vertices[0], end=vertices[1]),
        Edge(start=vertices[1], end=vertices[2]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    with pytest.raises(NotDAG):
        topological_sorting(graph)
