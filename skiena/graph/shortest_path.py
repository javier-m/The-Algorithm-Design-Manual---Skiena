from typing import List
from math import inf

from datastructures import KeyedItem, Heap, Stack, StackEmptyError

from .graph import Graph, Vertex, Edge, NodeList, Edgenode
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


def run_floyd_warshall_algorithm(graph: Graph) -> NodeList:
    """O(n**3)"""
    # convert adjacency-list-based graph into adjacency matrix
    distances = NodeList(vertices=graph.adjacency_lists)
    for vertex in distances:
        distances[vertex] = NodeList(vertices=graph.adjacency_lists,
                                     default=inf)
        distances[vertex][vertex] = 0
        for edgenode in graph.adjacency_lists[vertex].edgenodes:
            tail = edgenode.tail
            if edgenode.weight < 0:
                raise GraphTypeError
            if edgenode.weight < distances[vertex][tail]:
                distances[vertex][tail] = edgenode.weight 

    for v_k in distances:
        for v_i in distances:
            for v_j in distances[v_i]:
                dist_v_i_v_j = distances[v_i][v_j]
                dist_v_i_v_k_v_j = distances[v_i][v_k] + distances[v_k][v_j]
                if dist_v_i_v_k_v_j < dist_v_i_v_j:
                    distances[v_i][v_j] = dist_v_i_v_k_v_j

    return distances


def find_network_flow(graph: Graph,
                      source: Vertex,
                      sink: Vertex) -> [float, Graph]:
    # initialize by creating residual graph
    edges = []
    for vertex in graph.adjacency_lists:
        for edgenode in graph.adjacency_lists[vertex].edgenodes:
            edge = edgenode.to_edge(head=vertex)
            edge.flow = 0
            edge.residual = edgenode.weight
            edge.opposite = None
            edges.append(edge)
            opposite_edge = edgenode.to_edge(head=vertex)
            opposite_edge.head, opposite_edge.tail = opposite_edge.tail, opposite_edge.head
            opposite_edge.flow = 0
            opposite_edge.residual = 0
            opposite_edge.opposite = edge
            edge.opposite = opposite_edge
            edges.append(opposite_edge)
    graph = Graph(vertices=[v for v in graph.adjacency_lists],
                  edges=edges,
                  directed=True)

    def is_edge_processable(head: Vertex, edgenode: Edgenode):
        return True if edgenode.residual > 0 else False

    def calculate_path_volume(graph: Graph,
                              start: Vertex,
                              end: Vertex) -> float:
        stack = Stack(implementation='linked_list')
        parent_edges = graph.parent_edges
        while True:
            edge = parent_edges[end]
            if edge:
                stack.push(edge)
                end = edge.head
                if end is start:
                    break
            else:
                return 0
        volume = inf
        while True:
            try:
                volume = min(volume, stack.pop().residual)
            except StackEmptyError:
                break
        return volume

    def augment_path(graph: Graph,
                     start: Vertex,
                     end: Vertex,
                     volume: float):
        stack = Stack(implementation='linked_list')
        parent_edges = graph.parent_edges
        while True:
            edge = parent_edges[end]
            if edge:
                stack.push(edge)
                end = edge.head
                if end is start:
                    break
            else:
                break
        while True:
            try:
                edge = stack.pop()
            except StackEmptyError:
                break
            else:
                edge.edgenode.flow += volume
                edge.edgenode.residual -= volume
                edge.edgenode.opposite.residual += volume

    graph.bfs(start=source,
              is_edge_processable=is_edge_processable)  # get parent_edges at each BFS
    volume = 0
    new_volume = calculate_path_volume(graph=graph,
                                       start=source,
                                       end=sink)
    while new_volume > 0:
        volume += new_volume
        augment_path(graph=graph,
                     start=source,
                     end=sink,
                     volume=new_volume)
        graph.bfs(start=source,
                  is_edge_processable=is_edge_processable)  # get parent_edges at each BFS
        new_volume = calculate_path_volume(graph=graph,
                                           start=source,
                                           end=sink)

    return volume, graph
