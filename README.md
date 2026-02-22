# Agentic RAG for PubMed

This project implements an Agentic Retrieval-Augmented Generation (RAG) system for biomedical literature mining.

## Features
- PubMed retrieval
- Vector search using FAISS
- Local LLM reasoning (Mistral)
- Agentic loop (search → retrieve → decide → answer)
- Explainability using SHAP

## Applications
- Biomarker discovery
- Cardiotoxicity monitoring
- Drug safety research

## Stack
- Python
- Ollama
- FAISS
- SentenceTransformers
- SHAP

## Setup

1. Install Ollama and pull Mistral:
```bash
ollama pull mistral
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run:
```
python src/main.py
```


