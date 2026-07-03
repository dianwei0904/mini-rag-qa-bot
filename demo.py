from src.rag_pipeline import run_rag_pipeline


def main():
    print("Mini RAG QA Bot")
    print("Type your question and press Enter.")
    print("Type 'exit' to quit.")
    print("-" * 50)

    while True:
        question = input("\nQuestion: ").strip()

        if question.lower() in ["exit", "quit", "q"]:
            print("Goodbye.")
            break

        if not question:
            print("Please enter a question.")
            continue

        result = run_rag_pipeline(question)

        print("\nAnswer:")
        print(result["answer"])

        show_sources = input("\nShow retrieved documents? (y/N): ").strip().lower()

        if show_sources == "y":
            print("\nRetrieved Documents:")

            if result["retrieved_docs"]:
                for index, doc in enumerate(result["retrieved_docs"], start=1):
                    print(f"\n[{index}]")
                    print(doc)
            else:
                print("No relevant documents were found.")


if __name__ == "__main__":
    main()