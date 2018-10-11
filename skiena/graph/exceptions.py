class CycleInGraphError(Exception):
    """raised when a directed graph is detected as having a cycle"""
    pass


class GraphDirectionTypeError(Exception):
    """raised when the function expects a graph with a different direction type
    i.e., either directed or undirected"""
    pass
