from math import inf

from datastructures import KeyedItem, Heap

from .graph import Graph, Vertex, Edge, NodeList
from .exceptions import *


def run_dijkstra_algorithm(graph: Graph,
                           source: Vertex) -> NodeList:
    nb_processed_vertices = 1
    nb_vertices = graph.nb_vertices
    shortest_paths = NodeList(vertices=graph.adjacency_lists)

    # a list of vertices does the bookkeeping of keeping track
    # of which vertices are processed/unprocessed
    vertex_statuses = NodeList(vertices=graph.adjacency_lists,
                               default=False)

    class ItemContent:
        def __init__(self, vertex: Vertex, edge: Edge=None):
            self.vertex = vertex
            self.edge = edge

    class Path:
        def __init__(self, source: Vertex):
            self.source = source
            self.destination = None
            self.path_to_last_hop = None
            self.last_hop = None
            self.distance = None

        def build(self, path_to_last_hop, last_hop: Edge):
            if self.source is not path_to_last_hop.source:
                raise PathError
            if path_to_last_hop.destination is not last_hop.head:
                raise PathError
            self.path_to_last_hop = path_to_last_hop
            self.last_hop = last_hop
            self.destination = last_hop.tail
            self.distance = path_to_last_hop.distance + last_hop.weight

    # a heap contains all vertices not in the path
    # their keys are the min distance to the source vertex
    # initialization in O(n + m)
    heap = Heap(heaptype='min')
    for vertex in graph.adjacency_lists:
        shortest_paths[vertex] = Path(source=source)
        shortest_paths[vertex].distance = inf

    shortest_paths[source].destination = source
    shortest_paths[source].distance = 0

    for edgenode in graph.adjacency_lists[source].edgenodes:
        tail = edgenode.tail
        if edgenode.weight < 0:
            raise GraphTypeError
        if shortest_paths[tail].distance is not None and edgenode.weight < shortest_paths[tail].distance:
            shortest_paths[tail].destination = tail
            shortest_paths[tail].last_hop = edgenode.to_edge(head=source)
            shortest_paths[tail].distance = edgenode.weight

    vertex_items = []
    for vertex in graph.adjacency_lists:
        if vertex is not source:
            vertex_item = KeyedItem(key=shortest_paths[vertex].distance,
                                    content=ItemContent(vertex=vertex,
                                                        edge=shortest_paths[vertex].last_hop))
            vertex_items.append(vertex_item)
            vertex_statuses[vertex] = vertex_item

    heap.heapify(vertex_items)
    del vertex_items

    def update_heap(deleted_vertex: Vertex, distance_to_deleted_vertex: float):
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
                distance = vertex_item.key
                vertex = vertex_item.content.vertex
                edge = vertex_item.content.edge
                # delete it from the heap
                heap.delete(vertex_item)
                # recompute its distance
                if edgenode.weight < 0:
                    raise GraphTypeError
                new_distance = distance_to_deleted_vertex + edgenode.weight
                if new_distance < distance:
                    distance = new_distance
                    edge = edgenode.to_edge(head=deleted_vertex)
                vertex_item.key = distance
                vertex_item.content = ItemContent(vertex=vertex, edge=edge)
                # insert it back into the heap
                heap.insert(vertex_item)

    while nb_processed_vertices < nb_vertices:
        # pick cheapest edge crossing the cut
        # from the graph shortest_path_tree = (processed_vertices, paths)
        # to the graph graph - shortest_path_tree
        heap_item = heap.extract_root()
        last_hop = heap_item.content.edge
        v = heap_item.content.vertex
        # add it to the path leading to v
        shortest_paths[v].build(path_to_last_hop=shortest_paths[last_hop.head],
                                last_hop=last_hop)
        # update nb_processed_vertices
        nb_processed_vertices += 1
        # update heap
        update_heap(deleted_vertex=v, distance_to_deleted_vertex=shortest_paths[v].distance)

    return shortest_paths
