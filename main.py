from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import shutil

from src.parser.resume_parser import extract_resume_text
from src.nlp.preprocess import preprocess_to_string
from src.nlp.skill_extractor import extract_skills
from src.matching.job_matcher import compute_similarity, get_match_label
from src.scoring.ats_scorer import calculate_skill_match, calculate_final_ats_score

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    file: UploadFile = File(...),          # MUST be named file
    jd_text: str = Form(...)              # MUST be named jd_text
):
    # Save uploaded resume
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Resume processing
    raw_text = extract_resume_text(file_path)
    clean_resume = preprocess_to_string(raw_text)
    clean_job = preprocess_to_string(jd_text)

    resume_skills = extract_skills(clean_resume)

    similarity_score = compute_similarity(clean_resume, clean_job)
    skill_match_score, matched_skills, missing_skills = calculate_skill_match(resume_skills, clean_job)

    final_ats_score = calculate_final_ats_score(similarity_score, skill_match_score)
    match_label = get_match_label(final_ats_score)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "score": final_ats_score,
        "level": match_label,
        "matched": matched_skills,
        "missing": missing_skills,
        "filename": file.filename
    })