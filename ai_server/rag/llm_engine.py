from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

MODEL_NAME = "gpt2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=80,
    do_sample=True,
    temperature=0.7,
    top_p=0.9
)

def generate_answer(context: str, question: str) -> str:
    prompt = (
        "You are a medical assistant.\n"
        "Answer the question clearly and briefly using the context.\n\n"
        f"Context: {context}\n"
        f"Question: {question}\n"
        "Answer:"
    )
    output = generator(prompt)
    text = output[0]["generated_text"]
    answer = text.split("Answer:")[-1].split("Question:")[0].strip()
    return answer