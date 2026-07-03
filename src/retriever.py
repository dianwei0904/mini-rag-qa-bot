from pathlib import Path
import re


def load_knowledge_base(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Knowledge base file not found: {file_path}")

    return path.read_text(encoding="utf-8")


def split_documents(content: str) -> list[str]:
    sections = []
    current_section = []

    for line in content.splitlines():
        if line.startswith("## ") and current_section:
            sections.append("\n".join(current_section).strip())
            current_section = [line]
        else:
            current_section.append(line)

    if current_section:
        sections.append("\n".join(current_section).strip())

    return [section for section in sections if section.startswith("## ")]


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9]+", text.lower()))


def extract_product_name(text: str) -> str | None:
    match = re.search(r"product\s+([a-zA-Z0-9]+)", text.lower())

    if not match:
        return None

    return f"product {match.group(1)}"


def retrieve_relevant_docs(query: str, documents: list[str]) -> list[str]:
    query_tokens = tokenize(query)
    query_product = extract_product_name(query)
    matched_docs = []

    ignored_keywords = {
        "does",
        "do",
        "is",
        "are",
        "the",
        "a",
        "an",
        "support",
        "supports",
    }

    meaningful_keywords = query_tokens - ignored_keywords

    for doc in documents:
        doc_lower = doc.lower()
        doc_tokens = tokenize(doc)

        if query_product and query_product not in doc_lower:
            continue

        if meaningful_keywords & doc_tokens:
            matched_docs.append(doc)

    return matched_docs