import matplotlib.pyplot as plt
import streamlit as st
import networkx as nx 

def draw_graph(G, coloring):
    fig, ax = plt.subplots()
    node_colors = [coloring.get(node, 0) for node in G.nodes()]
    nx.draw(G, with_labels=True, node_color=node_colors, cmap=plt.cm.Set3, ax=ax)
    st.pyplot(fig)

