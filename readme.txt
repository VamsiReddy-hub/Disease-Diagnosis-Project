# Disease Diagnosis Based on Symptoms

This project is a **Disease Diagnosis System** that predicts diseases based on user-provided symptoms. It uses a **Logistic Regression model** trained on a dataset of diseases and their associated symptoms. Additionally, it integrates the **Google Gemini API** to fetch cure and prevention methods for the predicted diseases.

---

## Features

1. **Disease Prediction**:
   - Predicts diseases based on user-input symptoms.
   - Displays the top 5 predicted diseases with confidence scores.

2. **Cure and Prevention Methods**:
   - Fetches cure and prevention methods for each predicted disease using the **Google Gemini API**.

3. **User-Friendly Interface**:
   - Built with **Streamlit**, providing a clean and interactive web interface.
   - Supports comma-separated symptom input.

4. **Custom Styling**:
   - Clean white background with black text for better readability.
   - Responsive design for a seamless user experience.

---

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.8 or higher**.
2. **pip** (Python package installer).

---

## Installation

### Step 1: Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/your-username/disease-diagnosis.git
cd disease-diagnosis

Step 2: Create a Virtual Environment
Create a virtual environment to manage dependencies:
python -m venv .venv

Activate the virtual environment:

On Windows:
.venv\Scripts\activate

Step 3: Install Dependencies
Install the required Python packages:

pip install streamlit pandas scikit-learn nltk google-generativeai


Running the Project
Step 1: Set Up Google Gemini API Key
Obtain a Google Gemini API key from the Google Cloud Console.

Replace the placeholder API key in app.py with your actual API key:
genai.configure(api_key="YOUR_API_KEY_HERE")


Step 2: Run the Streamlit App
Start the Streamlit app:
streamlit run app.py


disease-diagnosis/
├── data/
│   └── cleaned_symptom_disease.csv       # Dataset containing diseases and symptoms
├── utils/
│   └── SymptomSuggestion.py              # Script for symptom preprocessing and prediction
├── app.py                                # Streamlit app for the user interface
├── requirements.txt                      # List of dependencies
└── README.md                             # Project documentation