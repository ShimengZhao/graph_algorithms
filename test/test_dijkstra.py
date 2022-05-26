import unittest

from dijkstra import Dijkstra
from graph import Graph


class TestDijkstra(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph(9)
        edge_list = [
            (0, 1, 4),
            (0, 6, 7),
            (1, 6, 11),
            (1, 7, 20),
            (1, 2, 9),
            (2, 3, 6),
            (2, 4, 2),
            (3, 4, 10),
            (3, 5, 5),
            (4, 5, 15),
            (4, 7, 1),
            (4, 8, 5),
            (5, 8, 12),
            (6, 7, 1),
            (7, 8, 3),
        ]
        for t in edge_list:
            self.graph.add_edge(t)

    def test_should_calculate_one_shortest_path_correctly(self):
        dk = Dijkstra(self.graph)
        result = dk.get_shortest_path(2, 8)
        self.assertEqual(6, result.distance)
        self.assertSequenceEqual([2, 4, 7, 8], result.path)

    def test_should_calculate_multiple_shortest_path_of_same_start_vertex_correctly(self):
        dk = Dijkstra(self.graph)

        result_1 = dk.get_shortest_path(2, 8)
        self.assertEqual(6, result_1.distance)
        self.assertSequenceEqual([2, 4, 7, 8], result_1.path)

        result_2 = dk.get_shortest_path(2, 5)
        self.assertEqual(11, result_2.distance)
        self.assertSequenceEqual([2, 3, 5], result_2.path)

    def test_should_calculate_multiple_shortest_path_of_different_start_vertices_correctly(self):
        dk = Dijkstra(self.graph)

        result_1 = dk.get_shortest_path(2, 8)
        self.assertEqual(6, result_1.distance)
        self.assertSequenceEqual([2, 4, 7, 8], result_1.path)

        result_2 = dk.get_shortest_path(0, 5)
        self.assertEqual(24, result_2.distance)
        self.assertSequenceEqual([0, 1, 2, 3, 5], result_2.path)


if __name__ == '__main__':
    unittest.main()
