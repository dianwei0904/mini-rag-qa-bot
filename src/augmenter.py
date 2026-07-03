def build_augmented_prompt(question: str, retrieved_docs: list[str]) -> str:
    """
    Build an augmented prompt for the RAG pipeline.

    The prompt includes:
    - role definition
    - response rules
    - user question
    - retrieved documents
    - required output format
    """
    if retrieved_docs:
        docs_text = "\n\n".join(retrieved_docs)
    else:
        docs_text = "No relevant documents were found."

    prompt = f"""
Role:
You are a QA-focused AI assistant.

Task:
Answer the user's question based only on the retrieved documents.

Response Rules:
1. Use only the retrieved documents as the source of truth.
2. Do not use outside knowledge.
3. If the retrieved documents do not contain enough information, say that the available data is insufficient.
4. Do not apply information from one product to another product.
5. Keep the answer clear and concise.

User Question:
{question}

Retrieved Documents:
{docs_text}

Required Output Format:
Conclusion:
Evidence:
Limitation:
""".strip()

    return prompt