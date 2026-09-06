import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer


# --------------------------------------------------
# 1. Load embedding model
# --------------------------------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")


# --------------------------------------------------
# 2. Load FAISS index
# --------------------------------------------------

index = faiss.read_index(
    "vector_store/index.faiss"
)


# --------------------------------------------------
# 3. Load chunks
# --------------------------------------------------

with open(
    "vector_store/chunks.pkl",
    "rb"
) as file:

    chunks = pickle.load(file)


# --------------------------------------------------
# 4. Retrieve relevant chunks
# --------------------------------------------------

def retrieve(query, top_k=5):

    # Convert query into embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    # Normalize for cosine similarity
    faiss.normalize_L2(query_embedding)


    # --------------------------------------------------
    # Search ALL chunks
    # --------------------------------------------------

    scores, indices = index.search(
        query_embedding,
        index.ntotal
    )


    results = []

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
    # Build results
    # --------------------------------------------------

    for score, index_number in zip(
        scores[0],
        indices[0]
    ):

        chunk = chunks[index_number]

        text_lower = chunk["text"].lower()


        exact_match = False

        if bug_id:

            if bug_id in text_lower:

                exact_match = True


        results.append({

            "chunk_id": chunk["chunk_id"],

            "page": chunk["page"],

            "text": chunk["text"],

            "score": float(score),

            "exact_match": exact_match

        })


    # --------------------------------------------------
    # Prioritize exact BUG ID matches
    # --------------------------------------------------

    if bug_id:

        results.sort(

            key=lambda x: (
                x["exact_match"],
                x["score"]
            ),

            reverse=True

        )

    else:

        results.sort(

            key=lambda x: x["score"],

            reverse=True

        )


    # --------------------------------------------------
    # Return top results
    # --------------------------------------------------

    return results[:top_k]


# --------------------------------------------------
# 5. Test Retriever
# --------------------------------------------------

if __name__ == "__main__":

    query = input(
        "\nEnter your query: "
    )


    results = retrieve(
        query,
        top_k=5
    )


    print("\nRetrieved Chunks:")


    for result in results:

        print("\n" + "=" * 70)

        print(
            "Page:",
            result["page"]
        )

        print(
            "Chunk:",
            result["chunk_id"]
        )

        print(
            "Score:",
            result["score"]
        )

        print(
            "Exact BUG Match:",
            result["exact_match"]
        )

        print("=" * 70)

        print(result["text"])