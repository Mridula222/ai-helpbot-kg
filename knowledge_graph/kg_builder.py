import json

def build_knowledge_graph(input_file='../nlp_processing/faq_entities.json', output_file='kg_data.json'):
    with open(input_file, 'r') as f:
        faqs = json.load(f)

    kg = {}

    for faq in faqs:
        question = faq.get('question', '')
        answer = faq.get('answer', '')
        entities = faq.get('entities', [])
        entity_names = [e[0] for e in entities]

        for entity_name, entity_type in entities:
            if entity_name not in kg:
                kg[entity_name] = {
                    'type': entity_type,
                    'description': '',
                    'related_entities': [],
                    'info': []
                }
            if not kg[entity_name]['description']:
                kg[entity_name]['description'] = answer
            related = [e for e in entity_names if e != entity_name]
            for rel in related:
                if rel not in kg[entity_name]['related_entities']:
                    kg[entity_name]['related_entities'].append(rel)
            if answer and answer not in kg[entity_name]['info']:
                kg[entity_name]['info'].append(answer)
    with open(output_file, 'w') as f:
        json.dump(kg, f, indent=2)
    print(f"Knowledge graph built and saved to '{output_file}'")

if __name__ == "__main__":
    build_knowledge_graph()
