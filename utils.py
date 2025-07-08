from dotenv import load_dotenv
import os
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
print(f"Using OpenRouter API Key: {OPENROUTER_API_KEY}")

from openai import OpenAI

import tiktoken

from crawl4ai import AsyncWebCrawler
import asyncio

def truncate_markdown(markdown_text, max_tokens=20000, model="gpt-4o"):
    """
    Truncates the markdown content to fit within a max token limit for a given GPT model.

    Parameters:
        markdown_text (str): Full markdown content to truncate.
        max_tokens (int): Maximum number of tokens allowed (default: 8000).
        model (str): The model name for tiktoken tokenizer (e.g., 'gpt-4o').

    Returns:
        str: Truncated markdown content.
    """
    # Load the appropriate tokenizer
    enc = tiktoken.encoding_for_model(model)

    # Tokenize the entire input
    tokens = enc.encode(markdown_text)

    if len(tokens) <= max_tokens:
        return markdown_text  # No truncation needed

    # Truncate and decode back to string
    truncated = enc.decode(tokens[:max_tokens])
    
    # Optionally: make a cleaner cut (e.g., end at paragraph or sentence)
    last_paragraph_end = truncated.rfind("\n\n")
    if last_paragraph_end != -1:
        truncated = truncated[:last_paragraph_end] + "\n\n*...(truncated)*"

    return truncated

def summarize_web_content_by_qwen(topic, web_content, openrouter_client):
    """
    Summarizes web content using Qwen model.

    Parameters:
        web_content (str): The content to summarize.
        openrouter_client: Optional client for OpenRouter API.

    Returns:
        str: Summary of the web content.
    """
    # Placeholder for Qwen summarization logic
    # This should be replaced with actual Qwen API call or logic

    summarize_prompt = f"""Summarize the webpage content relevant to the topic '{topic}'.
```web_content
{web_content}
```
"""
    response = openrouter_client.chat.completions.create(
        model="qwen/qwen3-235b-a22b:free",
        messages=[
            {"role": "system", "content": "You are a helpful assistant to summarize webpage content relevant to the given topic."},
            {"role": "user", "content": summarize_prompt}
        ],
        max_tokens=2000,  # Adjust as needed
    )
    # return response # debug
    return response.choices[0].message.content


async def main():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://www.amazon.sg")
        markdown = result.markdown
        short_markdown = truncate_markdown(markdown, max_tokens=20000)
        summary = summarize_web_content_by_qwen("cosmetics", short_markdown, client)
        print(summary)

if __name__ == "__main__":
    asyncio.run(main())
