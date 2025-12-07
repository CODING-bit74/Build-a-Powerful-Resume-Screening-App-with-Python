## 📄 Resume Category Prediction (FastAPI + ML + Frontend)

A machine learning–powered web application that predicts the job category of a resume using text extraction and classification techniques.
Built using FastAPI, Scikit-Learn, Jinja2 templates, and a modern HTML/CSS/JS frontend with drag-and-drop uploads.

## 🚀 Features
🔍 Resume Category Prediction

Upload a resume (PDF, DOCX, or TXT) and the model predicts the most relevant job domain.

📎 File Extraction

Supports automatic text extraction from:

PDF (.pdf)

Word (.docx)

Plain text (.txt)

💡 Clean & Interactive UI

Includes:

Drag & drop upload area

Modern card UI

Animated loading spinner

Error handling

Result preview with extracted text snippet

⚙️ API Powered

Backend built using:

FastAPI

Machine learning model (SVC Classifier + TF-IDF)

Pickle-based artifact loading

📂 Project Structure

📦 resume-category-prediction
│
├── app.py                    # FastAPI main app
├── model_loader.py           # ML model loaders + text extraction functions
├── clf.pkl                   # Trained classifier model
├── tfidf.pkl                 # TF-IDF vectorizer
├── encoder.pkl               # Label encoder
│
├── templates/
│   └── index.html            # Frontend UI (Jinja2)
│
├── static/
│   ├── style.css             # UI styling
│   └── app.js                # Frontend JS logic
│
├── README.md                 # Project documentation
└── requirements.txt          # Dependencies

## 🛠️ Tech Stack
Frontend

HTML

CSS

JavaScript

Drag-and-drop UI

## Backend

FastAPI

Uvicorn

Python

## ML Model

Scikit-Learn

SVC Classifier

TF-IDF Vectorization

LabelEncoder

## 📥 Installation
1️⃣ Clone the repository

git clone https://github.com/yourusername/resume-category-prediction.git
cd resume-category-prediction

## 2️⃣ Create virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
## 3️⃣ Install dependencies
pip install -r requirements.txt
## ▶️ Running the Application
uvicorn app:app --reload
## Open in browser:
http://localhost:8000
## 📤 Using the API (Optional)
Endpoint: POST /predict

Send a resume file:
curl -X POST -F "file=@resume.pdf" http://localhost:8000/predict
JSON Response Example:
{
  "filename": "resume.pdf",
  "predicted_category": "Data Scientist",
  "extracted_text_snippet": "Experienced data analyst..."
}

## 🧠 Model Training (Optional)
If training your own model:

Clean text using regex

Fit TF-IDF vectorizer

Train SVC

Encode labels
## Save artifacts:
import pickle

pickle.dump(tfidf, open("tfidf.pkl", "wb"))
pickle.dump(svc_model, open("clf.pkl", "wb"))
pickle.dump(le, open("encoder.pkl", "wb"))
## 🚀 Deployment
You can deploy easily on:

Render

Railway

AWS EC2

Azure App Service

Google Cloud Run
