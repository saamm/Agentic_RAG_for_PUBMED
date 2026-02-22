from Bio import Entrez
import pandas as pd

Entrez.email = "soumyasinha.ai@gmail.com" 

def fetch_pubmed_articles(pmids):
    records = []

    for pmid in pmids:
        handle = Entrez.efetch(db="pubmed", id=pmid, rettype="abstract", retmode="xml")
        data = Entrez.read(handle)

        article = data["PubmedArticle"][0]["MedlineCitation"]["Article"]
        title = article["ArticleTitle"]
        abstract = article["Abstract"]["AbstractText"][0] if "Abstract" in article else ""

        records.append({
            "pmid": pmid,
            "title": title,
            "text": abstract
        })

    return pd.DataFrame(records)
