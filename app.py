import streamlit as st
import os
import nltk
from utils.SymptomSuggestion import predict_disease
import google.generativeai as genai

# Download NLTK resources
nltk.download('wordnet')
nltk.download('omw-1.4')

# Set page config
st.set_page_config(page_title="Disease Diagnosis", page_icon="\ud83c\udfe5", layout="wide")

# Configure Gemini API using environment variable
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Initialize Gemini model
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"\u274c Error initializing Gemini model: {e}")
    model = None

def get_cure_and_prevention(disease):
    if model is None:
        return "Error: Gemini model not initialized."
    try:
        response = model.generate_content(f"What are the cure and prevention methods for {disease}?")
        return response.text
    except Exception as e:
        return f"Error fetching details: {e}"

# Custom CSS for styling
st.markdown(
    """
    <style>
    html, body {
        height: 100%;
        margin: 0;
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        color: white;
        font-family: 'Lato', sans-serif;
    }
    .stApp {
        background: transparent;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: white;
    }
    .stTextInput input {
        color: black;
        background-color: white;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stSuccess {
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("\ud83c\udfe5 Disease Diagnosis Based on Symptoms")
    st.write("Enter your symptoms (comma-separated) to get a diagnosis.")

    symptoms = st.text_input("Enter Symptoms (e.g., fever, headache, cough):")

    if st.button("\ud83d\udd0d Predict Disease"):
        if not symptoms:
            st.error("\ud83d\udea8 Please enter at least one symptom.")
        else:
            with st.spinner("\ud83d\udd2c Predicting..."):
                result = predict_disease(symptoms)
                if "error" in result[0]:
                    st.error(f"\u274c Error: {result[0]['error']}")
                else:
                    st.success("\u2705 Predicted Diseases:")
                    for disease in result:
                        st.write(f"### {disease['disease']} (Confidence: {disease['confidence']}%)")
                        details = get_cure_and_prevention(disease['disease'])
                        st.write(f"#### Cure and Prevention Methods:")
                        st.write(details)
                        st.write("---")

if __name__ == "__main__":
    main()
