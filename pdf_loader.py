import pymupdf


def load_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)

    pages = []

    for page_number, page in enumerate(doc):
        text = page.get_text()

        pages.append({
            "page": page_number + 1,
            "text": text
        })

    doc.close()

    return pages


if __name__ == "__main__":
    pages = load_pdf("data/research_paper.pdf")

    print("Total pages:", len(pages))

    print("\nFirst page:\n")
    print(pages[0]["text"][:2000])