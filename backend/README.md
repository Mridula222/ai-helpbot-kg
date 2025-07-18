# 🚀 Backend Module (Member 3)

This module is part of the **AI Help Bot** project developed for the Bharatiya Antariksh Hackathon. It serves as the **core backend API** that connects the frontend user interface with the NLP and Knowledge Graph modules.

It is built using **FastAPI**, ensuring a high-performance and scalable structure to handle user requests and route them to the appropriate logic layers.

---

## 🔧 Responsibilities

- Expose API endpoints to serve chat-based queries
- Connect with the NLP module to extract entities and intent
- Interface with the Knowledge Graph to fetch relevant data
- Handle response construction and send it to the frontend
- Act as a central controller coordinating between all AI modules

---

## 📁 Files & Structure

| File/Folder        | Description                                                      |
| ------------------ | ---------------------------------------------------------------- |
| `app/main.py`      | Main FastAPI application – defines routes and integrates modules |
| `requirements.txt` | Lists Python dependencies                                        |
| `.gitignore`       | Specifies files/folders to ignore in version control             |
| `.gitkeep`         | Keeps empty folders tracked (if any)                             |
| `README.md`        | You're reading it!                                               |
| `venv/`            | (Optional) Python virtual environment folder                     |

---

## 🧠 Technologies Used

- **FastAPI** for backend routing and API development
- **Uvicorn** as the ASGI server (recommended for running FastAPI apps)
- **Python 3.x**
- **Pydantic** for request/response validation
- **CORS middleware** for secure cross-origin communication with the frontend

---

## ▶️ How to Run Locally

1.  **Clone the repo** (if not already):
    ```bash
    git clone <repo-url>
    cd backend
    ```
2.  **(Optional) Activate virtual environment:**

    ```bash
    source venv/bin/activate # Linux/macOS
    .\venv\Scripts\activate # Windows
    ```

3.  **Install dependencies:**

        ```bash
        pip install -r requirements.txt
        ```

4.  **Run the FastAPI server:**

        ```bash
        uvicorn app.main:app --reload

    The API will be available at:
    👉 http://127.0.0.1:8000

Explore interactive docs:
FastAPI provides Swagger UI:
👉 http://127.0.0.1:8000/docs

## ✅ Task Completion Note

✔️ Task completed by Shubhasmita Dash (Member 3) <br>
✔️ FastAPI backend fully functional and integrated with AI modules <br>
✔️ Supports clean API structure for frontend consumption <br>
✔️ Updated on: July 17, 2025 <br>
