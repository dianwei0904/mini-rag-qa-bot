from src.retriever import load_knowledge_base, split_documents, retrieve_relevant_docs


FAQ_PATH = "data/product_faq.md"


def test_load_knowledge_base():
    content = load_knowledge_base(FAQ_PATH)

    assert "Product A" in content
    assert "Product B" in content


def test_split_documents():
    content = load_knowledge_base(FAQ_PATH)
    documents = split_documents(content)

    assert len(documents) == 5
    assert documents[0].startswith("## Product A - Windows Support")


def test_retrieve_product_a_macos_docs():
    content = load_knowledge_base(FAQ_PATH)
    documents = split_documents(content)

    results = retrieve_relevant_docs("Does Product A support macOS?", documents)

    assert any("Product A - macOS Driver Requirement" in doc for doc in results)


def test_retrieve_ios_support_docs():
    content = load_knowledge_base(FAQ_PATH)
    documents = split_documents(content)

    results = retrieve_relevant_docs("Does Product A support iOS 19?", documents)

    assert any("Product A - iOS Support" in doc for doc in results)


def test_retrieve_unknown_product_should_return_empty():
    content = load_knowledge_base(FAQ_PATH)
    documents = split_documents(content)

    results = retrieve_relevant_docs("Does Product Z support Android?", documents)

    assert results == []