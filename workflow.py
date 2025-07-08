import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
import json

from prompts import system_prompt
from schemas import ResponseFormatter
from search_api import get_text_search_results, get_image_search_results
from visit_api import visit
from utils import truncate_markdown, summarize_web_content_by_qwen

# Load .env file
load_dotenv()

# Set API key from environment
# openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

qwen_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# get the question and image path from command line arguments
if len(sys.argv) < 2:
    print("Usage: python workflow.py <question> [image_path]")
    sys.exit(1)

question = sys.argv[1]
image_path = sys.argv[2] if len(sys.argv) > 2 else None

if image_path:
    question_content = [
        {
            "type": "input_text",
            "text": question
        },
        {
            "type": "input_image",
            "image_url": image_path
        }
    ]
else:
    question_content = question

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": question_content}
]

# response_format = {
#     "name": "format_response",
#     "description": "Format the response to the user with rationale, knowledge gap, action, and action parameter.",
#     "parameters": ResponseFormatter.model_json_schema()
# }

answer = None
search_count = 0

while not answer:
    response = client.responses.parse(
        model="gpt-4o-2024-08-06",
        input=messages,
        text_format=ResponseFormatter,
    )

    # print("Response:", response)

    # messages.append({
    #     "role": "assistant",
    #     "content": response
    # })

    step = response.output_parsed

    response_content = json.dumps(step.model_dump(), indent=2)

    print("Response:", response_content)

    messages.append({
        "role": "assistant",
        "content": response_content
    })

    if step.action == "text_search":
        search_count += 1
        if search_count > 5:
            user_message = {
                "role": "user",
                "content": "Search quota reached. Please provide a final answer."
            }
            messages.append(user_message)
            continue
        else:
            search_results = get_text_search_results(step.action_param)
            result_string = json.dumps(search_results, indent=2)
            messages.append({
                "role": "user",
                "content": "```search_results\n" + result_string + "\n```"
            })
            continue
    elif step.action == "image_search":
        search_count += 1
        if search_count > 5:
            user_message = {
                "role": "user",
                "content": "Search quota reached. Please provide a final answer."
            }
            messages.append(user_message)
            continue
        else:
            if step.action_param == "IMAGE":
                image_path = image_path
            else:
                image_path = step.action_param
            search_results = get_image_search_results(image_path)
            result_string = json.dumps(search_results, indent=2)
            messages.append({
                "role": "user",
                "content": "```search_results\n" + result_string + "\n```"
            })
            continue
    elif step.action == "visit":
        raw_content = visit(step.action_param)
        short_content = truncate_markdown(raw_content, max_tokens=20000)
        web_summary = summarize_web_content_by_qwen(
            step.knowledge_gap, short_content, qwen_client
        )
        messages.append({
            "role": "user",
            "content": "Here's a summary of the requested website:\n```web_content\n" + str(web_summary) + "\n```"
        })
        continue
    elif step.action == "answer":
        answer = step.action_param
    else:
        messages.append({
            "role": "user",
            "content": "Invalid action. Please provide a valid action."
        })

print("Final Answer:", answer)
print("Search Count:", search_count)