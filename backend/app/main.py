import sys
import os

from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # ONE instance only — keep this

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use * for dev; restrict in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup paths for your modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, "knowledge_graph"))
sys.path.append(os.path.join(BASE_DIR, "nlp_processing"))

from nlp_processing.backend_interface import process_nlp
text = "Surya is a product launched in 2023 by ISRO."

print(process_nlp(text))
from knowledge_graph.backend_interface import query_kg

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message
    try:
        nlp_result = process_nlp(user_message)
        kg_result = query_kg(nlp_result)
        return {"reply": kg_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type != "text/plain":
        raise HTTPException(status_code=400, detail="Only plain text files are accepted.")
    
    content = await file.read()
    text = content.decode("utf-8")

    # Process the uploaded text file using your NLP pipeline
    entities = process_nlp(text)

    # Optional: Filter out CARDINAL entities if you want to reduce noise
    filtered_entities = {k: v for k, v in entities.items() if v != "CARDINAL"}

    summary = query_kg(filtered_entities)

    return {
    "filename": file.filename,
    "content_length": len(content),
    "entities_extracted": filtered_entities,
    "kg_summary": summary
}


