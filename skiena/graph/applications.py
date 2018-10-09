from typing import Sequence

from .graph import Graph, NodeList, Vertex


def find_connected_components(graph: Graph) -> Sequence[Graph]:
    """BFS: find connected components for undirected graph"""
    connected_components = []
    vertices = [v for v in graph.adjacency_lists]
    processed = NodeList(vertices, default=False)
    for v in vertices:
        if not processed[v]:
            connected_component = graph.bfs(start=v)
            connected_components.append(connected_component)
            for w in connected_component.adjacency_lists:
                processed[w] = True
    return connected_components


def find_cycles(graph: Graph) -> Graph:
    """DFS: return first cycle found if any for undirected graph"""
    vertices = [v for v in graph.adjacency_lists]

    class CycleFound(Exception):
        def __init__(self, start, end, *args, **kwargs):
            Exception.__init__(self, *args, **kwargs)
            self.start = start
            self.end = end

    def process_edge(start: Vertex, end: Vertex):
        nonlocal graph
        # check if there is a parent-child relationship
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
