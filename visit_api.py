import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("JINA_API_KEY")

def visit(url: str):
    request_url = "https://r.jina.ai/" + url
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(request_url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return f"Website Visit Error: {response.status_code}"
    
if __name__ == "__main__":
    # Example usage
    url = "https://www.amazon.sg/"
    result = visit(url)
    print(result)