from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_name = "mistralai/Mistral-7B-Instruct-v0.1"  # or use Ollama/Zephyr
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)
    prompt = f"""You are a helpful assistant. Answer based only on the below context.\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer:"""
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(inputs["input_ids"], max_new_tokens=256, do_sample=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
