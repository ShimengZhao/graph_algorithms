import csv
import random
from typing import List


class Graph:
    def __init__(self, number_of_vertices: int, directed: bool = True):
        self.number_of_vertices = number_of_vertices
        self.directed = directed
        self.adjacency_matrix = [[-1 for _ in range(number_of_vertices)] for __ in range(number_of_vertices)]
        self.key_map = None
        self.id_map = None

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

    def set_key_map(self, key_map):
        self.key_map = key_map

    def set_id_map(self, id_map):
        self.id_map = id_map

    def get_distance_by_name(self, v1, v2):
        return self.adjacency_matrix[self.key_map[v1]][self.key_map[v2]]

    def export_graph(self, destination_path):
        with open(destination_path, "w+") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['start', 'end', 'weight'])
            for i in range(len(self.adjacency_matrix)):
                for j in range(len(self.adjacency_matrix)):
                    if self.adjacency_matrix[i][j] != -1:
                        csv_writer.writerow([i, j, self.adjacency_matrix[i][j]])

    @classmethod
    def from_csv(cls, file_path, directed=True):
        edge_list, v_set = cls._get_vertex_set_and_edge_list(file_path)
        graph = cls(len(v_set), directed)
        for edge in edge_list:
            graph.add_edge(
                (int(edge[0]), int(edge[1]), float(edge[2]))
            )
        return graph

    @classmethod
    def from_named_nodes_csv(cls, file_path, directed=True):
        edge_list, v_set = cls._get_vertex_set_and_edge_list(file_path)

        key_map = dict()
        id_map = ['' for _ in range(len(v_set))]
        for i, v in enumerate(v_set):
            key_map[v] = i
            id_map[i] = v

        graph = cls(number_of_vertices=len(v_set), directed=directed)
        graph.set_key_map(key_map)
        graph.set_id_map(id_map)
        for edge in edge_list:
            graph.add_edge(
                (key_map[edge[0]], key_map[edge[1]], float(edge[2]))
            )
        return graph

    @staticmethod
    def _get_vertex_set_and_edge_list(file_path):
        # todo: 2. auto check whether the given file is directed or not
        with open(file_path, 'r') as f:
            edges = csv.reader(f)
            next(edges)

            v_set = set()
            edge_list = []
            for edge in edges:
                v_set.add(edge[0])
                v_set.add(edge[1])
                edge_list.append(edge)
        return edge_list, v_set

    @classmethod
    def generate_random_graph(cls, number_of_vertices, weight_range: tuple):
        g = cls(number_of_vertices=number_of_vertices)
        for i in range(len(g.adjacency_matrix)):
            for j in range(len(g.adjacency_matrix)):
                if i != j:
                    g.adjacency_matrix[i][j] = round(
                        weight_range[0] + (weight_range[1] - weight_range[0]) * random.random(), 2)
        return g
