import copy


class UndirectedGraph:
    def __init__(self, nodes, edge_pairs):
        self.graph = {}
        for node in nodes:
            self.graph[node] = []
        for from_node, to_node in edge_pairs:
            from_list = self.graph.get(from_node, [])
            from_list.append(to_node)
            to_list = self.graph.get(to_node, [])
            to_list.append(from_node)
            self.graph[from_node] = from_list
            self.graph[to_node] = to_list

    def get_nodes(self):
        """
        Returns a copy of all the nodes in the graph
        :return: deep copy of all graph nodes
        """
        return copy.deepcopy(self.graph)

    def search_bfs(self, start, to_find):
        """
        Performs breadth-first search on the current graph
        :param start: starting node to use in search
        :param to_find: value to find
        :return: True if there is a path to the value, False otherwise
        """
        if len(self.graph) == 0 or start not in self.graph:
            return False

        visited = {}
        adjacent_node_queue = [start]

        while len(adjacent_node_queue) > 0:
            current = adjacent_node_queue.pop()
            if current == to_find:
                return True
            else:
                visited[current] = True
                for sibling in self.graph.get(current):
                    if sibling not in visited:
                        adjacent_node_queue.append(sibling)

        return False
