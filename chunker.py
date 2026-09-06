from pdf_loader import load_pdf


def create_chunks(pages, chunk_size=800, overlap=150):
    chunks = []
    chunk_id = 0

    for page in pages:
        text = page["text"].strip()

        start = 0

        while start < len(text):
            end = start + chunk_size

            chunk_text = text[start:end]

            chunks.append({
                "chunk_id": chunk_id,
                "page": page["page"],
                "text": chunk_text
            })

            chunk_id += 1
            start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    pages = load_pdf("data/research_paper.pdf")

    chunks = create_chunks(pages)

    print("Total pages:", len(pages))
    print("Total chunks:", len(chunks))

    print("\nFirst chunk:\n")
    print(chunks[0]["text"])

    print("\n---")

    print("\nLast chunk:\n")
    print(chunks[-1]["text"])