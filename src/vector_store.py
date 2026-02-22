import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from config import EMBED_MODEL

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer(EMBED_MODEL)
        self.index = faiss.IndexFlatL2(384)
        self.texts = []

    def add_texts(self, texts):
        embeddings = self.model.encode(texts)
        self.index.add(np.array(embeddings).astype("float32"))
        self.texts.extend(texts)

    def search(self, query, k=5):
        q_emb = self.model.encode([query])
        distances, indices = self.index.search(np.array(q_emb).astype("float32"), k)
        return [self.texts[i] for i in indices[0]]
