from fastapi import FastAPI, Request
from pydantic import BaseModel
from logic import generate_report  # ✅ Corrected import
import uvicorn

app = FastAPI()

class ReportRequest(BaseModel):
    company_name: str

@app.on_event("startup")
def startup_event():
    print("FastAPI backend is starting up and initializing the logic.")

@app.get("/")
def health_check():
    return {"status": "Your API health is good"}

@app.post("/generate-report")
def generate(report_req: ReportRequest):
    report_text, report_path = generate_report(report_req.company_name)
    return {"report_text": report_text, "report_file_path": report_path}

