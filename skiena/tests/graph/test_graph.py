import re
import pytest

from graph import Vertex, Edge, Graph
from graph.graph import Edgenode, AdjacencyList, NodeList


def test_repr_vertex():
    v1 = Vertex()
    v2 = Vertex(a=1, b=2)
    assert re.match(r'^V#\d+$', repr(v1))
    assert re.match(r'^V#\d+\sa=1\sb=2$', repr(v2))


def test_repr_edge():
    v1 = Vertex()
    v2 = Vertex(a=1, b=2)
    e1 = Edge(v1, v2)
    e2 = Edge(v1, v2, weight=1, c=3, d=4)
    assert re.match(r'^V#\d+\s->\sV#\d+\sa=1\sb=2\s-\sweight=None$', repr(e1))
    assert re.match(r'^V#\d+\s->\sV#\d+\sa=1\sb=2\s-\sweight=1\sc=3\sd=4$', repr(e2))


def test_edgenode_with_start_vertex_as_second_arg():
    v1 = Vertex()
    v2 = Vertex()
    e = Edge(v1, v2)
    edgenode = Edgenode(start=v2, edge=e)
    assert edgenode.end is v1


def test_edgenode_with_extra_args():
    v1 = Vertex()
    v2 = Vertex()
    e = Edge(v1, v2, a=1, b=2)
    edgenode = Edgenode(start=v1, edge=e)
    assert edgenode.end is v2
    assert (edgenode.a, edgenode.b) == (1, 2)


def test_wrong_node_for_edgenode():
    v1 = Vertex()
    v2 = Vertex(a=1, b=2)
    v3 = Vertex()
    e1 = Edge(v1, v2, weight=1, c=3, d=4)
    with pytest.raises(Exception):
        Edgenode(start=v3, edge=e1)


def test_adjacency_list():
    v = Vertex()
    vertices = [Vertex() for i in range(4)]
    edges = [Edge(v, w) for w in vertices]
    adjacency_list = AdjacencyList(start=v)
    for edge in edges:
        adjacency_list.connect(edge)
    i = 4
    for edgenode in adjacency_list.connected_vertices:
        i -= 1
        assert edgenode.end is vertices[i]
    assert adjacency_list.degree == 4


def test_set_and_get_nodelist():
    vertices = [Vertex() for i in range(4)]
    nodelist = NodeList(vertices)
    for i, v in enumerate(vertices):
        nodelist[v] = i
    for i, v in enumerate(vertices):
        assert nodelist[v] == i


def test_fail_set_and_get_nodelist():
    vertices = [Vertex() for i in range(4)]
    nodelist = NodeList(vertices)
    v = Vertex()
    with pytest.raises(KeyError):
        nodelist[v] = 3
    with pytest.raises(KeyError):
        nodelist[v]


def test_contains_nodelist():
    vertices = [Vertex() for i in range(4)]
    nodelist = NodeList(vertices)
    for v in vertices:
        assert v in nodelist


def test_iter_nodelist():
    vertices = [Vertex() for i in range(4)]
    nodelist = NodeList(vertices)
    set_of_vertices = {v for v in vertices}
    set_of_iterated_vertices = {v for v in nodelist}
    assert set_of_vertices == set_of_iterated_vertices


