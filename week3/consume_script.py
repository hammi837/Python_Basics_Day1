import requests

def fetch_data(url, params=None, headers=None):
    """
    Fetch JSON data from a URL.
    """
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"  # Example API
    headers = {"Accept": "application/json"}
    
    data = fetch_data(url, headers=headers)
    
    if data:
        for item in data[:5]:  # Print first 5 results
            print(item)


