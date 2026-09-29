from pathlib import Path
import json
import re


PROJECT_ROOT = Path(__file__).resolve().parent.parent

KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"
OUTPUT_FILE = PROJECT_ROOT / "okf" / "knowledge_base.json"


def extract_frontmatter(content):
    metadata = {}

    if not content.startswith("---"):
        return metadata

    parts = content.split("---", 2)

    if len(parts) < 3:
        return metadata

    frontmatter = parts[1].strip()

    for line in frontmatter.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()

    return metadata


def remove_frontmatter(content):
    if not content.startswith("---"):
        return content.strip()

    parts = content.split("---", 2)

    if len(parts) < 3:
        return content.strip()

    return parts[2].strip()


def create_chunks(content):
    sections = re.split(r"\n(?=#{1,6}\s)", content)

    chunks = []

    for section in sections:
        section = section.strip()

        if section:
            chunks.append(section)

    return chunks


def build_knowledge_base():

    knowledge_base = []

    markdown_files = [
        file for file in PROJECT_ROOT.rglob("*.md")
        if "venv" not in file.parts
        and ".git" not in file.parts
        and "okf" not in file.parts
    ]

    for file_path in markdown_files:

        content = file_path.read_text(
            encoding="utf-8"
        )

        metadata = extract_frontmatter(content)

        clean_content = remove_frontmatter(content)

        chunks = create_chunks(clean_content)

        for index, chunk in enumerate(chunks):

            knowledge_base.append({
                "id": f"{file_path.stem}--{index}",
                "source": file_path.name,
                "metadata": metadata,
                "content": chunk
            })

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT_FILE.write_text(
        json.dumps(
            knowledge_base,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    print(
        f"Created {OUTPUT_FILE} "
        f"with {len(knowledge_base)} chunks"
    )


if __name__ == "__main__":
    build_knowledge_base()