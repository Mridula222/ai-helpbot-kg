import sys
import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, "knowledge_graph"))
sys.path.append(os.path.join(BASE_DIR, "nlp_processing"))

from nlp_processing.backend_interface import process_nlp
from knowledge_graph.backend_interface import query_kg

app = FastAPI()

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
