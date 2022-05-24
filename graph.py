from typing import List


class Graph:
    def __init__(self, number_of_vertices: int, directed: bool = True):
        self.number_of_vertices = number_of_vertices
        self.directed = directed
        self.adjacency_matrix = [[-1 for _ in range(number_of_vertices)] for __ in range(number_of_vertices)]

    def add_edge(self, edge_tuple: tuple):
        if self._validate_edge_tuple(edge_tuple):
            self.adjacency_matrix[edge_tuple[0]][edge_tuple[1]] = edge_tuple[2]
            if not self.directed:
                self.adjacency_matrix[edge_tuple[1]][edge_tuple[0]] = edge_tuple[2]
        else:
            raise ValueError(f"Invalid edge tuple: {edge_tuple}")

    def add_edges(self, edge_tuple_list: List[tuple]):
        for edge_tuple in edge_tuple_list:
            self.add_edge(edge_tuple)

    def _validate_edge_tuple(self, edge_tuple: tuple):
        if 0 <= edge_tuple[0] < self.number_of_vertices and 0 <= edge_tuple[1] < self.number_of_vertices:
            return True
        else:
            return False
