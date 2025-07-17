from entity_extraction import extract_entities

def process_nlp(message: str) -> dict:
    """
    Given user message text, extract named entities using spaCy.
    Returns a dict with entity texts and labels.
    """
    entities = extract_entities(message)
    # For simplicity, return as dict {entity_text: label}
    return {ent[0]: ent[1] for ent in entities}
