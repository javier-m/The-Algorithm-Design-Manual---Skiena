from typing import Sequence, List

from datastructures import Stack, StackEmptyError

from .graph import Graph, NodeList, Vertex, Edgenode, EdgeType


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

    def process_edge(start: Vertex, edgenode: Edgenode):
        nonlocal graph
        # check if there is a parent-child relationship
        end = edgenode.end
        if not ((graph.parent_edges[end]
                 and graph.parent_edges[end].start is start)
                or (graph.parent_edges[start]
                    and graph.parent_edges[start].start is end)):
            raise CycleFound(start=end, end=start)

    for v in vertices:
        try:
            graph.dfs(start=v, process_edge=process_edge)
        except CycleFound as e:
            return graph.find_path(start=e.start, end=e.end)
    return None


class NotDAG(Exception):
    """raised when a directed graph is detected as having a cycle"""
    pass


def topological_sorting(graph: Graph) -> List:
    """DFS: returns the list of topologically-ordered vertices in a
    Directed Acyclic Graph (DAG)"""
    vertices = [v for v in graph.adjacency_lists]

    stack = Stack(implementation='linked_list')
    discovered_vertices = NodeList(vertices, default=False)
    processed_vertices = NodeList(vertices, default=False)
    ordered_vertices = []

    def process_vertex_early(vertex: Vertex):
        nonlocal discovered_vertices
        discovered_vertices[vertex] = True

    def process_vertex_late(vertex: Vertex):
        nonlocal stack, processed_vertices
        processed_vertices[vertex] = True
        stack.push(vertex)

    def process_edge(start: Vertex, edgenode: Edgenode):
        # check that the edge is not a back edge
        if edgenode.edgetype is EdgeType.BACK:
            raise NotDAG

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
            ordered_vertices = stack.pop()
        except StackEmptyError:
            break

    return ordered_vertices
