import os
import time

from serpapi import GoogleSearch

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SERP_API_KEY")
# print(f"Using SERP API Key: {API_KEY}")
retry_attempt = 3

def get_text_search_results(query, num_results=5):
    params = {
        "engine": "google",
        "q": query,
        "api_key": API_KEY,
        "num": num_results,
    }
    for i in range(retry_attempt):
        try:
            search = GoogleSearch(params)
            # debug: 
            # print(search.get_dict())
            organic_results = search.get_dict().get("organic_results", [])
            if not organic_results:
                return (f"No results found for query: {query}")
            parsed_results = []
            for result in organic_results:
                parsed_result = {
                    "title": result.get("title"),
                    "link": result.get("link"),
                    "snippet": result.get("snippet"),
                    "displayed_link": result.get("displayed_link"),
                }
                parsed_results.append(parsed_result)
            return parsed_results
        except Exception as e:
            print(f"Attempt {i+1} failed: {e}")
            if i < retry_attempt - 1:
                time.sleep(2)
            else:
                print("All retries failed.")
                return ("Connection error to the search engine. Please try again later.")
            
def get_image_search_results(image_path, num_results=5):
    params = {
    "engine": "google_lens",
    "search_type": "all",
    "url": image_path,
    "api_key": API_KEY
    }

    for i in range(retry_attempt):
        try:
            search = GoogleSearch(params)
            organic_results = search.get_dict().get("visual_matches", [])
            if not organic_results:
                return (f"No results found for image: {image_path}")
            if len(organic_results) < num_results:
                return organic_results
            # Limit the number of results to num_results
            parsed_results = organic_results[:num_results]
            return parsed_results
        except Exception as e:
            print(f"Attempt {i+1} failed: {e}")
            if i < retry_attempt - 1:
                time.sleep(2)
            else:
                print("All retries failed.")
                return ("Connection error to the search engine. Please try again later.")


if __name__ == "__main__":
    # Example usage
    print("--- Text Search Results ---")
    query = "What is the capital of France?"
    print(get_text_search_results(query))

    print("\n--- Image Search Results ---")

    # For image search, you can provide a local image path or a URL
    image_path = "https://mitalinlp.oss-cn-hangzhou.aliyuncs.com/rallm/mm_data/vfreshqa_datasets_v2/Freshqa_en_zh/Freshqa_en_extracted_images/image_1.jpeg"  # Replace with your image URL or local path
    print(get_image_search_results(image_path))


# def search_text_by_text(text):
#     params = {
#         "engine": "google",
#         "q": text,
#         "api_key": API_KEY,
#         "num": 5,
#     }
#     for i in range(retry_attempt):
#         try:
#             search = GoogleSearch(params)
#             results = search.get_dict()
#             return results.get("organic_results", [])
#         except Exception as e:
#             print(f"Attempt {i+1} failed: {e}")
#             if i < retry_attempt - 1:
#                 time.sleep(2)
#             else:
#                 print("All retries failed.")
#                 return []


