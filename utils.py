import tiktoken

from crawl4ai import AsyncWebCrawler
import asyncio

def truncate_markdown(markdown_text, max_tokens=8000, model="gpt-4o"):
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

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://www.nbcnews.com/business")
        markdown = result.markdown
        short_markdown = truncate_markdown(markdown, max_tokens=8000)
        print(short_markdown)

if __name__ == "__main__":
    asyncio.run(main())
