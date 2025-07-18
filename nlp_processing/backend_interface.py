import spacy

nlp = spacy.load("en_core_web_sm")

def process_nlp(text):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        entities[ent.text] = ent.label_

    # Manual fallback for domain-specific keywords if spaCy finds nothing
    if not entities:
        lowered = text.lower()
        known_keywords = {
            "mosdac": "ORG",
            "insat-3d": "PRODUCT",
            "rainfall": "DATA",
            "nowcasting": "FEATURE",
            # add more as needed
        }
        for key, label in known_keywords.items():
            if key in lowered:
                entities[key.capitalize()] = label  # Capitalize for consistency
    return entities
