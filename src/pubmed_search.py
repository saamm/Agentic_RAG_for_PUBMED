from Bio import Entrez

Entrez.email = "soumyasinha.ai@gmail.com"

def search_pubmed(query, max_results=500):
    """
    Search PubMed dynamically using a query string.
    Returns a list of PMIDs.
    """
    handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=max_results
    )
    results = Entrez.read(handle)
    return results["IdList"]
