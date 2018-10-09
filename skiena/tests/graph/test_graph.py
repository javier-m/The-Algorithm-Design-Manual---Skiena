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
