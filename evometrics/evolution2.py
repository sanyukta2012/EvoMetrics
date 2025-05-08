import streamlit as st
from Levenshtein import distance as lev_dist
from scipy.spatial.distance import hamming
from Bio.Align import substitution_matrices
import itertools

def blosum62_score(seq1, seq2):
    blosum62 = substitution_matrices.load("BLOSUM62")
    score = 0
    for a, b in zip(seq1, seq2):
        try:
            score += blosum62[(a, b)]
        except KeyError:
            score -= 4  # penalty for invalid residues
    return score

def read_fasta(uploaded_file, file_label):
    sequences = {}
    current_seq = []
    current_id = ""
    for line in uploaded_file:
        line = line.decode().strip()
        if line.startswith(">"):
            if current_id:
                sequences[f"{file_label}|{current_id}"] = "".join(current_seq)
            current_id = line[1:]
            current_seq = []
        else:
            current_seq.append(line)
    if current_id:
        sequences[f"{file_label}|{current_id}"] = "".join(current_seq)
    return sequences

st.set_page_config(page_title="Algorithms - Evolutionary Distances", layout="wide")
st.title("Evolutionary Distance Calculator")
st.subheader("Compare sequences from files and manual input")

# Sidebar for file upload and method selection
uploaded_files = st.sidebar.file_uploader(
    "Upload one or more FASTA files", type=["fasta", "txt"], accept_multiple_files=True
)
methods = st.sidebar.multiselect(
    "Select methods", ["Hamming", "Levenshtein", "BLOSUM62"], default=["Hamming", "Levenshtein"]
)

# Manual sequence entry
st.sidebar.markdown("### Sequence Entry")
manual_seqs = []
num_manual = st.sidebar.number_input("Number of manual sequences", min_value=0, max_value=10, value=0, step=1)
for i in range(num_manual):
    st.sidebar.markdown(f"**Manual Sequence {i+1}**")
    seq_id = st.sidebar.text_input(f"Sequence {i+1} ID", key=f"id_{i}")
    seq = st.sidebar.text_area(f"Sequence {i+1}", key=f"seq_{i}")
    if seq_id and seq:
        manual_seqs.append((f"Manual|{seq_id}", seq.replace('\n', '').replace(' ', '').upper()))

# Combine all sequences from files and manual input
all_sequences = {}

# Read sequences from uploaded files
if uploaded_files:
    for i, uploaded_file in enumerate(uploaded_files):
        file_label = f"File{i+1}"
        file_sequences = read_fasta(uploaded_file, file_label)
        all_sequences.update(file_sequences)

# Add manual sequences
for seq_id, seq in manual_seqs:
    all_sequences[seq_id] = seq

seq_ids = list(all_sequences.keys())

if len(all_sequences) < 2:
    st.info("Please upload at least two sequences (from files or manual input) for comparison.")
else:
    # Pairwise comparisons
    pairs = list(itertools.combinations(seq_ids, 2))

    with st.expander("Input Sequences", expanded=True):
        cols = st.columns(2)
        for i, (seq_id, sequence) in enumerate(all_sequences.items()):
            cols[i % 2].code(f">{seq_id}\n{sequence}", language="fasta")

    results = {}
    for method in methods:
        method_results = []
        for (id1, id2) in pairs:
            seq1 = all_sequences[id1]
            seq2 = all_sequences[id2]

            if method == "Hamming":
                if len(seq1) != len(seq2):
                    dist = "N/A (length mismatch)"
                else:
                    dist = hamming(list(seq1), list(seq2)) * len(seq1)
            elif method == "Levenshtein":
                dist = lev_dist(seq1, seq2)
            elif method == "BLOSUM62":
                min_len = min(len(seq1), len(seq2))
                dist = blosum62_score(seq1[:min_len], seq2[:min_len])
            method_results.append((id1, id2, dist))
        results[method] = method_results

    # Display results
    for method, method_data in results.items():
        with st.expander(f"{method} Distance Results", expanded=True):
            st.subheader("Pairwise Comparisons")
            for id1, id2, dist in method_data:
                st.write(f"**{id1}** vs **{id2}**: {dist}")

st.sidebar.markdown("### Instructions")
st.sidebar.info(
    "1. Upload one or more FASTA files and/or enter sequences manually.\n"
    "2. Select comparison methods.\n"
    "3. View results in the main panel."
)
