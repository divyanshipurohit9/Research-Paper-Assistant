from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# --------------------------------------------------
# 1. Load FLAN-T5
# --------------------------------------------------

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME
)


# --------------------------------------------------
# 2. Generate Answer
# --------------------------------------------------

def generate_answer(query, context):

    prompt = f"""
You are a research paper question-answering system.

Answer the question using ONLY the information in the research paper context.

Do NOT copy section headings.
Do NOT copy table headings.
Do NOT simply repeat the context.
Do NOT answer about another BUG.
Give the actual factual answer to the question.

Question:
{query}

Research paper context:
{context}

Instructions:
- Identify the specific BUG mentioned in the question.
- If the question asks for the root cause, explain the technical cause.
- If the question asks what the bug was, explain what went wrong.
- Ignore unrelated BUGs.
- Answer in 2-4 complete sentences.

Answer:
"""

    # Tokenize prompt
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=768,
        truncation=True
    )


    # Generate
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=False,
        num_beams=4,
        early_stopping=True
    )


    # Decode
    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )


    return answer.strip()


# --------------------------------------------------
# 3. Test Generator
# --------------------------------------------------

if __name__ == "__main__":

    query = "What was BUG-IDE-037 and what was its root cause?"

    context = """
    D. BUG-IDE-037: The Methodology's Key Catch

    Detection and symptom. A later seed-driven randomized
    mixed-operation soak caught a verification-failing signature
    for one message class.

    Root cause. In dilithium_sign.v, the rejection-sampling norm
    check reads coefficients from the main BRAM with 2-cycle
    latency, but the scan counts covered exactly the polynomial.
    Therefore, the last one or two coefficients arrived after the
    accept/reject decision.

    The fix extended each scan by the BRAM latency margin.
    """

    answer = generate_answer(
        query,
        context
    )

    print("\nQuestion:")
    print(query)

    print("\nAnswer:")
    print(answer)