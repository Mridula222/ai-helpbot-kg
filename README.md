# 🛰️ AI Help Bot: ISRO Knowledge Assistant

This project is an AI-powered chatbot that answers user queries about ISRO satellite missions by extracting and structuring data from MOSDAC resources. It integrates web scraping, NLP-based entity extraction, a Neo4j-based knowledge graph, and a LangChain RAG system into an interactive web interface.

---

## 📁 Project Structure

ai-helpbot-kg/
├── backend/ # Flask API backend + RAG integration
├── frontend/ # React/Vite frontend
├── data_ingestion/ # Scrapers and parsers (HTML, PDF, DOCX, XLSX)
├── nlp_processing/ # Entity extraction logic
├── knowledge_graph/ # Neo4j setup and Cypher scripts
├── models/ # Embedding models (OpenAI/Local)
└── README.md # Project documentation



---

## 👥 Team Roles & Contributions

### 🧾 Member 1 – Data Engineer (Scraper & Parser)
**Folder:** `data_ingestion/`

**Responsibilities:**
- Created `scrape_mosdac.py` to extract content from the MOSDAC portal.
- Used tools like `requests`, `BeautifulSoup`, and `selenium` for dynamic and static scraping.
- Parsed various document formats:
  - PDFs using `pdfplumber`
  - DOCX using `python-docx`
  - XLSX using `openpyxl`
- Output: Clean, structured textual data for downstream NLP processing.

---

### 🤖 Member 2 – NLP Engineer (Entity Extraction)
**Folder:** `nlp_processing/`

**Responsibilities:**
- Developed `entity_extraction.py` using `spaCy` and `nltk`.
- Extracted named entities like:
  - Satellite names
  - Launch years
  - Applications (e.g., weather, agriculture)
  - Instruments and sensors
- Output: JSON format of entities and relationships for graph insertion.

---

### 🧩 Member 3 – Knowledge Graph Architect
**Folder:** `knowledge_graph/`

**Responsibilities:**
- Set up Neo4j locally or with AuraDB.
- Created `neo4j_setup.ipynb` to:
  - Connect to the graph
  - Insert entity relationships using Cypher
- Defined node types (e.g., `Satellite`, `LaunchYear`, `Purpose`) and their edges.
- Verified relationships with visual graph exploration.

---

### 🧠 Member 4 – Full Stack & RAG Engineer
**Folders:** `backend/`, `frontend/`, `models/`

**Responsibilities:**
- Built a REST API using Flask (`app.py`) to connect frontend ↔ backend.
- Integrated RAG pipeline in `rag_integration.py` using:
  - `LangChain` for document retrieval
  - `OpenAI`/custom embeddings for answer generation
- Developed a Streamlit UI (`streamlit_app.py`) and a React + Vite chatbot.
- User flow: Query → Backend → Search + Generate → Return Answer + Source

---

## 🚀 Running the Project

### 1. Backend (FastAPI / Flask + LangChain)
```bash
cd backend/
uvicorn app.main:app --reload

Frontend (React + Vite)
cd frontend/chat-bot
npm install
npm run dev

Streamlit UI (Optional)
cd backend/
streamlit run streamlit_app.py
