from typing import Sequence, List

from datastructures import Stack, StackEmptyError

from .graph import Graph, NodeList, Vertex, Edgenode, EdgeType
from .exceptions import *


def find_connected_components(graph: Graph) -> Sequence[Graph]:
    """BFS: finds connected components for undirected graph"""
    connected_components = []
    vertices = [v for v in graph.adjacency_lists]
    processed_vertices = NodeList(vertices, default=False)

    def process_vertex_late(vertex: Vertex):
        nonlocal processed_vertices
        processed_vertices[vertex] = True

    for v in vertices:
        if not processed_vertices[v]:
            connected_component = graph.bfs(start=v,
                                            process_vertex_late=process_vertex_late)
            connected_components.append(connected_component)
    return connected_components


def find_cycles(graph: Graph) -> Graph:
    """DFS: returns first cycle found if any for undirected graph"""
    vertices = [v for v in graph.adjacency_lists]

    class CycleFound(Exception):
        def __init__(self, start, end, *args, **kwargs):
            Exception.__init__(self, *args, **kwargs)
            self.start = start
            self.end = end

    def process_edge(head: Vertex, edgenode: Edgenode):
        nonlocal graph
        # check if there is a parent-child relationship
        tail = edgenode.tail
        if not ((graph.parent_edges[tail]
                 and graph.parent_edges[tail].head is head)
                or (graph.parent_edges[head]
                    and graph.parent_edges[head].head is tail)):
            raise CycleFound(start=tail, end=head)

    for v in vertices:
        try:
            graph.dfs(start=v, process_edge=process_edge)
        except CycleFound as e:
            return graph.find_path(start=e.start, end=e.end)
    return None


def topological_sort(graph: Graph) -> List[Vertex]:
    """DFS: returns the list of topologically-ordered vertices in a
    Directed Acyclic Graph (DAG)"""
    if not graph.directed:
        raise GraphDirectionTypeError

    vertices = [v for v in graph.adjacency_lists]

    stack = Stack(implementation='linked_list')
    discovered_vertices = NodeList(vertices, default=False)
    processed_vertices = NodeList(vertices, default=False)
    sorted_vertices = []

    def process_vertex_early(vertex: Vertex):
        nonlocal discovered_vertices
        discovered_vertices[vertex] = True

    def process_vertex_late(vertex: Vertex):
        nonlocal stack, processed_vertices
        processed_vertices[vertex] = True
        stack.push(vertex)

    def process_edge(head: Vertex, edgenode: Edgenode):
        # check that the edge is not a back edge
        if edgenode.edgetype is EdgeType.BACK:
            raise CycleInGraphError

    for v in vertices:
        if not discovered_vertices[v]:
            graph.dfs(start=v,
                      process_vertex_early=process_vertex_early,
                      process_vertex_late=process_vertex_late,
                      process_edge=process_edge,
                      discovered_vertices=discovered_vertices,
                      processed_vertices=processed_vertices)

    while True:
        try:
            sorted_vertices.append(stack.pop())
        except StackEmptyError:
            break

    return sorted_vertices


def find_strongly_connected_components(graph: Graph) -> List[List[Vertex]]:
    """DFS-based: returns the list of strongly-connected components"""
    if not graph.directed:
        raise GraphDirectionTypeError

    vertices = [v for v in graph.adjacency_lists]
    sscs = NodeList(vertices, default=None)
    # leaders are the list of the oldest vertices to be known to be
    # in the same SSC than each vertex
    leaders = NodeList(vertices, default=None)
    for v in leaders:
        leaders[v] = v

    discovered_vertices = NodeList(vertices, default=False)
    processed_vertices = NodeList(vertices, default=False)

    stack = Stack(implementation='linked_list')

    def process_vertex_early(vertex: Vertex):
        nonlocal stack
        stack.push(vertex)

    sscs_found = 0

    def process_vertex_late(vertex: Vertex):
        nonlocal graph, leaders, sscs, sscs_found, stack
        if leaders[vertex] is vertex:
            sscs_found += 1
            sscs[vertex] = sscs_found
            while True:
                try:
                    v = stack.pop()
                except StackEmptyError:
                    break
                if v is vertex:
                    break
                sscs[v] = sscs_found
        parent_edge = graph.parent_edges[vertex]
        if parent_edge:
            parent = parent_edge.head
            if leaders[vertex].entry_time < leaders[parent].entry_time:
                leaders[parent] = leaders[vertex]

    def process_edge(head: Vertex, edgenode: Edgenode):
        nonlocal leaders, sscs
        tail = edgenode.tail
        # forward edges do not contribute to SSC
        # a back edge makes a SSC
        if edgenode.edgetype is EdgeType.BACK:
            # tail is in the same SSC than head
            # check if it is older than currrent leaders[head]
            if tail.entry_time < leaders[head].entry_time:
                leaders[head] = tail
        # for cross edges:
        # - either there is already a fully-formed SSC found
        # then it means it is one-way only
        # - or 
        elif edgenode.edgetype is EdgeType.CROSS:
            if sscs[tail] is None:  # SSC not assigned yet
                if tail.entry_time < leaders[head].entry_time:
                    leaders[head] = tail

    for v in vertices:
        if not discovered_vertices[v]:
            graph.dfs(start=v,
                      process_vertex_early=process_vertex_early,
                      process_vertex_late=process_vertex_late,
                      process_edge=process_edge,
                      discovered_vertices=discovered_vertices,
                      processed_vertices=processed_vertices)

    ssc_list = [[] for i in range(sscs_found)]
    for v in sscs:
        ssc_list[sscs[v]-1].append(v)

    return ssc_list


