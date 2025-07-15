# 🧠 NLP Entity Extraction Module (Member 2)

This module is part of the **AI Help Bot** project developed for the Bharatiya Antariksh Hackathon. It is responsible for extracting named entities (like satellites, organizations, dates) from FAQ content scraped from the [MOSDAC](https://mosdac.gov.in) portal.

---

## 🔧 Responsibilities

- Load cleaned FAQ data
- Use spaCy to extract named entities
- Save extracted entities in a structured JSON file
- Share output for Knowledge Graph integration

---

## 📁 Files

| File | Description |
|------|-------------|
| `entity_extraction.py` | Reusable function to extract entities using spaCy |
| `process_faq_entities.py` | Script to process full FAQ data and output entities |
| `faq_entities.json` | Output file containing extracted entities |

---

## 🧠 Technologies Used

- Python 3.x
- spaCy (`en_core_web_sm`)
- JSON file processing

---

## ▶️ How to Run

1. Activate your virtual environment:
   ```bash
   venv\Scripts\activate

---

## ✅ Task Completion Note

✔️ Task completed by **Mridula Kumari (Member 2)**  
✔️ All entity extraction scripts are finalized and committed  
✔️ Output `faq_entities.json` ready for Neo4j integration  
✔️ Updated on: July 15, 2025

