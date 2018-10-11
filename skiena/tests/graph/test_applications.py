import pytest

from graph import Vertex, Edge, Graph
from graph.applications import *
from graph.exceptions import *


def test_connected_components():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1]),
        Edge(head=vertices[1], tail=vertices[2]),
        Edge(head=vertices[2], tail=vertices[0]),
        Edge(head=vertices[3], tail=vertices[4]),
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
        Edge(head=vertices[0], tail=vertices[1]),
        Edge(head=vertices[1], tail=vertices[2]),
        Edge(head=vertices[1], tail=vertices[4]),
        Edge(head=vertices[2], tail=vertices[3]),
        Edge(head=vertices[3], tail=vertices[1]),
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
        Edge(head=vertices[0], tail=vertices[1]),
        Edge(head=vertices[0], tail=vertices[2]),
        Edge(head=vertices[1], tail=vertices[3]),
        Edge(head=vertices[1], tail=vertices[4]),
        Edge(head=vertices[2], tail=vertices[5]),
        Edge(head=vertices[2], tail=vertices[6]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    cycle_path = find_cycles(graph)
    assert cycle_path is None


def test_topological_sorting():
    vertices = [Vertex() for i in range(9)]
    edges = [
        Edge(head=vertices[0], tail=vertices[6]),
        Edge(head=vertices[0], tail=vertices[7]),
        Edge(head=vertices[6], tail=vertices[3]),
        Edge(head=vertices[7], tail=vertices[3]),
        Edge(head=vertices[3], tail=vertices[4]),
        Edge(head=vertices[3], tail=vertices[5]),
        Edge(head=vertices[1], tail=vertices[8]),
        Edge(head=vertices[8], tail=vertices[2]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=True)
    sorted_vertices = topological_sort(graph)
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
        Edge(head=vertices[0], tail=vertices[6]),
        Edge(head=vertices[0], tail=vertices[7]),
        Edge(head=vertices[6], tail=vertices[3]),
        Edge(head=vertices[7], tail=vertices[3]),
        Edge(head=vertices[3], tail=vertices[4]),
        Edge(head=vertices[3], tail=vertices[5]),
        Edge(head=vertices[1], tail=vertices[8]),
        Edge(head=vertices[8], tail=vertices[2]),
        Edge(head=vertices[5], tail=vertices[0]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=True)
    with pytest.raises(CycleInGraphError):
        topological_sort(graph)


def test_topological_sorting_fail_on_undirected_graph():
    vertices = [Vertex() for i in range(3)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1]),
        Edge(head=vertices[1], tail=vertices[2]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    with pytest.raises(GraphDirectionTypeError):
        topological_sort(graph)


def test_strongly_connected_components():
    vertices = [Vertex() for i in range(9)]
    edges = [
        Edge(head=vertices[0], tail=vertices[6]),
        Edge(head=vertices[6], tail=vertices[3]),
        Edge(head=vertices[3], tail=vertices[0]),
        Edge(head=vertices[6], tail=vertices[8]),
        Edge(head=vertices[8], tail=vertices[5]),
        Edge(head=vertices[5], tail=vertices[2]),
        Edge(head=vertices[2], tail=vertices[8]),
        Edge(head=vertices[5], tail=vertices[7]),
        Edge(head=vertices[5], tail=vertices[7]),
        Edge(head=vertices[7], tail=vertices[1]),
        Edge(head=vertices[1], tail=vertices[4]),
        Edge(head=vertices[4], tail=vertices[7]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=True)
    ssc_list = find_strongly_connected_components(graph)
    assert len(ssc_list) == 3
    ssc_1 = {vertices[0], vertices[6], vertices[3]}
    ssc_2 = {vertices[8], vertices[5], vertices[2]}
    ssc_3 = {vertices[7], vertices[1], vertices[4]}

    for i in range(3):
        ssc = {v for v in ssc_list[i]}
        assert ssc in [ssc_1, ssc_2, ssc_3]


def test_strongly_connected_components_fail_on_undirected_graph():
    vertices = [Vertex() for i in range(3)]
    edges = [
        Edge(head=vertices[0], tail=vertices[1]),
        Edge(head=vertices[1], tail=vertices[2]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    with pytest.raises(GraphDirectionTypeError):
        find_strongly_connected_components(graph)
