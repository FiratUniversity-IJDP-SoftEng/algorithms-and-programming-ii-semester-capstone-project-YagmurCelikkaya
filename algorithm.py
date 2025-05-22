def greedy_coloring(graph):
    coloring = {}
    for node in graph.nodes():
        neighbor_colors = {coloring.get(neigh) for neigh in graph.neighbors(node)}
        color = 0
        while color in neighbor_colors:
            color += 1
        coloring[node] = color
    return coloring

