from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url(name: str) -> str:
    """
    This function takes a string as input and returns a LinkedIn profile URL.
    """
    # Initialize the TavilySearchResults tool
    search = TavilySearchResults()
    
    # Perform the search using the tool
    res = search.run(f"{name}")
    
    return res