
# 🧾 Data Ingestion Module (Member 1 - Team Leader)

This module is part of the **AI Help Bot** project developed for the **Bharatiya Antariksh Hackathon**. It focuses on collecting and preparing structured data from both the **MOSDAC website** and **official documents** for further processing in NLP and Knowledge Graph modules.

---

## 🔧 Responsibilities

- ✅ Scrape **FAQs** from the [MOSDAC FAQ page](https://mosdac.gov.in/faq-page)
- ✅ Parse local documents in **PDF, DOCX, XLSX** formats
- ✅ Save extracted content in `.txt` and `.json` formats
- ✅ Merge all cleaned content into a **master dataset** for downstream NLP

---

## 📁 Folder Structure

```
data_ingestion/
├── docs/                     # Input documents (PDF, DOCX, XLSX)
├── parsed_output/            # Output text files and cleaned data
│   ├── sample_docx.txt
│   ├── sample_pdf.txt
│   ├── sample_xlsx.txt
│   ├── mosdac_faqs.txt
│   ├── mosdac_faqs.json
│   └── master_dataset.txt
├── process_all_data.py       # Main script: scrape + parse + save
└── README.md                 # This file
```

---

## 📦 Dependencies

Install required packages via pip:

```bash
pip install -r requirements.txt
```

You’ll need the following:

- `requests`
- `beautifulsoup4`
- `selenium`
- `webdriver-manager`
- `pdfplumber`
- `python-docx`
- `openpyxl`

---

## ▶️ How to Run

1. Add your `.pdf`, `.docx`, `.xlsx` files to:

```
data_ingestion/docs/
```

2. Run the main script:

```bash
python data_ingestion/process_all_data.py
```

3. After execution:

- Extracted FAQs are saved as:
  - `mosdac_faqs.json` (machine-readable)
  - `mosdac_faqs.txt` (human-readable)
- Document contents are saved as:
  - `sample_pdf.txt`, `sample_docx.txt`, `sample_xlsx.txt`
- Combined output:
  - `master_dataset.txt`

---

## ✅ Sample Output

```text
data_ingestion/parsed_output/
├── mosdac_faqs.txt
├── mosdac_faqs.json
├── sample_pdf.txt
├── sample_docx.txt
├── sample_xlsx.txt
└── master_dataset.txt
```

---

## 👨‍💻 Author

- **Member 1**: Loralin Sahoo  
- **Role**: Data Engineer & Team Leader  
- **Completion Date**: July 16, 2025

---

## 🧠 Next Steps

This module outputs `master_dataset.txt` for:

- Member 2 → NLP entity extraction  
- Member 3 → Knowledge Graph generation  
- Member 4 → Backend chatbot + RAG

---

## 📌 Status

✔️ Module complete  
✔️ Tested with dummy files  
✔️ Output verified and clean
