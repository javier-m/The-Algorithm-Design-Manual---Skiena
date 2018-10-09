from typing import Sequence

from .graph import Graph, NodeList


def find_connected_components(graph: Graph) -> Sequence[Graph]:
    """find connected components for undirected graph"""
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
