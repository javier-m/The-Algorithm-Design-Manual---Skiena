from typing import Sequence, Callable, Any
from enum import Enum

from datastructures import (LinkedList,
                            Queue,
                            QueueEmptyError,
                            Stack,
                            StackEmptyError)


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


class EdgeType(Enum):
    TREE = 1
    BACK = 2
    FORWARD = 3
    CROSS = 4


class Edge:
    def __init__(self, start: Vertex, end: Vertex, weight: float=None, edgetype: EdgeType=None, **kwargs):
        self.start = start
        self.end = end
        self.weight = weight
        self.edgetype = edgetype
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
        self.edgetype = edge.edgetype
        self._kwargs = edge._kwargs
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
        self.parent_edges = NodeList(vertices=vertices)
        # build adjacency lists
        for edge in edges:
            self.adjacency_lists[edge.start].connect(edge)
            if not directed:
                self.adjacency_lists[edge.end].connect(edge)

    def find_path(self, start: Vertex, end: Vertex):
        """return the path from start to end vertices as a graph"""
        vertice_stack = Stack(implementation='linked_list')
        edge_stack = Stack(implementation='linked_list')
        for i in range(self.nb_vertices):
            vertice_stack.push(end)
            if end is start:
                break
            edge = self.parent_edges[end]
            if edge:
                edge_stack.push(edge)
                end = edge.start
            else:
                raise Exception(f'No path found between {start} and {end}')
        else:
            raise Exception(f'No path found between {start} and {end}')
        vertices = []
        while True:
            try:
                vertices.append(vertice_stack.pop())
            except StackEmptyError:
                break
        edges = []
        while True:
            try:
                edges.append(edge_stack.pop())
            except StackEmptyError:
                break

        return Graph(vertices=vertices, edges=edges, directed=True)

    def bfs(self,
            start: Vertex,
            process_vertex_early: Callable[[Vertex], Any]=None,
            process_vertex_late: Callable[[Vertex], Any]=None,
            process_edge: Callable[[Vertex, Edgenode], Any]=None,
            discovered_vertices: NodeList=None,
            processed_vertices: NodeList=None):
        """Breadth-First Search
        returns the graph of processed vertices - one single connected component"""
        process_vertex_early = process_vertex_early if process_vertex_early else lambda v: None
        process_vertex_late = process_vertex_late if process_vertex_late else lambda v: None
        process_edge = process_edge if process_edge else lambda v, e: None

        vertices = [v for v in self.adjacency_lists]
        self.parent_edges = NodeList(vertices=vertices)  # reinit parents
        discovered = NodeList(vertices=vertices) if discovered_vertices is None else discovered_vertices  # added to stack
        processed = NodeList(vertices=vertices) if processed_vertices is None else processed_vertices  # processed and out of stack
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
                    process_edge(vertex, edgenode)
                if not discovered[next_vertex]:
                    discovered[next_vertex] = True
                    self.parent_edges[next_vertex] = Edge(start=vertex,
                                                          end=next_vertex,
                                                          weight=edgenode.weight,
                                                          edgetype=edgenode.edgetype,
                                                          **edgenode._kwargs)
                    queue.enqueue(next_vertex)
            process_vertex_late(vertex)
        processed_vertices = [v for v in processed if processed[v]]
        processed_edges = []
        for processed_vertex in processed_vertices:
            adjacency_list = self.adjacency_lists[processed_vertex]
            for edgenode in adjacency_list.connected_vertices:
                processed_edges.append(
                    Edge(start=processed_vertex,
                         end=edgenode.end,
                         weight=edgenode.weight,
                         **edgenode._kwargs)
                    )
        return Graph(vertices=processed_vertices,
                     edges=processed_edges,
                     directed=self.directed)

    def dfs(self,
            start: Vertex,
            process_vertex_early: Callable[[Vertex], Any]=None,
            process_vertex_late: Callable[[Vertex], Any]=None,
            process_edge: Callable[[Vertex, Edgenode], Any]=None,
            discovered_vertices: NodeList=None,
            processed_vertices: NodeList=None) -> NodeList:
        """Depth-First Search
        returns entry and exit times for each vertex
        - a vertex v1 is an ancestor of vertex v2 if the time interval of v2 is
        nested in the one of v1
        - the nb of descendants of a vertex v1 is half its time interval"""
        process_vertex_early = process_vertex_early if process_vertex_early else lambda v: None
        process_vertex_late = process_vertex_late if process_vertex_late else lambda v: None
        process_edge = process_edge if process_edge else lambda v, e: None

        vertices = [v for v in self.adjacency_lists]
        self.parent_edges = NodeList(vertices=vertices)  # reinit parents
        discovered = NodeList(vertices=vertices) if discovered_vertices is None else discovered_vertices  # added to stack
        processed = NodeList(vertices=vertices) if processed_vertices is None else processed_vertices  # processed and out of stack
        discovered[start] = True

        class StackTime:
            def __init__(self, entry: int=None, exit: int=None):
                self.entry = entry
                self.exit = exit

        entry_and_exit_times = NodeList(vertices=vertices, default=StackTime())

        class StackItem:
            def __init__(self, vertex: Vertex, status=0, iter_edgenodes=None):
                self.vertex = vertex
                self.status = status
                self.iter_edgenodes = iter_edgenodes

        stack = Stack(implementation='linked_list')
        stack.push(StackItem(vertex=start))

        counter = 0
        while True:
            try:
                stack_item = stack.pop()
            except StackEmptyError:
                break
            if not stack_item.status:
                entry_and_exit_times[stack_item.vertex] = StackTime(entry=counter)
                counter += 1
                stack_item.iter_edgenodes = iter(self.adjacency_lists[stack_item.vertex].connected_vertices)
                process_vertex_early(stack_item.vertex)
                stack_item.status = 1
            if stack_item.status == 1:
                while True:
                    try:
                        edgenode = next(stack_item.iter_edgenodes)
                        next_vertex = edgenode.end
                    except StopIteration:
                        stack_item.status = 2
                        stack.push(stack_item)
                        break
                    # if undiscovered vertex: add it to stack
                    if not discovered[next_vertex]:
                        discovered[next_vertex] = True
                        stack.push(stack_item)
                        # tree edge
                        edgenode.edgetype = EdgeType.TREE
                        # the parent of the next_vertex is the head of the edge,
                        # i.e., stack_item.vertex
                        self.parent_edges[next_vertex] = Edge(start=stack_item.vertex,
                                                              end=next_vertex,
                                                              weight=edgenode.weight,
                                                              edgenode=edgenode.edgetype,
                                                              **edgenode._kwargs)
                        process_edge(stack_item.vertex, edgenode)
                        stack.push(StackItem(vertex=next_vertex))
                        break
                    # if discovered vertex, then it has been put in stack before
                    # if it is still unprocessed, then it is still in the stack, so no need to add it
                    # if it has been processed but the graph is directed, the edge has not been processed yet
                    # in both case, the edge needs to be processed
                    # but it is a "back edge", the parent of the next_vertex is already known
                    elif not processed[next_vertex] or self.directed:
                        # discovered but not processed
                        if not processed[next_vertex]:
                            edgenode.edgetype = EdgeType.BACK
                        # discovered, processed but earlier entry time
                        elif entry_and_exit_times[stack_item.vertex].entry < entry_and_exit_times[next_vertex].entry:
                            edgenode.edgetype = EdgeType.FORWARD
                        # discovered, processed but later entry time
                        else:
                            edgenode.edgetype = EdgeType.CROSS
                        process_edge(stack_item.vertex, edgenode)
            elif stack_item.status == 2:
                process_vertex_late(stack_item.vertex)
                processed[stack_item.vertex] = True
                entry_and_exit_times[stack_item.vertex].exit = counter
                counter += 1

        return entry_and_exit_times
