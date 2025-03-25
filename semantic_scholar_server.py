from typing import Any, List, Dict
import asyncio
import logging
from mcp.server.fastmcp import FastMCP
from semantic_scholar_search import initialize_client, search_papers, get_paper_details, get_author_details, get_citations_and_references

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize FastMCP server
mcp = FastMCP("semanticscholar")

# Initialize SemanticScholar client
client = initialize_client()

@mcp.tool()
async def search_semantic_scholar(query: str, num_results: int = 10) -> List[Dict[str, Any]]:
    logging.info(f"Searching for papers with query: {query}, num_results: {num_results}")
    """
    Search for papers on Semantic Scholar using a query string.

    Args:
        query: Search query string
        num_results: Number of results to return (default: 10)

    Returns:
        List of dictionaries containing paper information
    """
    try:
        results = await asyncio.to_thread(search_papers, client, query, num_results)
        return results
    except Exception as e:
        return [{"error": f"An error occurred while searching: {str(e)}"}]

@mcp.tool()
async def get_semantic_scholar_paper_details(paper_id: str) -> Dict[str, Any]:
    logging.info(f"Fetching paper details for paper ID: {paper_id}")
    """
    Get details of a specific paper on Semantic Scholar.

    Args:
        paper_id: ID of the paper

    Returns:
        Dictionary containing paper details
    """
    try:
        paper = await asyncio.to_thread(get_paper_details, client, paper_id)
        return {
            "paperId": paper.paperId,
            "title": paper.title,
            "abstract": paper.abstract,
            "year": paper.year,
            "authors": [{"name": author.name, "authorId": author.authorId} for author in paper.authors],
            "url": paper.url,
            "venue": paper.venue,
            "publicationTypes": paper.publicationTypes,
            "citationCount": paper.citationCount
        }
    except Exception as e:
        return {"error": f"An error occurred while fetching paper details: {str(e)}"}

@mcp.tool()
async def get_semantic_scholar_author_details(author_id: str) -> Dict[str, Any]:
    logging.info(f"Fetching author details for author ID: {author_id}")
    """
    Get details of a specific author on Semantic Scholar.

    Args:
        author_id: ID of the author

    Returns:
        Dictionary containing author details
    """
    try:
        author = await asyncio.to_thread(get_author_details, client, author_id)
        return {
            "authorId": author.authorId,
            "name": author.name,
            "url": author.url,
            "affiliations": author.affiliations,
            "paperCount": author.paperCount,
            "citationCount": author.citationCount,
            "hIndex": author.hIndex
        }
    except Exception as e:
        return {"error": f"An error occurred while fetching author details: {str(e)}"}

@mcp.tool()
async def get_semantic_scholar_citations_and_references(paper_id: str) -> Dict[str, List[Dict[str, Any]]]:
    logging.info(f"Fetching citations and references for paper ID: {paper_id}")
    """
    Get citations and references for a specific paper on Semantic Scholar.

    Args:
        paper_id: ID of the paper

    Returns:
        Dictionary containing lists of citations and references
    """
    try:
        paper = await asyncio.to_thread(get_paper_details, client, paper_id)
        citations_refs = await asyncio.to_thread(get_citations_and_references, paper)
        return {
            "citations": [
                {
                    "paperId": citation.paperId,
                    "title": citation.title,
                    "year": citation.year,
                    "authors": [{"name": author.name, "authorId": author.authorId} for author in citation.authors]
                } for citation in citations_refs["citations"]
            ],
            "references": [
                {
                    "paperId": reference.paperId,
                    "title": reference.title,
                    "year": reference.year,
                    "authors": [{"name": author.name, "authorId": author.authorId} for author in reference.authors]
                } for reference in citations_refs["references"]
            ]
        }
    except Exception as e:
        return {"error": f"An error occurred while fetching citations and references: {str(e)}"}

if __name__ == "__main__":
    logging.info("Starting Semantic Scholar MCP server")
    # Initialize and run the server
    mcp.run(transport='stdio')
