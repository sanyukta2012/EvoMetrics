import streamlit as st
import matplotlib.pyplot as plt
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor, _DistanceMatrix
from Bio import Phylo
import math
import random

# --- Helper functions ---

def count_rooted_trees(n):
    # Number of rooted binary trees: (2n-3)! / [2^(n-2) * (n-2)!]
    if n < 2:
        return 0
    return math.factorial(2 * n - 3) // (2 ** (n - 2) * math.factorial(n - 2))

def count_unrooted_trees(n):
    # Number of unrooted binary trees: (2n-5)! / [2^(n-3) * (n-3)!]
    if n < 3:
        return 0
    return math.factorial(2 * n - 5) // (2 ** (n - 3) * math.factorial(n - 3))

def random_distance_matrix(names):
    # Generate a lower triangle random distance matrix for demonstration
    n = len(names)
    matrix = []
    for i in range(n):
        row = []
        for j in range(i):
            row.append(round(random.uniform(0.1, 1.0), 3))  # random distances
        matrix.append(row)
    return _DistanceMatrix(names, matrix)

def plot_tree(tree, rooted=True):
    fig = plt.figure(figsize=(6, 4))
    Phylo.draw(tree, do_show=False, rooted=rooted)
    st.pyplot(fig)
    plt.close(fig)

# --- Streamlit App ---

st.set_page_config(page_title="Phylogenetic Tree Constructor", layout="wide")
st.title("Phylogenetic Tree Constructor")
st.write("Visualize rooted and unrooted phylogenetic trees and calculate the number of possible trees for a given number of nodes.")

n_nodes = st.number_input("Number of taxa (nodes/leaves)", min_value=3, max_value=12, value=5, step=1)
taxa = [f"Taxon_{i+1}" for i in range(n_nodes)]

st.subheader("Number of Possible Trees")
col1, col2 = st.columns(2)
with col1:
    st.metric("Rooted Trees", f"{count_rooted_trees(n_nodes):,}")
with col2:
    st.metric("Unrooted Trees", f"{count_unrooted_trees(n_nodes):,}")


st.caption("Powered by Streamlit & Biopython")
