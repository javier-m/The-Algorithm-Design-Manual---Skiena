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
