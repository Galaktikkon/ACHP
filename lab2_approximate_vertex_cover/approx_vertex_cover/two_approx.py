from approx_vertex_cover.types import EdgeList


def two_approx(graph: EdgeList) -> set[int]:
    """
    Approximation algorithm for the Vertex Cover problem, which takes any edge
    and adds its ends to the solution.

    Approximation factor: 2

    :param graph: graph represented as a list of edges
    :return: set of vertices that approximate the cover
    """
    cover = set()

    for u, v in graph:
        if u not in cover and v not in cover:
            cover.add(u)
            cover.add(v)

    return cover
