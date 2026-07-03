from src.retriever import load_knowledge_base
from src.retriever import split_documents
from src.retriever import retrieve_relevant_docs
from src.augmenter import build_augmented_prompt
from src.generator import generate_answer


def run_rag_pipeline(question: str, faq_path: str = "data/product_faq.md") -> dict:
    content = load_knowledge_base(faq_path)
    documents = split_documents(content)
    retrieved_docs = retrieve_relevant_docs(question, documents)
    prompt = build_augmented_prompt(question, retrieved_docs)
    answer = generate_answer(prompt)

    result = {
        "question": question,
        "retrieved_docs": retrieved_docs,
        "prompt": prompt,
        "answer": answer,
    }

    return result