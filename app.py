# Main Streamlit application

import streamlit as st
from algorithm import greedy_coloring
from visualizer import draw_graph
import networkx as nx
from utils import parse_edges, calculate_chromatic_number, create_graph_from_edges

# Setting the layout to wide for better visualization.
st.set_page_config(layout="wide") 

# Title and description of the app.
st.title("Graph Coloring Visualizer") 
st.markdown("""
This app creates a visualization of graph coloring algorithms, demonstrating vertex coloring with minimum colors and constraint propagation.
You can see how different graph types are colored using the greedy algorithm.
""")

# Letting user select number of nodes.
num = st.slider("Select the number of nodes:", min_value=2, max_value=20, value=6)

G1 = nx.cycle_graph(num)
G2 = nx.path_graph(num)
G3 = nx.complete_graph(num)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Cycle Graph")
    coloring1 = greedy_coloring(G1)
    chromatic_number1 = calculate_chromatic_number(coloring1)
    st.write("Chromatic number:", chromatic_number1)
    draw_graph(G1, coloring1)
    st.write("**Cycle Graph** is a graph that consists of a single cycle, or in other words, some number of vertices connected in a closed chain.")

with col2:
    st.subheader("Path Graph")
    coloring2 = greedy_coloring(G2)
    chromatic_number2 = calculate_chromatic_number(coloring2)
    st.write("Chromatic number:", chromatic_number2)
    draw_graph(G2, coloring2)
    st.write("In **path graph** each node is connected to at most two others. It does not loop back to the start.")

with col3:
    st.subheader("Complete Graph")
    coloring3 = greedy_coloring(G3)
    chromatic_number3 = calculate_chromatic_number(coloring3)
    st.write("Chromatic number:", chromatic_number3)
    draw_graph(G3, coloring3)
    st.write("A simple graph with n vertices is called a **complete graph** if the degree of each vertex is n-1, that is, one vertex is attached with n-1 edges or the rest of the vertices in the graph.")

st.markdown("---")  

st.subheader("Create your own custom graph")

# Example section to help users understand the input format.
st.markdown("**Example input:**\n```\n0 1\n1 2\n2 3\n3 0\n```")
example_edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
G_example = create_graph_from_edges(example_edges)
coloring_example = greedy_coloring(G_example)
chromatic_number_example = calculate_chromatic_number(coloring_example)
st.markdown("""
In this example graph, each line represents an edge between two nodes. Use this format when creating your own graph.
""")
st.markdown("**Example output:**")
draw_graph(G_example, coloring_example, figsize=(2, 2), node_size=300)

user_input = st.text_area("Enter edges:", height=150)
edges, invalid_lines = parse_edges(user_input)

for line in invalid_lines:
    st.warning(f"Invalid line: {line}")

# Drawing the custom graph.
if edges:
    G_custom = create_graph_from_edges(edges)
    coloring_custom = greedy_coloring(G_custom)
    chromatic_number_custom = calculate_chromatic_number(coloring_custom)
    st.write("Chromatic number:", chromatic_number_custom)
    draw_graph(G_custom, coloring_custom, figsize=(2, 2), node_size=300)
    st.markdown(f"Number of nodes: {G_custom.number_of_nodes()}")
    st.markdown(f"Number of edges: {G_custom.number_of_edges()}")
