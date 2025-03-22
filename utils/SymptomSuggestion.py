import warnings
import pandas as pd
from sklearn.linear_model import LogisticRegression
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from collections import Counter
from itertools import combinations

warnings.simplefilter("ignore")

# ✅ Load Cleaned Dataset
dataset_path = "data/cleaned_symptom_disease.csv"

try:
    df = pd.read_csv(dataset_path)
    print(f"✅ Dataset loaded successfully: {len(df)} records")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")
    df = None  # Handle cases where dataset fails to load

# ✅ Extract Symptoms and Diseases
all_symptoms = set()
disease_symptom_map = {}

if df is not None:
    for _, row in df.iterrows():
        symptoms = str(row["Symptoms"]).split(", ")
        disease_symptom_map[row["Disease"]] = symptoms
        all_symptoms.update(symptoms)

all_symptoms = list(all_symptoms)
print(f"✅ Extracted {len(all_symptoms)} unique symptoms.")

# ✅ Train a Simple Logistic Regression Model
X = []
Y = []
for disease, symptoms in disease_symptom_map.items():
    row = [1 if symptom in symptoms else 0 for symptom in all_symptoms]
    X.append(row)
    Y.append(disease)

if X and Y:
    model = LogisticRegression()
    model.fit(X, Y)
    print("✅ Model trained successfully.")
else:
    print("❌ Model training failed due to missing data.")

# ✅ Initialize NLP Tools
lemmatizer = WordNetLemmatizer()
splitter = RegexpTokenizer(r'\w+')

# Symptom mapping for standardization
symptom_mapping = {
    "stomach pain": "stomach_pain",
    "ulcers on tongue": "ulcers_on_tongue",
    "chest pain": "chest_pain",
    # Add more mappings here
}

def map_symptoms(symptoms):
    """Map symptoms to standardized format."""
    mapped_symptoms = []
    for sym in symptoms:
        mapped_sym = symptom_mapping.get(sym, sym)  # Use mapping if available, else keep original
        mapped_symptoms.append(mapped_sym)
    return mapped_symptoms

def process_symptoms(symptoms):
    """Preprocess user input symptoms."""
    if not symptoms:
        return []

    # Standardize input format (replace spaces with underscores)
    user_symptoms = symptoms.lower().replace(" ", "_").split(',')
    processed_user_symptoms = [lemmatizer.lemmatize(word) for sym in user_symptoms for word in splitter.tokenize(sym.strip())]
    
    # Map symptoms to standardized format
    processed_user_symptoms = map_symptoms(processed_user_symptoms)
    
    print(f"🔍 Processed Symptoms: {processed_user_symptoms}")
    return processed_user_symptoms

def predict_disease(symptoms):
    """Predict disease based on symptoms."""
    if df is None:
        return [{"error": "Dataset not loaded"}]

    processed_symptoms = process_symptoms(symptoms)
    if not processed_symptoms:
        return [{"error": "No symptoms provided"}]

    # Check for exact match in the dataset
    exact_match = None
    for disease, disease_symptoms in disease_symptom_map.items():
        if set(processed_symptoms) == set(disease_symptoms):
            exact_match = disease
            break

    if exact_match:
        # If exact match found, return 100% confidence
        return [{"disease": exact_match, "confidence": 100.0}]

    # Assign weights to symptoms (example: cough has higher weight for respiratory diseases)
    symptom_weights = {
        "cough": 2.0,
        "cold": 1.5,
        # Add more symptom weights here
    }

    sample_x = [symptom_weights.get(symptom, 1.0) if symptom in processed_symptoms else 0 for symptom in all_symptoms]

    try:
        prediction = model.predict_proba([sample_x])[0]
        diseases = model.classes_
        top_k = prediction.argsort()[-5:][::-1]  # Get top 5 predictions
        results = [{"disease": diseases[i], "confidence": round(prediction[i] * 100, 2)} for i in top_k]

        print(f"✅ Predicted Diseases: {results}")
        return results

    except Exception as e:
        print(f"❌ Prediction Error: {e}")
        return [{"error": str(e)}]