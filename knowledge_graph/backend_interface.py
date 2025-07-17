from kg_query import query_kg as query_kg_from_module

def query_kg(nlp_data: dict) -> str:
    """
    Given NLP extracted entities (dict), query KG for each entity.
    Return a combined string summary of found entities.
    """
    if not nlp_data:
        return "Sorry, I couldn't find any entities in your message."

    responses = []
    for entity in nlp_data.keys():
        result = query_kg_from_module(entity)
        if result:
            desc = result.get("description", "No description available.")
            responses.append(f"{entity}: {desc}")
    
    if responses:
        return "\n".join(responses)
    else:
        return "No matching information found in the knowledge graph for the entities you mentioned."
