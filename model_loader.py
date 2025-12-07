import pickle
import re
from io import BytesIO
from docx import Document
import PyPDF2


def load_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)


def load_model():
    tfidf = load_pickle("tfidf.pkl")
    svc_model = load_pickle("clf.pkl")
    le = load_pickle("encoder.pkl")

    return {
        "tfidf": tfidf,
        "svc_model": svc_model,
        "le": le
    }


def clean_resume_text(txt):
    txt = re.sub(r"http\S+|www.\S+", " ", txt)
    txt = re.sub(r"@[A-Za-z0-9_]+", " ", txt)
    txt = re.sub(r"#[A-Za-z0-9_]+", " ", txt)
    txt = re.sub(r"[^a-zA-Z0-9 ]", " ", txt)
    txt = re.sub(r"\s+", " ", txt)
    return txt.strip()


def extract_text_from_pdf(file_bytes):
    pdf = PyPDF2.PdfReader(BytesIO(file_bytes))
    text = ""
    for page in pdf.pages:
        extracted = page.extract_text() or ""
        text += extracted + "\n"
    return text


def extract_text_from_docx(file_bytes):
    doc = Document(BytesIO(file_bytes))
    return "\n".join(p.text for p in doc.paragraphs)


def extract_text_from_txt(file_bytes):
    try:
        return file_bytes.decode("utf-8")
    except:
        return file_bytes.decode("latin-1")
