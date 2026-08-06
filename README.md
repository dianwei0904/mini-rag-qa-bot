# RAG Quality Validation Pipeline

A deterministic Retrieval-Augmented Generation pipeline designed to validate each RAG stage independently: document loading, section splitting, product-aware retrieval, prompt augmentation, response generation, and end-to-end output behavior.

The project focuses on QA observability and repeatability rather than external LLM integration. Every intermediate result is returned so retrieval errors, prompt issues, and unsupported answers can be tested directly.

## What It Demonstrates

| Area | Implementation |
|---|---|
| Knowledge source | Local Markdown FAQ |
| Document processing | Split FAQ content by Markdown section |
| Retrieval | Product filtering and keyword intersection |
| Prompt augmentation | Role, response rules, question, retrieved documents, and output format |
| Generation | Deterministic rule-based response generator |
| Traceability | Returns question, retrieved documents, prompt, and answer |
| Validation | Pytest coverage for retriever, augmenter, and complete pipeline |

## Pipeline Flow

```text
User Question
    ↓
Load Markdown Knowledge Base
    ↓
Split Content into Product Sections
    ↓
Filter by Product Name
    ↓
Match Target Keywords
    ↓
Build Grounded Prompt
    ↓
Generate Deterministic Answer
    ↓
Return Retrieval, Prompt, and Answer Evidence
```

## Test Scenarios

| Scenario | Expected Behavior |
|---|---|
| Product A macOS question | Retrieve only the macOS driver requirement |
| Product A iOS 19 question | Retrieve iOS support data but refuse to confirm unsupported iOS 19 |
| Unknown Product Z question | Return no documents and an insufficient-data response |
| Product-specific query | Prevent Windows or iOS content from leaking into a macOS answer |
| Prompt construction | Include grounding rules and required output fields |
| End-to-end pipeline | Return `question`, `retrieved_docs`, `prompt`, and `answer` |

## Answer Contract

Every generated answer follows this structure:

```text
Conclusion:
Evidence:
Limitation:
```

This structure makes the result easier to verify and prevents unsupported confidence from being hidden inside free-form text.

## Key Engineering Decisions

- The pipeline exposes intermediate results instead of returning only the final answer.
- Product-name filtering prevents knowledge from one product being applied to another.
- Stop words and product codes are removed before keyword matching.
- Retrieval and generation are deterministic, allowing repeatable automated assertions.
- The prompt requires the answer to use retrieved documents only.
- Unsupported questions return an explicit insufficient-data response.
- Components are separated into retriever, augmenter, generator, and pipeline modules so each stage can be tested independently.

## Tech Stack

Python · Pytest · uv · Markdown Knowledge Base · Regular Expressions

## Project Structure

```text
mini-rag-qa-bot/
├── data/
│   └── product_faq.md
├── src/
│   ├── augmenter.py
│   ├── generator.py
│   ├── rag_pipeline.py
│   └── retriever.py
├── tests/
│   ├── test_augmenter.py
│   ├── test_rag_pipeline.py
│   └── test_retriever.py
├── demo.py
├── pyproject.toml
├── pytest.ini
├── uv.lock
└── README.md
```

## Run Locally

Install the locked environment:

```bash
uv sync
```

Run the test suite:

```bash
uv run pytest -v
```

Run the demonstration script:

```bash
uv run python demo.py
```

## Validation Strategy

### Retrieval validation

- Confirm the knowledge base loads correctly.
- Confirm the Markdown file is split into the expected sections.
- Confirm relevant documents are returned.
- Confirm unrelated sections are excluded.
- Confirm unknown products return an empty result.

### Prompt validation

- Confirm retrieved evidence is included.
- Confirm outside knowledge is prohibited.
- Confirm product information cannot be mixed.
- Confirm the required answer format is present.
- Confirm missing evidence is represented explicitly.

### Pipeline validation

- Confirm all traceability fields are returned.
- Confirm supported answers contain the correct evidence.
- Confirm unsupported claims are not presented as facts.
- Confirm every answer includes conclusion, evidence, and limitation.

## Current Limitations

- Retrieval uses explicit product parsing and keyword matching rather than embeddings.
- The generator is deterministic and does not call an external LLM.
- The knowledge base contains a small fixed FAQ dataset.
- There is no API, user interface, vector database, persistence, or document upload.
- The implementation is optimized for testability and traceability, not semantic search coverage.

## Portfolio Value

This project demonstrates AI testing methodology by validating RAG as a multi-stage system rather than treating the final answer as a black box. It covers retrieval relevance, irrelevant-context exclusion, prompt grounding, insufficient-evidence handling, product-boundary protection, structured responses, and deterministic regression testing.

## Interview Talking Points

- Why test retrieval separately from the final generated answer?
- How does product filtering prevent cross-product hallucination?
- Why is deterministic generation useful during automated testing?
- What limitations does keyword matching have compared with embedding retrieval?
- How would you add semantic retrieval without losing test repeatability?
- Which metrics would you use to evaluate retrieval quality?
- How would this pipeline detect unsupported claims from a real LLM?

## Resume Highlight

> Built a deterministic RAG quality-validation pipeline that tests document retrieval, irrelevant-context exclusion, prompt grounding, insufficient-evidence handling, structured responses, and end-to-end traceability with Pytest.
