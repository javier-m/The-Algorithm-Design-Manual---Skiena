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
