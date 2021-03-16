import unittest
import undirected_graph as ug


class UndirectedGraphTest(unittest.TestCase):

    def test_graph_is_built_correctly(self):
        test_cases = [
            ({1: [2, 3], 2: [1], 3: [1, 4, 5], 4: [3, 5], 5: [3, 4]}, [1, 2, 3, 4, 5],
             [(1, 2), (1, 3), (3, 4), (3, 5), (5, 4)]),
            ({1: [2, 3], 2: [1], 3: [1, 4, 5], 4: [3, 5], 5: [3, 4], 6: []}, [1, 2, 3, 4, 5, 6],
             [(1, 2), (1, 3), (3, 4), (3, 5), (5, 4)]),
            ({1: [2, 3, 4, 5], 2: [1], 3: [1], 4: [1], 5: [1]}, [1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5)]),
            ({}, [], []),
            ({1: []}, [1], []),
            ({1: [2], 2: [1]}, [1, 2], [(1, 2)])]
        for expected_graph, nodes, edge_pairs in test_cases:
            undirected_graph = ug.UndirectedGraph(nodes, edge_pairs)
            for node, neighbors in undirected_graph.get_nodes().items():
                self.assertListEqual(expected_graph.get(node), neighbors)

    def test_bfs_search_returns_false_when_searching_for_unreachable_node(self):
        undirected_graph = ug.UndirectedGraph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                              [(1, 2), (1, 4), (1, 5), (2, 6), (2, 3), (3, 4), (5, 6), (5, 7), (6, 9),
                                               (7, 8)])
        test_cases = [(1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (100, 10),
                      (100, 100)]
        for start_node, to_find in test_cases:
            self.assertFalse(undirected_graph.search_bfs(start_node, to_find))

    def test_bfs_search_returns_true_when_searching_for_reachable_node(self):
        undirected_graph = ug.UndirectedGraph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                              [(1, 2), (1, 4), (1, 5), (2, 6), (2, 3), (3, 4), (5, 6), (5, 7), (6, 9),
                                               (7, 8)])
        test_cases = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
                      (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9),
                      (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9),
                      (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9),
                      (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9),
                      (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9),
                      (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9),
                      (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9),
                      (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]
        for start_node, to_find in test_cases:
            self.assertTrue(undirected_graph.search_bfs(start_node, to_find))
