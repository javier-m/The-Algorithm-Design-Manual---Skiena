from math import inf

from datastructures import KeyedItem, Heap, UnionFind
from sorting import quicksort

from .graph import Graph, Vertex, Edge, NodeList
from .exceptions import GraphDirectionTypeError


def run_prim_algorithm(graph: Graph, start: Vertex) -> Graph:
    """O(m + n*log n) with priority queue (heap-based) implementation
    for undirected graph - works with negative edge costs
    returns the tree spanning all vertices whose sum of edge costs
    is minimal"""
    if graph.directed:
        raise GraphDirectionTypeError
    nb_vertices = graph.nb_vertices
    mst_edges = []
    processed_vertices = [start]
    nb_processed_vertices = 1

    # a list of vertices does the bookkeeping of keeping track
    # of which vertices are processed/unprocessed
    vertex_statuses = NodeList(vertices=graph.adjacency_lists,
                               default=False)

    class ItemContent:
        def __init__(self, vertex: Vertex, edge: Edge=None):
            self.vertex = vertex
            self.edge = edge

    # a heap contains all unprocessed vertices
    # their keys are the min edge cost to the in-progress MST
    # initialization in O(n + m)
    heap = Heap(heaptype='min')
    vertex_items = []
    for vertex in vertex_statuses:
        if vertex is not start:
            edge = None
            weight = inf
            for edgenode in graph.adjacency_lists[vertex].edgenodes:
                if edgenode.tail is start:
                    if edgenode.weight < weight:
                        edge = edgenode.to_edge(head=vertex)
                        weight = edgenode.weight
            vertex_item = KeyedItem(key=weight,
                                    content=ItemContent(vertex=vertex, edge=edge))
            vertex_statuses[vertex] = vertex_item
            vertex_items.append(vertex_item)
    heap.heapify(vertex_items)
    del vertex_items

    def update_heap(deleted_vertex: Vertex):
        nonlocal graph, heap, vertex_statuses
        # update status
        vertex_statuses[deleted_vertex] = False
        # remove from the heap all vertices connected to
        # the deleted vertex
        for edgenode in graph.adjacency_lists[deleted_vertex].edgenodes:
            tail = edgenode.tail
            # check if the tail is in unprocessed vertices set
            vertex_item = vertex_statuses[tail]
            if vertex_item:
                weight = vertex_item.key
                vertex = vertex_item.content.vertex
                edge = vertex_item.content.edge
                # delete it from the heap
                heap.delete(vertex_item)
                # recompute its weight
                new_weight = edgenode.weight
                if new_weight < weight:
                    weight = new_weight
                    edge = edgenode.to_edge(head=deleted_vertex)
                vertex_item = KeyedItem(key=weight,
                                        content=ItemContent(vertex=vertex, edge=edge))
                # insert it back into the heap
                heap.insert(vertex_item)

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
        update_heap(deleted_vertex=v)

    return Graph(vertices=[v for v in graph.adjacency_lists],
                 edges=mst_edges,
                 directed=False)


def run_kruskal_algorithm(graph: Graph) -> Graph:
    """O(m * log n) with union-find"""
    if graph.directed:
        raise GraphDirectionTypeError
    vertices = [v for v in graph.adjacency_lists]  # O(n)
    union_find = UnionFind(graph.adjacency_lists)  # O(n)

    # sort edges by cost
    # O(n + m)
    edges = []
    for vertex in vertices:
        for edgenode in graph.adjacency_lists[vertex].edgenodes:
            edges.append(KeyedItem(key=edgenode.weight,
                                   content=edgenode.to_edge(head=vertex)))
    # O(m * log m)
    quicksort(edges)

    mst_edges = []
    for edge_item in edges:  # m times
        edge = edge_item.content
        if union_find.find(edge.head) is not union_find.find(edge.tail):  # O(1)
            mst_edges.append(edge)
            # this one is tricky:
            # each of the n vertices has its union-find group updated at most log2(n)
            # since for it to be updated, it has to double in size
            # so in total, there are O(m) cycle checks
            # but there are O(n * log n) union-find group updates
            union_find.union(edge.head, edge.tail)

    return Graph(vertices=vertices,
                 edges=mst_edges,
                 directed=False)




