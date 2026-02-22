from pubmed_search import search_pubmed
from pubmed_loader import fetch_pubmed_articles
from chunker import chunk_text
from vector_store import VectorStore
from agent import AgenticRAG
from explainability import ExplainableRetriever

# Example biomedical queries
QUERIES = [
    "cardiotoxicity biomarkers",
    "drug induced cardiotoxicity",
    "chemotherapy heart adverse effects"
]

all_pmids = []

print("Searching PubMed dynamically...")
for q in QUERIES:
    pmids = search_pubmed(q, max_results=200)
    all_pmids.extend(pmids)

all_pmids = list(set(all_pmids))  # remove duplicates
print(f"Retrieved {len(all_pmids)} PubMed articles")

print("Fetching abstracts...")
df = fetch_pubmed_articles(all_pmids)

chunks = []
for text in df["text"]:
    if isinstance(text, str) and len(text) > 0:
        chunks.extend(chunk_text(text))

print(f"Total chunks created: {len(chunks)}")

vectorstore = VectorStore()
vectorstore.add_texts(chunks)

agent = AgenticRAG(vectorstore)
explainer = ExplainableRetriever()

while True:
    query = input("\nAsk biomedical question (or exit): ")
    if query.lower() == "exit":
        break

    answer = agent.run(query)
    print("\nAnswer:\n", answer)

    # Explain top retrieved chunks
    explainer.explain(query, chunks[:10])
