from kg_query import query_kg

def main():
    queries = ["MOSDAC", "INSAT-3D", "SCATSAT-1", "NonexistentEntity"]

    for q in queries:
        result = query_kg(q)
        if result:
            print(f"Query: {q}")
            print(f"Description: {result['description']}")
            print(f"Related Entities: {result['related_entities']}\n")
        else:
            print(f"Query: {q} - No information found.\n")

if __name__ == "__main__":
    main()
