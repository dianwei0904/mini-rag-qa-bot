# Mini RAG QA Bot

A testable mini RAG-based QA bot with Retrieval, Augmentation, mock Generation, and pytest validation.

This project focuses on building a small but verifiable RAG workflow.  
Instead of only generating an answer, the system separates the process into clear layers and validates each layer with automated tests.

---

## Project Goal

The goal of this project is to demonstrate how a RAG system can be tested from a QA perspective.

This project covers:

- Retrieval: finding relevant documents from a local knowledge base
- Augmentation: building a structured prompt with rules and retrieved documents
- Generation: producing a deterministic mock answer
- Validation: using pytest to verify the RAG flow

The first version uses a mock generator instead of a real LLM API to keep the test results stable and repeatable.

---

## Why This Project Matters

RAG systems are not correct just because they return an answer.

A reliable RAG system should also verify:

- Whether the correct documents were retrieved
- Whether unrelated documents were excluded
- Whether the prompt contains clear response rules
- Whether insufficient data is handled safely
- Whether the final answer follows the expected format

This project demonstrates how QA thinking can be applied to AI application development.

---

## Tech Stack

| Category | Tool |
|---|---|
| Language | Python |
| Package Manager | uv |
| Test Framework | pytest |
| Knowledge Base | Local Markdown file |
| Generation | Mock Generator |
| Architecture | RAG |

---

## Project Structure

```text
mini-rag-qa-bot/
├── data/
│   └── product_faq.md
├── src/
│   ├── __init__.py
│   ├── retriever.py
│   ├── augmenter.py
│   ├── generator.py
│   └── rag_pipeline.py
├── tests/
│   ├── test_retriever.py
│   ├── test_augmenter.py
│   └── test_rag_pipeline.py
├── .gitignore
├── pytest.ini
├── README.md
├── pyproject.toml
└── uv.lock