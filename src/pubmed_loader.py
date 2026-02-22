from Bio import Entrez
import pandas as pd
from tqdm import tqdm

Entrez.email = "soumyasinha.ai@gmail.com"

def fetch_pubmed_articles(pmids):
    records = []

    for pmid in tqdm(pmids):
        try:
            handle = Entrez.efetch(
                db="pubmed",
                id=pmid,
                rettype="abstract",
                retmode="xml"
            )
            data = Entrez.read(handle)

            article = data["PubmedArticle"][0]["MedlineCitation"]["Article"]
            title = article.get("ArticleTitle", "")

            abstract = ""
            if "Abstract" in article:
                abstract = " ".join(article["Abstract"]["AbstractText"])

            records.append({
                "pmid": pmid,
                "title": title,
                "text": abstract
            })

        except Exception as e:
            print(f"Skipping PMID {pmid}: {e}")

    return pd.DataFrame(records)
