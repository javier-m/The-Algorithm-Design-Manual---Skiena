from datastructures import Heap

from .graph import Graph, Vertex, Edge
from .exceptions import GraphDirectionTypeError


def prim_algorithm(graph: Graph, start: Vertex) -> Graph:
    """O(m + n*log n) with priority queue (heap-based) implementation
    for undirected graph - works negative with edge costs
    returns the tree spanning all vertices whose sum of edge costs
    is minimal"""
    if graph.directed:
        raise GraphDirectionTypeError
    vertices = ...
    nb_vertices = graph.nb_vertices
    mst_edges = []
    processed_vertices = [start]
    nb_processed_vertices = 1

    class HeapItemContent:
        def __init__(self, vertex: Vertex, edge: Edge):
            self.vertex = vertex
            self.edge = edge

    

    heap = Heap(heaptype='min')
    # initialize heap
    for edgenode in graph.adjacency_lists[start].edgenodes:
        heap.insert()

    def update_heap(...):
        nonlocal heap
        pass

    while nb_processed_vertices < nb_vertices:
        # pick cheapest edge crossing the cut
        # from the graph mst_graph = (processed_vertices, mst_edges)
        # to the graph graph - mst_graph
        heap_item = heap.extract_root()
        e = heap_item.content.edge
        v = heap_item.content.vertex
        # add it to the list of the Minimum Spanning Tree edges
        mst_edges.append(e)
        # add its tail to thelist of processed vertices
        processed_vertices.append(v)
        # update nb_processed_vertices
        nb_processed_vertices += 1
        # update heap
        ...
        
    return Graph(vertices=vertices, edges=mst_edges, directed=False)
