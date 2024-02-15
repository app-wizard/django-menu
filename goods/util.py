from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from goods.models import Products


def q_search(query):
    """
    Perform a search in the Products table based on the given query.

    If the query is a digit and its length is less than or equal to 5,
    search for products with matching IDs. Otherwise, perform a full-text
    search on the 'name' and 'description' fields and return the results
    ordered by their relevance.

    Args:
        query (str): The search query.

    Returns:
        QuerySet: A queryset containing the search results.
    """
    if query.isdigit() and len(query) <= 5:
        # Search for products by ID if the query is a digit and its length is <= 5
        return Products.objects.filter(id=int(query))

    # Perform full-text search on 'name' and 'description' fields
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    # Annotate search results with rank based on relevance
    # Filter results with rank > 0 (meaning they match the search query)
    # Order results by rank in descending order (higher rank = more relevant)
    return (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
