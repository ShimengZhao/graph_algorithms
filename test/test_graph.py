import csv
import os
import unittest
from os import path

from graph import Graph


class TestGraph(unittest.TestCase):
    def test_should_initiate_graph_from_named_nodes_file_successfully(self):
        g = Graph.from_named_nodes_csv(path.join('test_resources', 'named_nodes_graph.csv'), directed=False)
        self.assertEqual(6, g.get_distance_by_name('C', 'D'))
        self.assertEqual(10, g.get_distance_by_name('E', 'D'))

    def test_should_initiate_graph_from_file_successfully(self):
        g = Graph.from_csv(file_path=path.join('test_resources', 'graph.csv'), directed=False)
        self.assertEqual(12, g.adjacency_matrix[5][8])

    def test_should_create_adjacency_matrix_of_the_give_size(self):
        g = Graph(4)
        self.assertEqual(4, len(g.adjacency_matrix))
        self.assertEqual(4, len(g.adjacency_matrix[0]))

    def test_should_add_edge_successfully(self):
        g = Graph(4)
        g.add_edge((1, 3, 9))
        self.assertEqual(9, g.adjacency_matrix[1][3])

    def test_should_add_weight_for_both_direction_when_graph_is_undirected(self):
        g = Graph(4, directed=False)
        g.add_edge((1, 3, 9))
        print(g.adjacency_matrix)
        self.assertEqual(9, g.adjacency_matrix[1][3])
        self.assertEqual(9, g.adjacency_matrix[3][1])

    def test_should_add_edge_list_successfully(self):
        g = Graph(4)
        edge_tuple_list = [(1, 3, 9), (2, 0, 6)]
        g.add_edges(edge_tuple_list=edge_tuple_list)
        self.assertEqual(9, g.adjacency_matrix[1][3])
        self.assertEqual(6, g.adjacency_matrix[2][0])

    def test_should_raise_error_when_adding_invalid_edge(self):
        g = Graph(4)
        with self.assertRaises(ValueError):
            g.add_edge((1, 4, 10))

    def test_should_generate_random_graph_correctly(self):
        g = Graph.generate_random_graph(number_of_vertices=10, weight_range=(10, 1000))
        self.assertEqual(-1, g.adjacency_matrix[0][0])
        self.assertNotEqual(-1, g.adjacency_matrix[0][3])

    def test_should_export_graph_correctly(self):
        g_export = Graph(4)
        edge_tuple_list = [(1, 3, 9), (2, 0, 6)]
        g_export.add_edges(edge_tuple_list=edge_tuple_list)

        dest_path = 'export_result.csv'
        g_export.export_graph(destination_path=dest_path)
        g_import = Graph.from_csv(file_path=dest_path, directed=True)
        self.assertEqual(9, g_import.adjacency_matrix[1][3])
        self.assertEqual(6, g_import.adjacency_matrix[2][0])

        os.remove(dest_path)


if __name__ == '__main__':
    unittest.main()
