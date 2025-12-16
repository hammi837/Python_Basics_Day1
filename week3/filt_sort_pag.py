import requests

def fetch_data(url, filters=None, sort=None, page=None, limit=None):
    params = {}
    
    # Add filtering params
    if filters:
        params.update(filters)
    
    # Add sorting params
    if sort:
        params.update(sort)
    
    # Add pagination params
    if page is not None:
        params['page'] = page
    if limit is not None:
        params['limit'] = limit
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/posts"
    
    filters = {"userId": 2}             
    sort = {"_sort": "id", "_order": "desc"}  # Sort by id descending
    page = 1
    limit = 5
    
    data = fetch_data(api_url, filters, sort, page, limit)
    print(data)
