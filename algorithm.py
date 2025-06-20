# This function colors the nodes of a graph using the greedy algorithm.

def greedy_coloring(graph): 
    coloring = {}
    for node in graph.nodes():
        neighbor_colors = { 
            coloring[neighbor]
            for neighbor in graph.neighbors(node)
            if neighbor in coloring
        }

        color = 0
        while color in neighbor_colors:
            color += 1

        coloring[node] = color

    return coloring
