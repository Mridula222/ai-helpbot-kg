import spacy

nlp = spacy.load("en_core_web_sm")  # Make sure the model is installed with: python -m spacy download en_core_web_sm

def process_nlp(text):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        entities[ent.text] = ent.label_
    return entities
