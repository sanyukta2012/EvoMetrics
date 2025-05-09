import streamlit as st
from PIL import Image

st.title("About")

# --- Author Section ---
st.header("About the Author")
col1, col2 = st.columns([1, 3])
with col1:
    # Load and display the author's profile image using PIL.Image.open
    img = Image.open("C:/Users/Sanyukta Kapare/Desktop/sanyukta_image.jpeg")  # Ensure this file exists
    st.image(img, width=150, caption="Sanyukta Rajendra Kapare")
with col2:
    st.markdown("""
    **Sanyukta Rajendra Kapare**  
    [LinkedIn Profile](https://www.linkedin.com/in/sanyukta-kapare-ba0223308/)

    Sanyukta is currently pursuing a Masters in Bioinformatics from DES Pune University, Pune.  
    She is passionate about computational biology, data analysis, and developing user-friendly bioinformatics tools to support research and education.
    """)

# --- Web Server Section ---
st.header("About the Web Server")
st.markdown("""
**EvoMetrics** is a web-based platform designed for evolutionary distance calculation and phylogenetic tree construction.  
It integrates multiple sequence comparison methods and tree-building algorithms in an accessible interface, making it a valuable tool for students, researchers, and educators in bioinformatics and evolutionary biology.
""")

# --- Mentor Section ---
st.header("Mentor & Acknowledgment")
st.markdown("""
**Dr. Kushagra Kashyap**  
[LinkedIn Profile](https://www.linkedin.com/in/dr-kushagra-kashyap-b230a3bb/)

Dr. Kashyap is an Assistant Professor at DES Pune University.  
His expertise and guidance have been instrumental in the development of EvoMetrics.

**Acknowledgment:**  
Sincere thanks to Dr. Kashyap for his mentorship, support, and insightful feedback throughout this project.
""")

# --- Feedback Section ---
st.header("Feedback")
st.markdown("""
We value your feedback and suggestions!  
- 📧 Email: [sanyuktakapare@gmail.com](mailto:sanyuktakapare@gmail.com)  
- [Connect on LinkedIn](https://www.linkedin.com/in/sanyukta-kapare-ba0223308/)
""")
