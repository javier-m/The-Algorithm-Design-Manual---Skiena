class GraphTypeError(Exception):
    pass


class CycleInGraphError(GraphTypeError):
    """raised when a directed graph is detected as having a cycle"""
    pass


class GraphDirectionTypeError(GraphTypeError):
    """raised when the function expects a graph with a different direction type
    i.e., either directed or undirected"""
    pass


class PathError(Exception):
    pass
