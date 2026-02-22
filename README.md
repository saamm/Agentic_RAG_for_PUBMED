# Agentic RAG for PubMed

An Explainable Agentic Retrieval-Augmented Generation System for Biomedical Knowledge Discovery

This project implements an open-source Agentic Retrieval-Augmented Generation (RAG) system for dynamically mining biomedical literature from PubMed, enabling explainable question answering for applications such as biomarker discovery and drug safety research.

## Features
- User biomedical query →
- PubMed search API →
- dynamic PMIDs →
- fetch abstracts →
- chunk →
- vectorstore →
- agentic RAG →
- answer + SHAP explanation

## Applications
- any biomedical topic
- real-time corpus construction
- reproducible science
- scalable literature mining
- research-style pipeline

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

## Next Steps
1. Add caching so PubMed is not re-downloaded every run
2. Add CLI interface: python main.py --query "cardiotoxicity biomarkers"

