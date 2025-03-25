import semanticscholar as sch
from semanticscholar import SemanticScholar, Author, Paper
from typing import List, Dict, Any

def initialize_client() -> SemanticScholar:
    """Initialize the SemanticScholar client."""
    return SemanticScholar()

def search_papers(client: SemanticScholar, query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Search for papers using a query string."""
    results = client.search_paper(query, limit=limit)
    return [
        {
            "paperId": paper.paperId,
            "title": paper.title,
            "abstract": paper.abstract,
            "year": paper.year,
            "authors": [{"name": author.name, "authorId": author.authorId} for author in paper.authors],
            "url": paper.url,
            "venue": paper.venue,
            "publicationTypes": paper.publicationTypes,
            "citationCount": paper.citationCount
        } for paper in results
    ]

def get_paper_details(client: SemanticScholar, paper_id: str) -> Paper:
    """Get details of a specific paper."""
    return client.get_paper(paper_id)

def get_author_details(client: SemanticScholar, author_id: str) -> Author:
    """Get details of a specific author."""
    return client.get_author(author_id)

def get_citations_and_references(paper: Paper) -> Dict[str, List[Dict[str, Any]]]:
    """Get citations and references for a paper."""
    return {
        "citations": paper.citations,
        "references": paper.references
    }

def main():
    try:
        # Initialize the client
        client = initialize_client()

        # Search for papers
        search_results = search_papers(client, "machine learning")
        print(f"Search results: {search_results[:2]}")  # Print first 2 results

        # Get paper details
        if search_results:
            paper_id = search_results[0]['paperId']
            paper = get_paper_details(client, paper_id)
            print(f"Paper details: {paper}")

            # Get citations and references
            citations_refs = get_citations_and_references(paper)
            print(f"Citations: {citations_refs['citations'][:2]}")  # Print first 2 citations
            print(f"References: {citations_refs['references'][:2]}")  # Print first 2 references

        # Get author details
        author_id = "1741101"  # Example author ID
        author = get_author_details(client, author_id)
        print(f"Author details: {author}")

    except sch.SemanticScholarException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
