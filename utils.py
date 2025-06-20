# Helper functions for "app.py" 

import networkx as nx

# Reads lines from user input and turns them into graph edges, while reporting invalid lines.
def parse_edges(text): 
    edges = []
    invalid_lines = []
    lines = text.strip().split('\n')
    for line in lines:
        try:
            u, v = map(int, line.strip().split())
            edges.append((u, v))
        except Exception:
            invalid_lines.append(line)
    return edges, invalid_lines

def calculate_chromatic_number(coloring): # Calculate chromatic number.

    if not coloring:
        return 0
    return max(coloring.values()) + 1

def create_graph_from_edges(edges): # Create a NetworkX graph from a list of edges.

    G = nx.Graph()
    G.add_edges_from(edges)
    return G
