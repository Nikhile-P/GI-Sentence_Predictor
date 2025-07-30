# Main application file for the Next Sentence Predictor
# Author: [Your Name]
# This version features a polished, two-column UI for a better user experience.

import streamlit as st
from transformers import pipeline

# 1. Page Configuration
# Setting a professional page title and icon.
st.set_page_config(
    page_title="Sentence Predictor",
    page_icon="🤖",
    layout="wide"  # Using a wide layout for the two-column design
)

# Main title of the application
st.title("Next Sentence Predictor")

# Caching the model is crucial for performance.
@st.cache_resource
def load_generator():
    """Loads and caches the pre-trained GPT-2 model."""
    return pipeline('text-generation', model='gpt2')

generator = load_generator()


# 2. Two-Column Layout
# Creating two columns with a specific width ratio for a balanced look.
col1, col2 = st.columns([2, 3])

# --- Column 1: Input Controls ---
with col1:
    # Using a container with a border to group the controls visually.
    with st.container(border=True):
        st.subheader("✍️ Your Input")
        
        user_input = st.text_area("Enter your starting sentence:", "The future of AI is", height=125)
        
        with st.expander("Adjust Settings"):
            max_length = st.slider("Max Length", 30, 150, 60, 10)
            top_k = st.slider("Creativity (Top-K)", 10, 100, 50, 5)

        predict_button = st.button("✨ Predict Sentences")

# --- Column 2: Prediction Results ---
with col2:
    # This container will hold the output.
    with st.container(border=True):
        st.subheader("💡 AI Predictions")
        
        if predict_button:
            if user_input:
                with st.spinner("The AI is thinking..."):
                    outputs = generator(
                        user_input, 
                        max_length=max_length, 
                        num_return_sequences=3, 
                        do_sample=True,
                        top_k=top_k,
                        no_repeat_ngram_size=2
                    )
                
                # Displaying each prediction in its own container for a clean, card-like effect.
                for i, output in enumerate(outputs):
                    clean_output = output['generated_text'].replace(user_input, "").strip()
                    st.info(f"**Option {i+1}:** {clean_output}")
            else:
                st.warning("Please enter a sentence to get started.")
        else:
            st.write("Results will appear here once you click predict.")

# 3. Footer Section
# De-emphasizing the 'About' section by placing it at the bottom.
st.markdown("---")
with st.expander("About this App"):
    st.write("""
        This application uses the **GPT-2 model** from Hugging Face to generate text. I built it to get hands-on experience with generative AI and the Streamlit framework. The focus is on creating a clean, interactive user experience.
    """)