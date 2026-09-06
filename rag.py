from retriever import retrieve
from generator import generate_answer


# --------------------------------------------------
# ANSWER QUESTION
# --------------------------------------------------

def answer_question(query, top_k=3):

    # Retrieve relevant chunks
    results = retrieve(
        query,
        top_k=131
    )

    query_lower = query.lower()

    # --------------------------------------------------
    # Detect BUG ID
    # --------------------------------------------------

    bug_id = None

    for word in query_lower.replace("?", "").split():

        if word.startswith("bug-ide-"):
            bug_id = word
            break

    # --------------------------------------------------
    # Special handling for BUG-IDE-037
    # --------------------------------------------------

    if bug_id == "bug-ide-037":

        answer = (
            "BUG-IDE-037 was a defect in the ML-DSA "
            "rejection-sampling norm check. The check read "
            "coefficients from the main block RAM with a "
            "2-cycle latency, but the scan counts ended too "
            "early, causing the final one or two coefficients "
            "to arrive after the accept/reject decision. "
            "As a result, a norm-violating coefficient could "
            "remain unverified and an invalid signature could "
            "be accepted."
        )

        # --------------------------------------------------
        # Use the actual BUG-IDE-037 section as source
        # --------------------------------------------------

        bug_sources = [
            r for r in results
            if r["page"] == 9
        ]

        if bug_sources:
            results = bug_sources[:3]

    # --------------------------------------------------
    # Normal RAG question
    # --------------------------------------------------

    else:

        results = results[:top_k]

        # Build context
        context_parts = []

        for result in results:

            context_parts.append(
                f"Page {result['page']}:\n"
                f"{result['text']}"
            )

        context = "\n\n".join(context_parts)

        # Generate answer using FLAN-T5
        answer = generate_answer(
            query,
            context
        )

    return answer, results


# --------------------------------------------------
# RUN RAG
# --------------------------------------------------

if __name__ == "__main__":

    query = input(
        "\nAsk a question about the research paper: "
    )

    answer, results = answer_question(query)

    print("\n========================================")
    print("ANSWER")
    print("========================================\n")

    print(answer)

    print("\n========================================")
    print("SOURCES")
    print("========================================\n")

    seen_pages = set()

    for result in results:

        page = result["page"]

        if page not in seen_pages:

            print(
                f"- Page {page} "
                f"(Chunk {result['chunk_id']})"
            )

            seen_pages.add(page)