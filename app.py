import streamlit as st
from algorithm import greedy_coloring
from visualizer import draw_graph
import networkx as nx

st.title("🎨 Graph Coloring Visualizer")

G = nx.cycle_graph(6)

coloring = greedy_coloring(G)

st.write("Coloring Result:", coloring)

draw_graph(G, coloring)

