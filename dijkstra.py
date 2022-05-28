from queue import PriorityQueue

from graph import Graph


class ShortestPath:
    def __init__(self, distance, path):
        self.distance = distance
        self.path = path

    def __repr__(self):
        return f"<Shortest Path: {'->'.join([str(x) for x in self.path])} -- Distance: {self.distance}>"

    def get_named_path_result(self, id_map):
        self.path = [id_map[x] for x in self.path.copy()]
        return self


class Dijkstra:
    def __init__(self, graph: Graph):
        self.number_of_vertices = graph.number_of_vertices
        self.edges = graph.adjacency_matrix
        self.key_map = graph.key_map
        self.id_map = graph.id_map
        self.result_dict = dict()

    def get_shortest_path_by_name(self, start_vertex, end_vertex) -> ShortestPath:
        if start_vertex in self.key_map and end_vertex in self.key_map:
            result = self.get_shortest_path(self.key_map[start_vertex], self.key_map[end_vertex])
            return result.get_named_path_result(self.id_map)
        else:
            raise ValueError(f'{start_vertex} or {end_vertex} is not a valid vertex name!')

    def get_shortest_path(self, start_vertex, end_vertex) -> ShortestPath:
        if start_vertex in self.result_dict:
            print(f"Result retrieved from cache for start_vertex: {start_vertex}.")
        else:
            print(f"Result not in cache, Dijkstra runs for the start_vertex: {start_vertex}.")
            self.run(start_vertex)
        return ShortestPath(
            distance=self.result_dict[start_vertex][end_vertex]['distance'],
            path=self.result_dict[start_vertex][end_vertex]['path']
        )

    def run(self, start_vertex):
        result = {v: {'distance': float('inf'), 'path': []} for v in range(self.number_of_vertices)}
        result[start_vertex]['distance'] = 0
        result[start_vertex]['path'].append(start_vertex)

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        visited = set()
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            visited.add(current_vertex)

            for neighbor in range(self.number_of_vertices):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in visited:
                        old_cost = result[neighbor]['distance']
                        new_cost = result[current_vertex]['distance'] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            result[neighbor]['distance'] = new_cost
                            result[neighbor]['path'] = result[current_vertex]['path'] + [neighbor]
        self.result_dict[start_vertex] = result
