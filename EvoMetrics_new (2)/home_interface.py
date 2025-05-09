import streamlit as st

# --- Page config for better appearance ---
st.set_page_config(
    page_title="EvoMetrics | Bioinformatics Tools",
    page_icon="🧬",
    layout="wide",
)

# --- Custom CSS for background and style ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(120deg, #e0f2fe 0%, #f0fdfa 100%);
            background-image: url('https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=1200&q=80');
            background-size: cover;
            background-attachment: fixed;
        }
        .stApp {
            background: rgba(255,255,255,0.88);
            border-radius: 18px;
            padding: 2.5rem;
            box-shadow: 0 6px 36px rgba(0,0,0,0.08);
        }
        h1, h2, h3, h4 {
            color: #0e7490 !important;
        }
        .css-1v0mbdj p, .css-1v0mbdj ul, .css-1v0mbdj li {
            font-size: 1.08rem;
        }
    </style>
""", unsafe_allow_html=True)
import streamlit as st

st.title("EvoMetrics")

st.write("""
**EvoMetrics** is a bioinformatics web application for calculating evolutionary distances and constructing phylogenetic trees. 
It supports Hamming distance, Levenshtein distance, and BLOSUM62 scoring for sequence comparison, and provides tools to compute the number of possible rooted and unrooted trees for a given set of nodes. It can also construct phylogenetic trees using the UPGMA and Neighbor Joining algorithms.
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

st.subheader("📝 User Guide")
st.markdown("""
 **How to use EvoMetrics:**
1. **Navigate Tabs:** Use the tabs at the top to switch between Home, About, and Tools.
2. **Choose a Tool:** Select your analysis tool from the sidebar on the left.
3. **Upload Data:** For sequence analysis, upload your DNA, RNA, or protein sequences in FASTA format.
4. **Select Method:** Choose the evolutionary distance method or tree construction algorithm as needed.
5. **View Results:** Results, including distance matrices and phylogenetic trees, will be displayed interactively.
6. **Download/Visualize:** Download your results or visualize trees directly within the app.
7. **Get Help:** Visit the About tab for contact, guidance, and feedback options.
""")
    

st.header("Why Use EvoMetrics?")

st.markdown("""
- Integrates multiple evolutionary distance metrics for comprehensive analysis.
- Supports calculation and visualization of phylogenetic trees with popular algorithms.
- User-friendly interface built with Streamlit for easy access and interaction.
""")

# To run: streamlit run your_script.py
