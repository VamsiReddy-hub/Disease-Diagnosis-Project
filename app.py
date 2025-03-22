import streamlit as st
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

from utils.SymptomSuggestion import predict_disease
import google.generativeai as genai
#This is Lonewolf here .

# Set page config (MUST BE THE FIRST STREAMLIT COMMAND)
st.set_page_config(page_title="Disease Diagnosis", page_icon="🏥", layout="wide")

# Configure Gemini API
genai.configure(api_key="AIzaSyCRVEEt82ZmPp8Xujbed2sBdla2_kGMJ5w")

# Initialize Gemini model
try:
    model = genai.GenerativeModel('gemini-1.5-flash')  # Use the correct model name
except Exception as e:
    st.error(f"❌ Error initializing Gemini model: {e}")
    model = None

def get_cure_and_prevention(disease):
    """Fetch cure and prevention methods for a disease using Gemini API."""
    if model is None:
        return "Error: Gemini model not initialized."

    try:
        response = model.generate_content(f"What are the cure and prevention methods for {disease}?")
        return response.text
    except Exception as e:
        return f"Error fetching details: {e}"

# Inject custom CSS for parallax star background
st.markdown(
    """
    <link href='https://fonts.googleapis.com/css?family=Lato:300,400,700' rel='stylesheet' type='text/css'>
    <style>
    html, body {
        height: 100%;
        margin: 0;
        overflow: hidden;
    }
    #stars {
        width: 1px;
        height: 1px;
        background: transparent;
        box-shadow: multiple-box-shadow(700);
        animation: animStar 50s linear infinite;
    }
    #stars:after {
        content: " ";
        position: absolute;
        top: 2000px;
        width: 1px;
        height: 1px;
        background: transparent;
        box-shadow: multiple-box-shadow(700);
    }
    #stars2 {
        width: 2px;
        height: 2px;
        background: transparent;
        box-shadow: multiple-box-shadow(200);
        animation: animStar 100s linear infinite;
    }
    #stars2:after {
        content: " ";
        position: absolute;
        top: 2000px;
        width: 2px;
        height: 2px;
        background: transparent;
        box-shadow: multiple-box-shadow(200);
    }
    #stars3 {
        width: 3px;
        height: 3px;
        background: transparent;
        box-shadow: multiple-box-shadow(100);
        animation: animStar 150s linear infinite;
    }
    #stars3:after {
        content: " ";
        position: absolute;
        top: 2000px;
        width: 3px;
        height: 3px;
        background: transparent;
        box-shadow: multiple-box-shadow(100);
    }
    @keyframes animStar {
        from {
            transform: translateY(0px);
        }
        to {
            transform: translateY(-2000px);
        }
    }
    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        color: white;
        font-family: 'Lato', sans-serif;
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
        font-size: 16px; /* Adjust font size for predicted diseases */
    }
    </style>
    <div id="stars"></div>
    <div id="stars2"></div>
    <div id="stars3"></div>
    """,
    unsafe_allow_html=True,
)

# Streamlit App
def main():
    # Title and description
    st.title("🏥 Disease Diagnosis Based on Symptoms")
    st.write("Enter your symptoms (comma-separated) to get a diagnosis.")

    # Input for symptoms
    symptoms = st.text_input("Enter Symptoms (e.g., fever, headache, cough):")

    # Predict button
    if st.button("🔍 Predict Disease"):
        if not symptoms:
            st.error("🚨 Please enter at least one symptom.")
        else:
            with st.spinner("🔬 Predicting..."):
                result = predict_disease(symptoms)
                if "error" in result[0]:
                    st.error(f"❌ Error: {result[0]['error']}")
                else:
                    st.success("✅ Predicted Diseases:")
                    for disease in result:
                        st.write(f"### {disease['disease']} (Confidence: {disease['confidence']}%)")
                        
                        # Fetch cure and prevention methods
                        details = get_cure_and_prevention(disease['disease'])
                        st.write(f"#### Cure and Prevention Methods:")
                        st.write(details)
                        st.write("---")

# Run the app
if __name__ == "__main__":
    main()
