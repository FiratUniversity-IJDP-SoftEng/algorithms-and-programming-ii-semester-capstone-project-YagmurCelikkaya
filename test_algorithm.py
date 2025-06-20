# Testing "algorithm.py" using "example" folder.
# To test this file run `python test-algortihm.py` 

import unittest
import json
import networkx as nx
from algorithm import greedy_coloring

class TestGreedyColoring(unittest.TestCase):

    def test_example1(self):
        with open("example/example1.json", "r") as f:
            data = json.load(f)
        edges = data["edges"]

        G = nx.Graph()
        G.add_edges_from(edges)

        coloring = greedy_coloring(G)

        for u, v in G.edges():
            self.assertNotEqual(coloring[u], coloring[v], f"Nodes {u} and {v} have the same color")

    def test_example2(self):
        with open("example/example2.json", "r") as f:
            data = json.load(f)
        edges = data["edges"]

        G = nx.Graph()
        G.add_edges_from(edges)

        coloring = greedy_coloring(G)

        for u, v in G.edges():
            self.assertNotEqual(coloring[u], coloring[v], f"Nodes {u} and {v} have the same color")

if __name__ == '__main__':
    unittest.main()
