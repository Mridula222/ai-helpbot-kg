import sys
import os

from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Setup FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Open for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup paths for your modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, "knowledge_graph"))
sys.path.append(os.path.join(BASE_DIR, "nlp_processing"))

# Import custom functions
from nlp_processing.backend_interface import process_nlp
from knowledge_graph.backend_interface import query_kg

# Schema for request body
class ChatRequest(BaseModel):
    message: str

# Simple rule-based fallback replies
def basic_reply(message: str) -> str:
    message = message.lower().strip()
    greetings = ["hi", "hello", "hey", "hola", "good morning", "good afternoon", "good evening"]
    if message in greetings:
        return "Hello! How can I assist you today? \n Send me a keyword related to MOSDAC, or please check the knowledge graph for more entities."
    elif "how are you" in message:
        return "I'm doing great! Thanks for asking 😊. Please send me a keyword related to MOSDAC for more information."
    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a great day!"
    elif "who are you" in message:
        return "I'm your AI assistant powered specifically for MOSDAC portal!"
    elif "i can't understand this" in message or "please explain more" in message or "can you explain more?" in message or "explain more" in message:
        return "All the relevant information from knowledge graph has already been provided. Please search another entity or related keyword for better responses."
    return None

# Chat endpoint
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # First, check for basic reply cases
        basic_response = basic_reply(request.message)
        if basic_response:
            return {"reply": basic_response}
        
        # Else, go with NLP processing
        nlp_result = process_nlp(request.message)

        if not nlp_result:
            return {"reply": "Sorry, I couldn't extract any relevant information from that."}
        
        response = query_kg(nlp_result,request.message)

        return {"reply": response or "I processed your message, but couldn't find anything relevant in the knowledge graph."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Upload text file and process it
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type != "text/plain":
        raise HTTPException(status_code=400, detail="Only plain text files are accepted.")
    
    content = await file.read()
    text = content.decode("utf-8")

    # Process the uploaded text file using NLP
    entities = process_nlp(text)

    # Filter out cardinal entities if needed
    filtered_entities = {k: v for k, v in entities.items() if v != "CARDINAL"}

    summary = query_kg(filtered_entities)

    return {
        "filename": file.filename,
        "content_length": len(content),
        "entities_extracted": filtered_entities,
        "kg_summary": summary
    }
import spacy
import subprocess
import sys

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")


@app.get("/")
def read_root():
    return {"message": "AI HelpBot API is running 🚀"}
