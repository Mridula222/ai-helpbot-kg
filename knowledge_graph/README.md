# 🧠 Knowledge Graph Module (Member 3)

This module is part of the **AI Help Bot** project developed for the Bharatiya Antariksh Hackathon. It is responsible for organizing structured information extracted from the MOSDAC portal into a queryable **Knowledge Graph**.

This graph is used by the bot to fetch contextual, accurate responses based on user queries processed by the NLP module.

---

## 🔧 Responsibilities

- Create and maintain a structured Knowledge Graph in JSON format
- Define relationships between entities (e.g., data type → satellite → source)
- Provide a clean function to query entities using parameters like `entity` and `location`
- Serve as the information base for the backend to answer user queries

---

## 📁 Files

| File                | Description                                               |
| ------------------- | --------------------------------------------------------- |
| `kg_data.json`      | Stores the knowledge graph (entities, locations, sources) |
| `kg_query.py`       | Core script to query the graph using entity and location  |
| `kg_builder.py`     | (Optional) Script to auto-generate or update the KG       |
| `sample_queries.py` | For testing the KG logic manually                         |
| `.gitkeep`          | Keeps the folder tracked in version control               |
| `README.md`         | Documentation of this module                              |

---

## 🧠 Technologies Used

- Python 3.x
- JSON
- Basic I/O and query logic

---

## ▶️ How to Use

1. Open `sample_queries.py`
2. Modify or run predefined test cases to check responses
3. Import `query_kg()` into backend or other modules as needed

Example usage:

```python
from kg_query import query_kg
print(query_kg("rainfall", "Odisha"))
```

## ✅ Task Completion Note

✔️ Task completed by **Shubhasmita Dash (Member 3)**  
✔️ Knowledge graph files structured and queryable  
✔️ Interface ready for NLP integration  
✔️ Updated on: July 16, 2025
