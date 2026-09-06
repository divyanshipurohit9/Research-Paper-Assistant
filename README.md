# 📚 Research Paper Assistant

A **Retrieval-Augmented Generation (RAG)** based AI application that allows users to ask questions about a research paper and receive relevant, context-aware answers with **page-level source references**.

The system combines **Sentence Transformers, FAISS, and FLAN-T5** to retrieve relevant sections from a research paper and generate answers locally.

---

## 🚀 Features

* 📄 **Research Paper PDF Processing**

  * Extracts text from research papers.
  * Splits extracted content into smaller chunks for efficient retrieval.

* 🔎 **Semantic Search**

  * Converts text chunks into vector embeddings using Sentence Transformers.
  * Uses FAISS for fast similarity-based retrieval.

* 🤖 **RAG-based Question Answering**

  * Retrieves relevant passages based on the user's question.
  * Uses the retrieved context to generate an answer with FLAN-T5.

* 📖 **Source References**

  * Displays the page and chunk from which relevant information was retrieved.
  * Helps users verify answers against the original paper.

* 🖥️ **Interactive Streamlit Interface**

  * Simple web interface for asking questions.
  * Adjustable number of retrieved chunks.
  * Displays answers and retrieved sources.

* 🔐 **Local AI Inference**

  * Uses a locally loaded FLAN-T5 model for answer generation.

---

## 🧠 How It Works

```text
                Research Paper PDF
                       │
                       ▼
                PDF Text Extraction
                       │
                       ▼
                    Chunking
                       │
                       ▼
          Sentence Transformer Embeddings
                       │
                       ▼
                  FAISS Index
                       │
                       ▼
                  User Question
                       │
                       ▼
             Semantic Retrieval
                       │
                       ▼
              Relevant Paper Chunks
                       │
                       ▼
                   FLAN-T5
                       │
                       ▼
              Generated Answer
                       │
                       ▼
             Page + Chunk Sources
```

---

## 🛠️ Tech Stack

| Technology                    | Purpose                         |
| ----------------------------- | ------------------------------- |
| **Python**                    | Core programming language       |
| **Streamlit**                 | Web application interface       |
| **Sentence Transformers**     | Text embeddings                 |
| **FAISS**                     | Vector similarity search        |
| **FLAN-T5**                   | Local answer generation         |
| **PyMuPDF**                   | PDF text extraction             |
| **Hugging Face Transformers** | NLP model loading and inference |
| **NumPy**                     | Numerical operations            |
| **Pickle**                    | Storing processed data          |

---

## 📂 Project Structure

```text
Research-Paper-Assistant/
│
├── app.py
├── rag.py
├── retriever.py
├── generator.py
├── vector_store.py
├── chunker.py
├── pdf_loader.py
│
├── data/
│   └── research_paper.pdf
│
├── vector_store/
│   ├── index.faiss
│   └── chunks.pkl
│
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/divyanshipurohit9/Research-Paper-Assistant.git
```

### 2. Navigate to the project

```bash
cd Research-Paper-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 💡 Example Questions

Once the research paper is loaded, users can ask questions such as:

```text
What was BUG-IDE-037?
```

```text
What was the root cause of BUG-IDE-037?
```

```text
What was the fix implemented for the identified defect?
```

```text
Why were the existing KATs insufficient to detect the bug?
```

The application retrieves relevant sections from the paper and presents the answer along with the corresponding source pages.

---

## 📊 Vector Store

For the current research paper:

* **Embedding Model:** `all-MiniLM-L6-v2`
* **Embedding Dimension:** 384
* **Total Chunks:** 131
* **Vector Store:** FAISS

The FAISS index stores vector representations of the paper chunks and enables semantic retrieval based on the user's query.

---

## 🔄 RAG Pipeline

The application follows a standard Retrieval-Augmented Generation pipeline:

### 1. Document Loading

The research paper is loaded from a PDF using PyMuPDF.

### 2. Text Chunking

The extracted text is divided into smaller chunks so that relevant sections can be retrieved efficiently.

### 3. Embedding Generation

Each chunk is converted into a numerical vector using:

```text
all-MiniLM-L6-v2
```

### 4. Vector Storage

The embeddings are stored in a FAISS index.

### 5. Retrieval

When a user asks a question, the question is embedded and compared against the stored vectors.

The most relevant chunks are retrieved.

### 6. Generation

The retrieved context is provided to the FLAN-T5 model, which generates the final response.

### 7. Source Attribution

The application displays the relevant page and chunk information alongside the answer.

---

## 🎯 Why RAG?

Research papers can contain large amounts of technical information. Instead of passing the entire paper to a language model, RAG allows the system to:

* Retrieve only relevant information.
* Reduce unnecessary context.
* Improve answer relevance.
* Provide source references.
* Work with documents that are larger than a model's practical context window.

---

## 🔮 Future Improvements

* 📑 Support multiple research papers.
* 🔄 Allow users to upload their own PDFs.
* 💬 Add conversational chat history.
* 🧠 Improve retrieval using hybrid search.
* 📊 Add document and retrieval analytics.
* 🔗 Add citation-aware answer generation.
* ⚡ Optimize model inference speed.
* ☁️ Deploy the application online.

---

## 👩‍💻 Author

**Divyanshi Purohit**

B.Tech — Computer Science & Artificial Intelligence / Machine Learning

Graphic Era Hill University

---

## ⭐ Project Goal

The goal of this project is to demonstrate how **Retrieval-Augmented Generation (RAG)** can be used to build a practical AI application for understanding and querying technical research papers.

It combines **document processing, vector databases, semantic search, information retrieval, and local LLM-based generation** into a single application.
