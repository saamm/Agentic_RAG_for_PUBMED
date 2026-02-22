import shap
import numpy as np
from sentence_transformers import SentenceTransformer

class ExplainableRetriever:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def explain(self, query, documents):
        embeddings = self.model.encode(documents)
        query_emb = self.model.encode([query])

        def similarity(x):
            return np.dot(x, query_emb.T).flatten()

        explainer = shap.Explainer(similarity, embeddings)
        shap_values = explainer(embeddings)

        shap.summary_plot(shap_values, feature_names=[f"dim_{i}" for i in range(embeddings.shape[1])])
