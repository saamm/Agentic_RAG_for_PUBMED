import ollama
from config import TOP_K

class AgenticRAG:

    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def search(self, question):
        return self.vectorstore.search(question, TOP_K)

    def decide(self, retrieved_chunks):
        joined = "\n".join(retrieved_chunks)
        prompt = f"""
You are a biomedical research assistant.
Decide if the following evidence is sufficient to answer the question.

Evidence:
{joined}

Answer only YES or NO.
"""
        response = ollama.chat(model="mistral", messages=[{"role":"user","content":prompt}])
        return response["message"]["content"].strip()

    def answer(self, question, retrieved_chunks):
        context = "\n".join(retrieved_chunks)
        prompt = f"""
Answer the biomedical question using only the evidence below.

Evidence:
{context}

Question: {question}

Answer with scientific reasoning.
"""
        response = ollama.chat(model="mistral", messages=[{"role":"user","content":prompt}])
        return response["message"]["content"]

    def run(self, question):
        retrieved = self.search(question)
        decision = self.decide(retrieved)

        if decision == "YES":
            return self.answer(question, retrieved)
        else:
            return "Insufficient evidence found. Please refine query."
