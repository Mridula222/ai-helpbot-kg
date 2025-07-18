from kg_query import query_kg as query_kg_from_module

# Add basic canned Q&A responses for common queries
basic_responses = {
    "what is mosdac": "MOSDAC is the Meteorological and Oceanographic Satellite Data Archival Centre, an ISRO facility for satellite data dissemination and archival.",
    "which satellite provides rainfall data": "INSAT-3D and INSAT-3DR satellites provide rainfall data as per MOSDAC datasets.",
    "what is nowcasting in mosdac": "Nowcasting provides short-term weather predictions using satellite observations, updated every 15 minutes on MOSDAC.",
    "show today's rainfall data": "Today's rainfall data:\n• Rainfall (mm): 25\n• Region: Eastern India\nSource: MOSDAC Rainfall Monitoring (link).",
    "how can i access satellite data from mosdac": "You can access satellite data by registering on the MOSDAC data portal at https://www.mosdac.gov.in/data.",
    "how to download data from mosdac": "To download data, login to your MOSDAC account, navigate to the Data section, select your desired dataset, and click ‘Download’.",
}

def query_kg(nlp_data: dict, user_query: str = "") -> str:
    """
    Given NLP extracted entities (dict) and the original user query (string),
    return a relevant response either from basic canned replies or from KG.
    """
    # Normalize user query for simple matching
    normalized_query = user_query.lower().strip()

    # Check if user query matches any basic canned response key phrase
    for key_phrase, response in basic_responses.items():
        if key_phrase in normalized_query:
            return response

    # Fallback to knowledge graph query using extracted entities
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
