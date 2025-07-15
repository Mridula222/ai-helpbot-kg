import json
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    """Extract named entities using spaCy"""
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def process_faq_file(input_path, output_path):
    """Read FAQ JSON, extract entities, save to new JSON"""
    with open(input_path, "r", encoding="utf-8") as f:
        faqs = json.load(f)

    processed = []
    for faq in faqs:
        question = faq.get("question", "")
        answer = faq.get("answer", "")
        entities = extract_entities(answer)

        processed.append({
            "question": question,
            "answer": answer,
            "entities": entities
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(processed, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    input_file = "data_ingestion/mosdac_faqs.json"
    output_file = "nlp_processing/faq_entities.json"
    process_faq_file(input_file, output_file)
    print(f"✅ Entity extraction completed. Output saved to: {output_file}")
