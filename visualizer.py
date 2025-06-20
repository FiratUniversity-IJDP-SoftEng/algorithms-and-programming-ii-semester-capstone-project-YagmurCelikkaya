# Visualization components

import matplotlib.pyplot as plt # for plotting
import streamlit as st # for display it in the app
import networkx as nx # for graph structure
# Getting the list of colors for the nodes.

def draw_graph(G, coloring, figsize=(4, 4), node_size=300):
    pos = nx.spring_layout(G, seed=42)

    fig, ax = plt.subplots(figsize=figsize)

    # Draws a colored graph using NetworkX and displays it in Streamlit.
    node_colors = [coloring.get(node, 0) for node in G.nodes()]

    nx.draw(
        G, pos,
        with_labels=True,
        node_color=node_colors,
        cmap=plt.cm.Set3,
        ax=ax,
        node_size=node_size,
        font_size=10
    )

    ax.set_axis_off()

    st.pyplot(fig, use_container_width=False)
    return fig

