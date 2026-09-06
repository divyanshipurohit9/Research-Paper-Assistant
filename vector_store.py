import faiss
import numpy as np
import pickle
import os

from pdf_loader import load_pdf
from chunker import create_chunks
from sentence_transformers import SentenceTransformer


# --------------------------------------------------
# 1. Load the embedding model
# --------------------------------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")


# --------------------------------------------------
# 2. Load PDF and create chunks
# --------------------------------------------------

pages = load_pdf("data/research_paper.pdf")

chunks = create_chunks(pages)

print("Total chunks:", len(chunks))


# --------------------------------------------------
# 3. Create embeddings
# --------------------------------------------------

texts = [chunk["text"] for chunk in chunks]

embeddings = model.encode(texts)


# --------------------------------------------------
# 4. Convert to float32
# --------------------------------------------------

embeddings = np.array(embeddings).astype("float32")


# --------------------------------------------------
# 5. Normalize embeddings
# --------------------------------------------------

faiss.normalize_L2(embeddings)


# --------------------------------------------------
# 6. Create FAISS index
# --------------------------------------------------

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)


# --------------------------------------------------
# 7. Add embeddings
# --------------------------------------------------

index.add(embeddings)


# --------------------------------------------------
# 8. Create vector_store folder
# --------------------------------------------------

os.makedirs("vector_store", exist_ok=True)


# --------------------------------------------------
# 9. Save FAISS index
# --------------------------------------------------

faiss.write_index(
    index,
    "vector_store/index.faiss"
)


# --------------------------------------------------
# 10. Save chunks
# --------------------------------------------------

with open("vector_store/chunks.pkl", "wb") as file:
    pickle.dump(chunks, file)


# --------------------------------------------------
# 11. Display information
# --------------------------------------------------

print("Number of vectors in FAISS:", index.ntotal)
print("Vector dimension:", dimension)
print("FAISS index saved successfully!")
print("Chunks saved successfully!")