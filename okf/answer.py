
from pathlib import Path
import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

from okf.semantic_retrieve import semantic_retrieve


PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_ROOT / ".env")


api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    raise ValueError("GROQ_API_KEY not found")


client = Groq(api_key=api_key)


def generate_answer(query):

    results = semantic_retrieve(
        query,
        top_k=5
    )

    if not results:
        return (
            "I could not find relevant information "
            "in the OpsMind knowledge base."
        )

    context_parts = []

    for result in results:

        context_parts.append(
            f"Source: {result['source']}\n"
            f"Content:\n{result['content']}"
        )

    context = "\n\n".join(context_parts)


    prompt = f"""
You are OpsMind, an internal engineering knowledge assistant.

Answer the user's question using ONLY the provided context.

If the answer is not available in the context,
say that the information is not available
in the OpsMind knowledge base.

Do not invent facts.

Context:
{context}

User Question:
{query}

Answer:
"""


    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )


    answer = response.choices[0].message.content


    sources = []

    for result in results:

        source = result["source"]

        if source not in sources:
            sources.append(source)


    source_text = "\n\nSources:\n"

    for source in sources:
        source_text += f"- {source}\n"


    return answer + source_text


if __name__ == "__main__":

    query = input("Enter your question: ")

    answer = generate_answer(query)

    print()
    print("OpsMind Answer:")
    print("-" * 70)
    print(answer)
    print("-" * 70)

