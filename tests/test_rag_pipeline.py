from src.rag_pipeline import run_rag_pipeline


def test_pipeline_returns_required_keys():
    result = run_rag_pipeline("Does Product A support macOS?")

    assert "question" in result
    assert "retrieved_docs" in result
    assert "prompt" in result
    assert "answer" in result


def test_pipeline_answer_contains_required_sections():
    result = run_rag_pipeline("Does Product A support macOS?")
    answer = result["answer"]

    assert "Conclusion:" in answer
    assert "Evidence:" in answer
    assert "Limitation:" in answer


def test_pipeline_answers_product_a_macos_with_driver_requirement():
    result = run_rag_pipeline("Does Product A support macOS?")
    answer = result["answer"]

    assert "additional macOS driver" in answer
    assert "driver-free macOS support" in answer


def test_pipeline_does_not_confirm_ios_19_support():
    result = run_rag_pipeline("Does Product A support iOS 19?")
    answer = result["answer"]

    assert "insufficient to confirm iOS 19 support" in answer
    assert "iOS 17 and iOS 18" in answer
    assert "does not mention iOS 19 support" in answer


def test_pipeline_handles_unknown_product_question():
    result = run_rag_pipeline("Does Product Z support Android?")
    answer = result["answer"]

    assert "insufficient" in answer.lower()
    assert "Conclusion:" in answer
    assert "Evidence:" in answer
    assert "Limitation:" in answer