def test_undirected_bfs():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(vertices[0], vertices[1]),
        Edge(vertices[0], vertices[4]),
        Edge(vertices[0], vertices[5]),
        Edge(vertices[1], vertices[2]),
        Edge(vertices[1], vertices[4]),
        Edge(vertices[2], vertices[3]),
        Edge(vertices[3], vertices[4]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    graph.bfs(start=vertices[0])
    assert graph.parent_edges[vertices[0]] is None
    assert graph.parent_edges[vertices[1]].start is vertices[0]
    assert graph.parent_edges[vertices[2]].start is vertices[1]
    assert graph.parent_edges[vertices[3]].start is vertices[4]
    assert graph.parent_edges[vertices[4]].start is vertices[0]
    assert graph.parent_edges[vertices[5]].start is vertices[0]


def test_directed_bfs():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(vertices[0], vertices[1]),
        Edge(vertices[0], vertices[2]),
        Edge(vertices[1], vertices[3]),
        Edge(vertices[2], vertices[3]),
        Edge(vertices[3], vertices[4]),
        Edge(vertices[3], vertices[5]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=True)
    graph.bfs(start=vertices[0])
    assert graph.parent_edges[vertices[0]] is None
    assert graph.parent_edges[vertices[1]].start is vertices[0]
    assert graph.parent_edges[vertices[2]].start is vertices[0]
    assert graph.parent_edges[vertices[3]].start is vertices[1] or graph.parent_edges[vertices[3]].start is vertices[2]
    assert graph.parent_edges[vertices[4]].start is vertices[3]
    assert graph.parent_edges[vertices[5]].start is vertices[3]


def test_undirected_dfs():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(vertices[0], vertices[1]),
        Edge(vertices[0], vertices[4]),
        Edge(vertices[0], vertices[5]),
        Edge(vertices[1], vertices[2]),
        Edge(vertices[2], vertices[3]),
        Edge(vertices[3], vertices[4]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=False)
    entry_and_exit_times = graph.dfs(start=vertices[0])
    assert graph.parent_edges[vertices[0]] is None
    assert (entry_and_exit_times[vertices[0]].entry, entry_and_exit_times[vertices[0]].exit) == (0, 11)
    if graph.parent_edges[vertices[1]].start is vertices[0]:
        assert entry_and_exit_times[vertices[1]].exit - entry_and_exit_times[vertices[1]].entry == 7
        assert graph.parent_edges[vertices[2]].start is vertices[1]
        assert entry_and_exit_times[vertices[2]].exit - entry_and_exit_times[vertices[2]].entry == 5
        assert graph.parent_edges[vertices[3]].start is vertices[2]
        assert entry_and_exit_times[vertices[3]].exit - entry_and_exit_times[vertices[3]].entry == 3
        assert graph.parent_edges[vertices[4]].start is vertices[3]
        assert entry_and_exit_times[vertices[4]].exit - entry_and_exit_times[vertices[4]].entry == 1
    else:
        assert graph.parent_edges[vertices[1]].start is vertices[2]
        assert entry_and_exit_times[vertices[1]].exit - entry_and_exit_times[vertices[1]].entry == 1
        assert graph.parent_edges[vertices[2]].start is vertices[3]
        assert entry_and_exit_times[vertices[2]].exit - entry_and_exit_times[vertices[2]].entry == 3
        assert graph.parent_edges[vertices[3]].start is vertices[4]
        assert entry_and_exit_times[vertices[3]].exit - entry_and_exit_times[vertices[3]].entry == 5
        assert graph.parent_edges[vertices[4]].start is vertices[0]
        assert entry_and_exit_times[vertices[4]].exit - entry_and_exit_times[vertices[4]].entry == 7
    assert graph.parent_edges[vertices[5]].start is vertices[0]
    assert entry_and_exit_times[vertices[5]].exit - entry_and_exit_times[vertices[5]].entry == 1


def test_directed_dfs():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(vertices[0], vertices[1]),
        Edge(vertices[0], vertices[2]),
        Edge(vertices[1], vertices[3]),
        Edge(vertices[2], vertices[3]),
        Edge(vertices[3], vertices[4]),
        Edge(vertices[3], vertices[5]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=True)
    entry_and_exit_times = graph.dfs(start=vertices[0])
    assert graph.parent_edges[vertices[0]] is None
    assert (entry_and_exit_times[vertices[0]].entry, entry_and_exit_times[vertices[0]].exit) == (0, 11)
    assert graph.parent_edges[vertices[1]].start is vertices[0]
    assert graph.parent_edges[vertices[2]].start is vertices[0]
    assert graph.parent_edges[vertices[3]].start is vertices[1] or graph.parent_edges[vertices[3]].start is vertices[2]
    if graph.parent_edges[vertices[3]].start is vertices[1]:
        assert (entry_and_exit_times[vertices[1]].entry, entry_and_exit_times[vertices[1]].exit) == (1, 8)
        assert (entry_and_exit_times[vertices[2]].entry, entry_and_exit_times[vertices[2]].exit) == (9, 10)
    else:
        assert (entry_and_exit_times[vertices[2]].entry, entry_and_exit_times[vertices[2]].exit) == (1, 8)
        assert (entry_and_exit_times[vertices[1]].entry, entry_and_exit_times[vertices[1]].exit) == (9, 10)
    assert (entry_and_exit_times[vertices[3]].entry, entry_and_exit_times[vertices[3]].exit) == (2, 7)
    assert graph.parent_edges[vertices[4]].start is vertices[3]
    assert entry_and_exit_times[vertices[4]].exit - entry_and_exit_times[vertices[4]].entry == 1    
    assert graph.parent_edges[vertices[5]].start is vertices[3]
    assert entry_and_exit_times[vertices[5]].exit - entry_and_exit_times[vertices[5]].entry == 1


def test_path_finder():
    vertices = [Vertex() for i in range(6)]
    edges = [
        Edge(vertices[0], vertices[1]),
        Edge(vertices[0], vertices[4]),
        Edge(vertices[0], vertices[5]),
        Edge(vertices[1], vertices[2]),
        Edge(vertices[1], vertices[4]),
        Edge(vertices[2], vertices[3]),
        Edge(vertices[3], vertices[4]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=True)
    graph.bfs(start=vertices[0])
    path = graph.find_path(start=vertices[0], end=vertices[2])

    class PathLogger:
        def __init__(self):
            self.path = []

        def __call__(self, vertex: Vertex):
            self.path.append(vertex)

    path_logger = PathLogger()
    path.bfs(start=vertices[0], process_vertex_early=path_logger)
    for i in range(3):
        assert path_logger.path[i] is vertices[i]


def test_path_finder_fail():
    vertices = [Vertex() for i in range(4)]
    edges = [
        Edge(vertices[0], vertices[1]),
        Edge(vertices[1], vertices[2]),
        Edge(vertices[2], vertices[0]),
        Edge(vertices[2], vertices[3]),
    ]
    graph = Graph(vertices=vertices, edges=edges, directed=True)
    graph.bfs(start=vertices[0])
    with pytest.raises(Exception):
        graph.find_path(start=vertices[3], end=vertices[1])


