from pathlib import Path
import json

import faiss
from sentence_transformers import SentenceTransformer


PROJECT_ROOT = Path(__file__).resolve().parent.parent

KNOWLEDGE_BASE_FILE = (
    PROJECT_ROOT / "okf" / "knowledge_base.json"
)

INDEX_FILE = (
    PROJECT_ROOT / "okf" / "knowledge.index"
)


def load_knowledge_base():

    with open(
        KNOWLEDGE_BASE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def semantic_retrieve(
    query,
    top_k=5,
    max_distance=1.2
):

    knowledge_base = load_knowledge_base()

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    index = faiss.read_index(
        str(INDEX_FILE)
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for distance, index_id in zip(
        distances[0],
        indices[0]
    ):

        # Ignore results that are not relevant enough
        if distance > max_distance:
            continue

        if index_id == -1:
            continue

        item = knowledge_base[index_id]

        results.append({
            "distance": float(distance),
            "id": item["id"],
            "source": item["source"],
            "metadata": item["metadata"],
            "content": item["content"]
        })

    return results


def print_results(query, results):

    print()
    print("Query:")
    print(query)

    print()
    print("Semantic Search Results:")
    print("-" * 70)

    for number, result in enumerate(
        results,
        start=1
    ):

        print()
        print(f"Result: {number}")
        print(f"Distance: {result['distance']:.4f}")
        print(f"Source: {result['source']}")
        print()
        print(result["content"][:500])
        print("-" * 70)


if __name__ == "__main__":

    query = input(
        "Enter your question: "
    )

    results = semantic_retrieve(
        query,
        top_k=5
    )

    print_results(
        query,
        results
    )