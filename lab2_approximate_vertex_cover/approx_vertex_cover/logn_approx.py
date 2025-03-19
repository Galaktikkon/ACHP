from copy import deepcopy
from approx_vertex_cover.types import VertexSets


def get_highest_degree_vertex(graph: VertexSets, active: list[bool]) -> int:
    highest_degree = 0
    highest_degree_vertex = None

    for i, vertex_set in enumerate(graph):
        if not active[i]:
            continue

        if len(vertex_set) > highest_degree:
            highest_degree = len(vertex_set)
            highest_degree_vertex = i

    return highest_degree_vertex


def logn_approx(graph: VertexSets) -> set[int]:
    """
    Approximation algorithm for the Vertex Cover problem, which takes the vertex
    with the highest degree and adds it to the solution.

    Approximation factor: log(n)

    :param graph: graph represented as a list of edges
    :return: set of vertices that approximate the cover
    """

    G = deepcopy(graph)
    sol = set()
    active = [True for _ in range(len(G))]
    while any(active):
        v = get_highest_degree_vertex(graph=G, active=active)

        if v is None:
            break

        active[v] = False
        sol.add(v)

        for vertex_set in G:
            if v in vertex_set:
                vertex_set.remove(v)

    return sol
