from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import traceback

from model_loader import (
    load_model,
    clean_resume_text,
    extract_text_from_pdf,
    extract_text_from_docx,
    extract_text_from_txt,
)

app = FastAPI()

# Enable CORS (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend assets
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load models once at startup
model_artifacts = load_model()


@app.get("/", response_class=HTMLResponse)
async def load_homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict_resume(file: UploadFile = File(...)):
    try:
        filename = file.filename
        ext = filename.split(".")[-1].lower()
        content = await file.read()

        # File extraction
        if ext == "pdf":
            text = extract_text_from_pdf(content)
        elif ext == "docx":
            text = extract_text_from_docx(content)
        elif ext == "txt":
            text = extract_text_from_txt(content)
        else:
            raise HTTPException(
                status_code=400,
                detail="Unsupported file format. Upload PDF, DOCX, or TXT."
            )

        # Clean text
        cleaned = clean_resume_text(text)

        # Predict
        tfidf = model_artifacts["tfidf"]
        svc_model = model_artifacts["svc_model"]
        le = model_artifacts["le"]

        vectorized = tfidf.transform([cleaned]).toarray()
        prediction = svc_model.predict(vectorized)
        category = le.inverse_transform(prediction)[0]

        return {
            "filename": filename,
            "predicted_category": category,
            "extracted_snippet": cleaned[:200]
        }

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
