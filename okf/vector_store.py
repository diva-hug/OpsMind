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


def build_vector_store():

    print("Loading Knowledge base ......")

    knowledge_base = load_knowledge_base()

    print(
        f"Loaded {len(knowledge_base)} chunks."
    )

    print("Loading embedding model ....")

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    texts = [
        item["content"]
        for item in knowledge_base
    ]

    print("Creating Embedding......")

    embeddings = model.encode(
        texts,
        convert_to_numpy=True
    )

    print(
        f"Embedding Shape: {embeddings.shape}"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        embeddings
    )

    faiss.write_index(
        index,
        str(INDEX_FILE)
    )

    print()
    print("Vector store created successfully.")
    print(
        f"Vectors stored: {index.ntotal}"
    )
    print(
        f"Vector dimension: {dimension}"
    )
    print(
        f"Index file: {INDEX_FILE}"
    )


if __name__ == "__main__":

    build_vector_store()

