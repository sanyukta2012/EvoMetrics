import streamlit as st
from PIL import Image

# --- Attractive Page Config and Background ---
st.set_page_config(
    page_title="About | EvoMetrics",
    page_icon="🧬",
    layout="wide",
)

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #e0f2fe 0%, #f0fdfa 100%);
        background-image: url('https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=1200&q=80');
        background-size: cover;
        background-attachment: fixed;
    }
    .stApp {
        background: rgba(255,255,255,0.85);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 32px rgba(0,0,0,0.08);
    }
    h1, h2, h3 {
        color: #0e7490 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Your Existing Code Below ---
st.title("About")

# --- Author Section ---
st.header("About the Author")
col1, col2 = st.columns([1, 3])
with col1:
    img = Image.open("C:/Users/Sanyukta Kapare/Desktop/sanyukta_image.jpeg")
    st.image(img, width=150, caption="Sanyukta Rajendra Kapare")
with col2:
    st.markdown("""
    **Sanyukta Rajendra Kapare**  
    [LinkedIn Profile](https://www.linkedin.com/in/sanyukta-kapare-ba0223308/)

    Sanyukta is currently pursuing a Masters in Bioinformatics from DES Pune University, Pune. Passionate about computational biology, data analysis, and developing user-friendly bioinformatics tools to support research and education.
    """)

# --- Web Server Section ---
st.header("About the Web Server")
st.markdown("""
**EvoMetrics** is a web-based platform designed for evolutionary distance calculation and phylogenetic tree construction.It integrates multiple sequence comparison methods and tree-building algorithms in an accessible interface, making it a valuable tool for students, researchers, and educators in bioinformatics and evolutionary biology.
""")

# --- Mentor Section ---
st.header("Mentor & Acknowledgment")
st.markdown("""
**Dr. Kushagra Kashyap**  
[LinkedIn Profile](https://www.linkedin.com/in/dr-kushagra-kashyap-b230a3bb/)

Dr. Kushagra Kashyap is an Assistant Professor at DES Pune University.  
His expertise and guidance have been instrumental in the development of EvoMetrics.

**Acknowledgment:**  
Sincere thanks to Dr. Kushagra Kashyap for his mentorship, support, and insightful feedback throughout this project.
""")

# --- Feedback Section ---
st.header("Feedback")
st.markdown("""
We value your feedback and suggestions!  
- 📧 Email: [sanyuktakapare@gmail.com](mailto:sanyuktakapare@gmail.com)  
- [Connect on LinkedIn](https://www.linkedin.com/in/sanyukta-kapare-ba0223308/)
""")
