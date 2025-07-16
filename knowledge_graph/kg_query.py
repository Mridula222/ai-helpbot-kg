import json
import os

# Load the knowledge graph JSON once at module load for efficiency
KG_FILE = os.path.join(os.path.dirname(__file__), 'kg_data.json')

try:
    with open(KG_FILE, 'r') as f:
        knowledge_graph = json.load(f)
except FileNotFoundError:
    print(f"Error: {KG_FILE} not found. Make sure kg_data.json exists.")
    knowledge_graph = {}

def query_kg(entity_name):
    """
    Query the knowledge graph for an entity.
    
    Args:
        entity_name (str): The entity to search for.
        
    Returns:
        dict: Information about the entity including description, related entities, and info list.
              Returns None if entity not found.
    """
    entity_name = entity_name.strip()
    entity_data = knowledge_graph.get(entity_name)

    if entity_data:
        return {
            "entity": entity_name,
            "type": entity_data.get("type", "Unknown"),
            "description": entity_data.get("description", ""),
            "related_entities": entity_data.get("related_entities", []),
            "info": entity_data.get("info", [])
        }
    else:
        return None

# Example usage for quick testing
# if __name__ == "__main__":
#     test_entity = "MOSDAC"
#     result = query_kg(test_entity)
#     if result:
#         print(f"Info for '{test_entity}':")
#         print(f"Type: {result['type']}")
#         print(f"Description: {result['description']}")
#         print(f"Related Entities: {', '.join(result['related_entities'])}")
#         print(f"Additional Info: {result['info']}")
#     else:
#         print(f"Entity '{test_entity}' not found in knowledge graph.")
