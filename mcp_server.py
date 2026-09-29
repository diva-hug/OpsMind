from pathlib import Path
import json

from mcp.server import MCPServer


PROJECT_ROOT = Path(__file__).resolve().parent

KNOWLEDGE_BASE_FILE = (
    PROJECT_ROOT / "okf" / "knowledge_base.json"
)


mcp = MCPServer("OpsMind")


def load_knowledge_base():
    with open(
        KNOWLEDGE_BASE_FILE,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


@mcp.tool()
def search_knowledge(query: str) -> str:
    """
    Search the OpsMind knowledge base.
    """

    knowledge_base = load_knowledge_base()

    query_words = set(
        query.lower().split()
    )

    results = []

    for item in knowledge_base:
        content = item["content"].lower()

        matched_words = [
            word
            for word in query_words
            if word in content
        ]

        if matched_words:
            results.append(
                {
                    "score": len(matched_words),
                    "source": item["source"],
                    "content": item["content"]
                }
            )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    results = results[:5]

    if not results:
        return (
            "No relevant information found "
            "in the OpsMind knowledge base."
        )

    output = []

    for result in results:
        output.append(
            f"Source: {result['source']}\n"
            f"Content:\n{result['content']}"
        )

    return "\n\n---\n\n".join(output)


@mcp.tool()
def search_incidents(query: str) -> str:
    """
    Search incident records in OpsMind.
    """

    knowledge_base = load_knowledge_base()

    query_words = set(
        query.lower().split()
    )

    results = []

    for item in knowledge_base:

        source = item["source"].lower()

        if "inc-" not in source:
            continue

        content = item["content"].lower()

        matched_words = [
            word
            for word in query_words
            if word in content
        ]

        if matched_words:
            results.append(
                {
                    "score": len(matched_words),
                    "source": item["source"],
                    "content": item["content"]
                }
            )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    results = results[:5]

    if not results:
        return "No matching incidents found."

    output = []

    for result in results:
        output.append(
            f"Incident: {result['source']}\n"
            f"{result['content']}"
        )

    return "\n\n---\n\n".join(output)


@mcp.tool()
def get_service_dependencies(service: str) -> str:
    """
    Find dependency information for a service.
    """

    knowledge_base = load_knowledge_base()

    service = service.lower()

    results = []

    for item in knowledge_base:

        source = item["source"].lower()
        content = item["content"].lower()

        if service in source or service in content:

            if (
                "depend" in content
                or "service" in content
            ):
                results.append(
                    f"Source: {item['source']}\n"
                    f"{item['content']}"
                )

    if not results:
        return (
            f"No dependency information found "
            f"for {service}."
        )

    return "\n\n---\n\n".join(results[:5])


if __name__ == "__main__":
    mcp.run()
            
            


    