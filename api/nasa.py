import os
from dotenv import load_dotenv
import requests
from typing import Optional, Dict

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

def get_api_key():
    """Get NASA API key from environment, with fallback to DEMO_KEY."""
    return os.getenv("NASA_API_KEY") or "DEMO_KEY"

def make_api_request(url: str, params: dict, timeout: int = 10) -> Optional[Dict]:
    """
    Make an HTTP GET request to the specified URL with given parameters.
    
    Args:
        url (str): The URL to make the request to
        params (dict): Dictionary of parameters to include in the request
        timeout (int, optional): Request timeout in seconds. Defaults to 10.
    
    Returns:
        Optional[Dict]: JSON response as a dictionary if successful, None if failed
    
    Raises:
        Prints error message to console if request fails
    """
    try:
        response = requests.get(url, params=params, timeout=timeout)
        
        # Check if the response status code indicates success
        response.raise_for_status()
        
        # Try to parse JSON response
        return response.json()
        
    except requests.exceptions.Timeout:
        print(f"Request timeout after {timeout} seconds for URL: {url}")
        return None
    
    except requests.exceptions.ConnectionError:
        print(f"Connection error occurred for URL: {url}")
        return None
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error {response.status_code} for URL: {url} - {e}")
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"Request error for URL: {url} - {e}")
        return None
    
    except ValueError as e:
        print(f"JSON decode error for URL: {url} - Invalid JSON response: {e}")
        return None
    
    except Exception as e:
        print(f"Unexpected error for URL: {url} - {e}")
        return None

def get_nasa_apod(date: Optional[str] = None):
    """
    Retrieve NASA's Astronomy Picture of the Day (APOD).
    
    Args:
        api_key (str, optional): NASA API key. Defaults to NASA_API_KEY from environment.
        date (Optional[str], optional): Date in YYYY-MM-DD format for specific APOD.
                                       If None, returns today's APOD. Defaults to None.
    
    Returns:
        Optional[Dict]: Dictionary containing APOD data including title, explanation, 
                       image URL, and other metadata. Returns None if request fails.
    
    Example:
       apod = get_nasa_apod(date="2023-01-01")
       print(apod["title"])
    """
    # Build API URL and parameters
    base_url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": get_api_key(),
    }

    if date:
        #
        params["date"] = date

    return make_api_request(base_url, params, timeout=10)

def search_nasa_images(query: str,
                       size: int = 3) -> Optional[Dict]:
    """
    Search NASA's Image and Video Library for images matching the query.
    
    Args:
        query (str): Search term to look for in NASA's image library
        size (int, optional): Number of results to return (page size). Defaults to 3.
    
    Returns:
        Optional[Dict]: Dictionary containing search results with image metadata,
                       URLs, and descriptions. Returns None if request fails.
    
    Example:
        results = search_nasa_images("Mars rover", size=5)
        for item in results["collection"]["items"]:
        print(item["data"][0]["title"])
    """
    # NASA Image and Video Library API endpoint
    base_url = "https://images-api.nasa.gov/search"

    # Build parameters
    params = {
        "q": query,
        "media_type": "image",
        "page": 1,
        "page_size": size
    }

    return make_api_request(base_url, params, timeout=15)