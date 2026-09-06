import streamlit as st

from rag import answer_question


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #777;
        margin-bottom: 30px;
    }

    .answer-box {
        padding: 20px;
        border-radius: 12px;
        background-color: #f5f5f5;
        margin-top: 15px;
        margin-bottom: 25px;
        line-height: 1.6;
    }

    .source-box {
        padding: 12px;
        border-radius: 8px;
        background-color: #fafafa;
        margin-bottom: 8px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    '<div class="main-title">📚 Research Paper Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Ask questions about a research paper using '
    'RAG + FAISS + FLAN-T5.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("⚙️ Settings")

    top_k = st.slider(
        "Retrieved chunks",
        min_value=1,
        max_value=5,
        value=3
    )

    st.markdown("---")

    st.write("### 🧠 Architecture")

    st.write(
        """
        **Research Paper**
        
        ↓
        
        **PDF Extraction**
        
        ↓
        
        **Chunking**
        
        ↓
        
        **Embeddings**
        
        ↓
        
        **FAISS**
        
        ↓
        
        **Retriever**
        
        ↓
        
        **FLAN-T5**
        
        ↓
        
        **Answer + Sources**
        """
    )


# --------------------------------------------------
# QUESTION INPUT
# --------------------------------------------------

query = st.text_input(
    "🔎 Ask a question",
    placeholder="Example: What was BUG-IDE-037 and what was its root cause?"
)


# --------------------------------------------------
# ASK BUTTON
# --------------------------------------------------

if st.button("Ask Question 🚀"):

    if not query.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Searching the research paper..."
        ):

            try:

                answer, results = answer_question(
                    query,
                    top_k=top_k
                )


                # --------------------------------------------------
                # ANSWER
                # --------------------------------------------------

                st.subheader("💡 Answer")

                st.markdown(
                    f"""
                    <div class="answer-box">
                    {answer}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                # --------------------------------------------------
                # SOURCES
                # --------------------------------------------------

                st.subheader("📖 Sources")

                seen_pages = set()

                for result in results:

                    page = result["page"]

                    chunk_id = result["chunk_id"]

                    score = result["score"]


                    if page not in seen_pages:

                        st.markdown(
                            f"""
                            <div class="source-box">

                            📄 <b>Page:</b> {page}

                            <br>

                            🔹 <b>Chunk:</b> {chunk_id}

                            <br>

                            🎯 <b>Similarity:</b> {score:.3f}

                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                        seen_pages.add(page)


            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )