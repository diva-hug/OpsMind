from pathlib  import Path
import json
import re

PROJECT_ROOT =Path(__file__).resolve().parent.parent

KNOWLEDGE_BASE_FILE = (
    PROJECT_ROOT /"okf"/"knowledge_base.json"
)


def load_knowledge_base():
    with open(
        KNOWLEDGE_BASE_FILE,
        "r",
        encoding="utf-8"
    )as file:
        return json.load(file)

def normalize_text(text):
    text=text.lower()
    text=re.sub(r"[^a-z0-9\s-]"," ",text)
    text =re.sub(r"\s+"," ",text)

    return text.strip()

def calculate_score(query,content):
    query_words=set(
        normalize_text(query).split()
    )

    content_words =set(
        normalize_text(content).split()
    )

    if not query_words:
        return 0

    matched_words =query_words.intersection(
        content_words
    )

    return len(matched_words)/len(query_words)


def retrieve (query , top_k=5):

    knowledge_base = load_knowledge_base()

    results =[]

    for item in knowledge_base:
        score = calculate_score(
            query,
            item["content"]
        )

        if score>0:

            results.append({
                "score":score,
                "id":item["id"],
                "source":item["source"],
                "metadata": item["metadata"],
                "content":item["content"]


            })

    results.sort(
        key=lambda x:x["score"],
        reverse=True
    )

    return results[:top_k]
def print_results(query,results):
    print()
    print("Query:")
    print(query)

    print()
    print("Retrieved Results:")
    print("-" * 70)

    for index, result in enumerate(results,start=1):

        print()
        print(f"Result:{index}")
        print(f"Score: {result['score']:.3f}")
        print(f"ID:{result['id']}")
        print()
        print(result["content"][:500])
        print("-"*70)

if __name__ =="__main__":
    query = input(
        "Enter your question :"
    )

    results = retrieve(
        query,
        top_k=5
    )

    print_results(
        query,
        results
    )

