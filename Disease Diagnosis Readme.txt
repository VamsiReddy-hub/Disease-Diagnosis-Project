🏥 Disease Diagnosis Based on Symptoms

This project is a Disease Diagnosis System that predicts diseases based on user-provided symptoms. It is built using Machine Learning (Logistic Regression), Streamlit, and Google Gemini API to fetch cure and prevention methods.

📌 Technologies Used

1️⃣ Python 🐍

Used as the primary programming language for building the ML model and Streamlit web app.

2️⃣ Machine Learning (Logistic Regression) 🤖

The model is trained on a dataset of diseases and symptoms.

It predicts the top 5 possible diseases based on the given symptoms.

3️⃣ Natural Language Processing (NLP) 💠

NLTK (Natural Language Toolkit) is used for:

Lemmatization (reducing words to their base form).

Tokenization (splitting text into words).

4️⃣ Google Gemini API 🧠

Used to fetch cure and prevention methods for the predicted diseases.

The Generative AI model (Gemini 1.5 Flash) processes medical queries.

5️⃣ Streamlit 🎨

Provides an interactive and user-friendly interface.

Allows users to input symptoms and view predictions in real time.

6️⃣ Custom CSS Styling 🎨

Uses a starry night background with smooth animations.

Improves the visual appeal of the web app.

📌 Project Workflow

✅ Step 1: User Input

Users enter symptoms as comma-separated values (e.g., "fever, cough, headache").

✅ Step 2: Disease Prediction

The Logistic Regression model processes the symptoms.

The top 5 diseases with confidence scores are displayed.

✅ Step 3: Fetching Cure & Prevention

The Google Gemini API fetches cure and prevention methods for each disease.

✅ Step 4: Display Results

The diseases, confidence scores, cure, and prevention are displayed neatly.

📌 Key Features

🎯 1. Predict Diseases

Users enter symptoms, and the model predicts possible diseases.

🧑‍⚕️ 2. Get Cure & Prevention

Google Gemini AI fetches real-time medical advice.

🌟 3. Modern UI with Custom Styling

Dark theme, animations, and responsive design.

⚡ 4. Fast & Efficient

Predictions are made in seconds using ML & Generative AI.

📌 How to Run the Project

🔹 Step 1: Clone the Repository

git clone https://github.com/your-username/disease-diagnosis.git
cd disease-diagnosis

🔹 Step 2: Create a Virtual Environment

python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

🔹 Step 3: Install Dependencies

pip install -r requirements.txt

🔹 Step 4: Set Up Google Gemini API Key

Go to Google AI Studio

Get your API Key and replace it in app.py:

genai.configure(api_key="YOUR_API_KEY_HERE")

🔹 Step 5: Run the Streamlit App

streamlit run app.py

📌 Common Interview Questions & Answers

❓ Q1: What is the objective of this project?

✅ Answer:The objective is to build an AI-powered disease diagnosis system that predicts diseases based on user symptoms and provides cure & prevention methods using Google Gemini API.

❓ Q2: How does the Machine Learning model work?

✅ Answer:

We used Logistic Regression to train a model on a dataset of diseases and symptoms.

It predicts the most probable diseases for given symptoms.

The model outputs the top 5 diseases with confidence scores.

❓ Q3: How does the Google Gemini API help?

✅ Answer:

It is an AI-powered chatbot that can generate text-based responses.

We use it to fetch cure & prevention methods for the predicted diseases.

The model asks the API for medical advice and displays the response.

❓ Q4: Why did you use Streamlit?

✅ Answer:

Streamlit allows fast and interactive UI development for data science projects.

It provides a simple interface for users to enter symptoms and get instant predictions.

❓ Q5: How do you handle errors in this project?

✅ Answer:

We use try-except blocks to handle API errors and missing inputs.

Example:

try:
    response = model.generate_content(f"What are the cure and prevention methods for {disease}?")
    return response.text
except Exception as e:
    return f"Error fetching details: {e}"

If the API fails, the app shows a user-friendly error message instead of crashing.

❓ Q6: What are the limitations of this project?

✅ Answer:

Accuracy depends on the dataset – The ML model is only as good as the training data.

Google Gemini API limitations – It may not always provide accurate medical advice.

Not a replacement for doctors – This tool helps users, but professional medical consultation is still required.

🚀 Final Thoughts

This project is a powerful AI-based disease prediction system that combines:✅ Machine Learning for diagnosis✅ Google Gemini AI for medical advice✅ Streamlit for a user-friendly interface

Hope this helps in your interview! Let me know if you need any modifications or explanations! 😊🔥

