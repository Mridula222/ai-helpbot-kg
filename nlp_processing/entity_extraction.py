import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Function to extract named entities from text
def extract_entities(text):
    doc = nlp(text)
    entities = []

    for ent in doc.ents:
        entities.append((ent.text, ent.label_))

    return entities

# Test the function
if __name__ == "__main__":
    sample_text = "ISRO launched SCATSAT-1 in 2016 for weather forecasting."
    result = extract_entities(sample_text)
    print("Extracted Entities:", result)
