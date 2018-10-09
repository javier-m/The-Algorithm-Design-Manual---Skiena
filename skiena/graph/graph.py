from typing import Sequence, Callable, Any

from datastructures import LinkedList, Queue, QueueEmptyError


class Vertex:
    nb_of_instances = 0

    def __init__(self, **kwargs):
        Vertex.nb_of_instances += 1
        self._id = Vertex.nb_of_instances
        self._kwargs = kwargs

    @property
    def id(self):
        return self._id

    def __repr__(self) -> str:
        vertex_repr = f'V#{self.id}'
        kwargs_repr = ' '.join([f'{kwarg}={value}' for kwarg, value in self._kwargs.items()])
        return vertex_repr + ' ' + kwargs_repr if kwargs_repr else vertex_repr


class Edge:
    def __init__(self, start: Vertex, end: Vertex, weight: float=None, **kwargs):
        self.start = start
        self.end = end
        self.weight = weight
        self._kwargs = kwargs
        for kwarg, value in kwargs.items():
            setattr(self, kwarg, value)

    def __repr__(self) -> str:
        edge_repr = repr(self.start) + ' -> ' + repr(self.end) + f' - weight={self.weight}'
        kwargs_repr = ' '.join([f'{kwarg}={value}' for kwarg, value in self._kwargs.items()])
        return edge_repr + ' ' + kwargs_repr if kwargs_repr else edge_repr


class Edgenode:
    def __init__(self, start: Vertex, edge: Edge):
        if start is edge.start:
            end = edge.end
        elif start is edge.end:
            end = edge.start
        else:
            raise Exception('Starting vertex not in this edge')
        self.end = end
        self.weight = edge.weight
        for kwarg, value in edge._kwargs.items():
            setattr(self, kwarg, value)


class AdjacencyList:
    def __init__(self, start: Vertex):
        self.start = start
        self.connected_vertices = LinkedList()
        self.degree = 0

    def connect(self, edge: Edge):
        self.connected_vertices.insert(Edgenode(start=self.start, edge=edge))
        self.degree += 1


class NodeList:
    def __init__(self, vertices: Sequence[Vertex], default=None):
        self._dict = {v.id: default for v in vertices}
        self._vertices = vertices

    def __setitem__(self, key: Vertex, value):
        if key not in self._vertices:
            raise KeyError(key)
        self._dict[key.id] = value

    def __getitem__(self, key: Vertex) -> Any:
        if key not in self._vertices:
            raise KeyError(key)
        return self._dict[key.id]

    def __contains__(self, key: Vertex) -> bool:
        return key.id in self._dict

    def __iter__(self):
        for v in self._vertices:
            yield v


class Graph:
    """Adjancency list-based"""
    def __init__(self,
                 vertices: Sequence[Vertex],
                 edges: Sequence[Edge],
                 directed: bool=False):
        self.nb_vertices = len(vertices)
        self.nb_edges = len(edges) if directed else 2*len(edges)
        self.directed = directed
        # create nodelists
        self.adjacency_lists = NodeList(vertices=vertices)
        for vertex in vertices:
            self.adjacency_lists[vertex] = AdjacencyList(start=vertex)
        self.parents = NodeList(vertices=vertices)
        # build adjacency lists
        for edge in edges:
            self.adjacency_lists[edge.start].connect(edge)
            if not directed:
                self.adjacency_lists[edge.end].connect(edge)

    def bfs(self,
            start: Vertex,
            process_vertex_early: Callable[[Vertex], Any]=None,
            process_vertex_late: Callable[[Vertex], Any]=None,
            process_edge: Callable[[Edgenode], Any]=None):
        process_vertex_early = process_vertex_early if process_vertex_early else lambda v: None
        process_vertex_late = process_vertex_late if process_vertex_late else lambda v: None
        process_edge = process_edge if process_edge else lambda v1, v2: None
        vertices = [v for v in self.adjacency_lists]
        discovered = NodeList(vertices=vertices)
        processed = NodeList(vertices=vertices)
        discovered[start] = True
        queue = Queue(implementation='doubly_linked_list')
        queue.enqueue(start)
        while True:
            try:
                vertex = queue.dequeue()
            except QueueEmptyError:
                break
            processed[vertex] = True
            process_vertex_early(vertex)
            adjacency_list = self.adjacency_lists[vertex]
            for edgenode in adjacency_list.connected_vertices:
                next_vertex = edgenode.end
                if not processed[next_vertex] or self.directed:
                    process_edge(vertex, next_vertex)
                if not discovered[next_vertex]:
                    discovered[next_vertex] = True
                    self.parents[next_vertex] = vertex
                    queue.enqueue(next_vertex)
            process_vertex_late(vertex)


