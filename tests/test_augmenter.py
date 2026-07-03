from src.augmenter import build_augmented_prompt


def test_prompt_contains_user_question():
    question = "Does Product A support macOS?"
    retrieved_docs = [
        "## Product A - macOS Driver Requirement\nProduct A can be used on macOS only when the additional macOS driver is installed."
    ]

    prompt = build_augmented_prompt(question, retrieved_docs)

    assert question in prompt


def test_prompt_contains_retrieved_documents():
    question = "Does Product A support macOS?"
    retrieved_docs = [
        "## Product A - macOS Driver Requirement\nProduct A can be used on macOS only when the additional macOS driver is installed."
    ]

    prompt = build_augmented_prompt(question, retrieved_docs)

    assert "Product A - macOS Driver Requirement" in prompt
    assert "additional macOS driver" in prompt


def test_prompt_contains_response_rules():
    question = "Does Product A support macOS?"
    retrieved_docs = []

    prompt = build_augmented_prompt(question, retrieved_docs)

    assert "Use only the retrieved documents as the source of truth." in prompt
    assert "Do not use outside knowledge." in prompt
    assert "available data is insufficient" in prompt


def test_prompt_contains_required_output_format():
    question = "Does Product A support macOS?"
    retrieved_docs = []

    prompt = build_augmented_prompt(question, retrieved_docs)

    assert "Conclusion:" in prompt
    assert "Evidence:" in prompt
    assert "Limitation:" in prompt


def test_prompt_handles_empty_retrieved_documents():
    question = "Does Product A support Android?"
    retrieved_docs = []

    prompt = build_augmented_prompt(question, retrieved_docs)

    assert "No relevant documents were found." in prompt