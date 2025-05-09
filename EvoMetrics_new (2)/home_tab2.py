import streamlit as st

st.title("EvoMetrics")

st.write("""
**EvoMetrics** is a bioinformatics web application for calculating evolutionary distances and constructing phylogenetic trees. 
It supports Hamming distance, Levenshtein distance, and BLOSUM62 scoring for sequence comparison, and provides tools to compute the number of possible rooted and unrooted trees for a given set of nodes. 
You can also construct phylogenetic trees using the UPGMA and Neighbor Joining algorithms.
""")

st.header("Methods Supported")

st.markdown("""
- **Hamming Distance:** Counts the number of positions with different characters between two sequences of equal length.
- **Levenshtein Distance:** Measures the minimum number of single-character edits (insertions, deletions, substitutions) needed to change one sequence into another.
- **BLOSUM62:** Uses a substitution matrix to score alignments between protein sequences based on evolutionary divergence.
- **Rooted/Unrooted Tree Calculation:** Computes the total number of possible rooted ((2n-3)!!) and unrooted ((2n-5)!!) trees for n nodes.
- **UPGMA:** Constructs rooted phylogenetic trees assuming a constant rate of evolution (molecular clock).
- **Neighbor Joining:** Builds unrooted trees without assuming a constant rate, suitable for varying evolutionary rates.
""")

st.header("Key Features")

st.markdown("""
1. **Multiple Distance Metrics:** Choose from Hamming, Levenshtein, or BLOSUM62 for flexible sequence comparison.
2. **Tree Enumeration:** Instantly calculate the number of possible rooted and unrooted trees for your dataset.
3. **Phylogenetic Tree Construction:** Build trees using both UPGMA and Neighbor Joining methods.
4. **User-Friendly Interface:** Simple, intuitive design for easy access and fast results.
5. **Comprehensive Analysis:** Supports both DNA/RNA and protein sequence comparison.
6. **Visualization Ready:** Results can be used for further visualization and analysis.
""")

st.header("Why Use EvoMetrics?")

st.markdown("""
- Integrates multiple evolutionary distance metrics for comprehensive analysis.
- Supports calculation and visualization of phylogenetic trees with popular algorithms.
- User-friendly interface built with Streamlit for easy access and interaction.
""")

# To run: streamlit run your_script.py
