import asyncio
import httpx

async def fetch_data(url, params=None, headers=None):
    """
    Async fetch JSON data from a URL.
    """
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            response = await client.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            print(f"Request error: {e}")
        except httpx.HTTPStatusError as e:
            print(f"HTTP error {e.response.status_code}: {e.response.text}")
        return None

async def main():
    url = "https://jsonplaceholder.typicode.com/posts"  # Example API
    headers = {"Accept": "application/json"}
    
    data = await fetch_data(url, headers=headers)
    
    if data:
        for item in data[:5]:
            print(item)

if __name__ == "__main__":
    asyncio.run(main())
