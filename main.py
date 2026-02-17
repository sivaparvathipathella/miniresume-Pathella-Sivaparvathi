from fastapi import FastAPI, File, UploadFile, Form
import os
import date
import re
from fastapi import HTTPException
app = FastAPI()
candidates_db = []
candidate_id_counter = 1
@app.get("/")
def read_root():
    return {"message": "API is running"}
@app.get("/health")
async def health():
    """Returns a standard REST 200 OK response [cite: 56]"""
    return {"status": "healthy"}


# Temporary storage for candidate data [cite: 7]
candidates_db = []
re.match

@app.post("/upload")
async def upload_resume(
    full_name: str = Form(...),
    dob: date = Form(...),
    contact_number: int = Form(...),
    contact_address: str = Form(...),
    education_qualification: str = Form(...),
    graduation_year: int = Form(...),
    years_of_experience: int = Form(...),
    skill_set: str = Form(...),
    resume_file: UploadFile = File(...)
):
    content_type = resume_file.content_type
    
    # Professional validation for PDF, DOC, and DOCX
    allowed_types = [
        "application/pdf", 
        "application/msword", 
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]
    if content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Only PDF/DOC/DOCX allowed.")

    return {"message": "File validated successfully"}
    # Save file logic 
    file_path = f"uploads/{resume_file.filename}"
    with open(file_path, "wb") as f:
        f.write(await resume_file.read())

    # Create candidate record [cite: 7]
    candidate_id = len(candidates_db) + 1
    new_candidate = {
        "id": candidate_id,
        "full_name": full_name,
        "graduation_year": graduation_year,
        "years_of_experience": years_of_experience,
        "skill_set": skill_set,
        "file_path": file_path
    }
    candidates_db.append(new_candidate)
    
    return {"message": "Upload successful", "candidate_id": candidate_id}
from typing import Optional

@app.get("/candidates")
async def list_candidates(
    skill: Optional[str] = None,
    experience: Optional[int] = None,
    graduation_year: Optional[int] = None
):
    results = candidates_db
    
    if skill:
        results = [c for c in results if skill.lower() in c['skill_set'].lower()]
    if experience is not None:
        results = [c for c in results if c['years_of_experience'] == experience]
    if graduation_year is not None:
        results = [c for c in results if c['graduation_year'] == graduation_year]
        
    return results
@app.get("/candidates/{candidate_id}")
async def get_candidate(candidate_id: int):
    # Search the list for the matching ID
    for candidate in candidates_db:
        if candidate["id"] == candidate_id:
            return candidate
    return {"error": "Candidate not found"}

@app.delete("/candidates/{candidate_id}")
async def delete_candidate(candidate_id: int):
    global candidates_db
    # Filter out the candidate with the matching ID
    candidates_db = [c for c in candidates_db if c["id"] != candidate_id]
    return {"message": f"Candidate {candidate_id} deleted"}


