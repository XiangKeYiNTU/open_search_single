## Test
- Create conda environment and activate
```bash
conda create -n search-qa python==3.12
conda activate search-qa
```
- Clone the repository and enter the folder
```bash
git clone https://github.com/XiangKeYiNTU/open_search_single.git
cd open_search_single
```
- Install the required packages
```bash
pip install -r requirements.txt
```
- Copy `.env.example` file and rename it as `.env`
- Enter your openai api key, serpapi key, and jina api key in the `.env` file
```env
OPENAI_API_KEY="your_openai_api_key_here"
SERP_API_KEY="your_serp_api_key_here"
JINA_API_KEY="your_jina_api_key_here"
```
- Execute the `workflow.py` file with the following command:
```bash
python workflow.py <question> [image_path]
```
Enter your public image URL at the placeholder `[image_path]` if your question contains an image (optional)

- Or execute using the shell script `ask.sh`
```bash
chmod +x ask.sh
./ask.sh
```

---

## Example command and output

```bash
./ask.sh
```

```output
Enter your question: What city did the actor in this picture die in 2024?
Enter public image URL (or press Enter to skip): https://datasets-server.huggingface.co/cached-assets/CaraJ/MMSearch/--/f9616f150908dae99fc7fc6329e1af93b4854299/--/end2end/end2end/82/query_image/image.jpg?Expires=1751957602&Signature=OA7x2Q6mZsp73UQ23J1~bogNfCaWh-zO3v~YpD0oe7K039EVCtPwnlv7KLOe1xUxHZobmvd-Khq3oiFKqelKjfgIhsONmx6iZ0GvIsVlp-Kb~ENUty3f40xS2YBNoct5uiHZLIhGcF-LeSsSl53XZc6YHpPWanHdeoeIOgIREEoOR5bPCXPdj4Rpo9xNUysnmQi1lCVp2k7C0zKD4BvpwKvLEMKrrrRHMDgdAPE0l-Cb4zH-n1cpUwf~GJX1E4VShDUVyMmpt9tGh2f29-UpTrB26ZpGKAshFpeHC7J7iQTY7jRLI~i9~XKRDDY9gvcor9f4fXdE8sh8OMu1cKcgqA__&Key-Pair-Id=K3EI6M078Z3AC3
[*] Running question: What city did the actor in this picture die in 2024?
[*] With image: https://datasets-server.huggingface.co/cached-assets/CaraJ/MMSearch/--/f9616f150908dae99fc7fc6329e1af93b4854299/--/end2end/end2end/82/query_image/image.jpg?Expires=1751957602&Signature=OA7x2Q6mZsp73UQ23J1~bogNfCaWh-zO3v~YpD0oe7K039EVCtPwnlv7KLOe1xUxHZobmvd-Khq3oiFKqelKjfgIhsONmx6iZ0GvIsVlp-Kb~ENUty3f40xS2YBNoct5uiHZLIhGcF-LeSsSl53XZc6YHpPWanHdeoeIOgIREEoOR5bPCXPdj4Rpo9xNUysnmQi1lCVp2k7C0zKD4BvpwKvLEMKrrrRHMDgdAPE0l-Cb4zH-n1cpUwf~GJX1E4VShDUVyMmpt9tGh2f29-UpTrB26ZpGKAshFpeHC7J7iQTY7jRLI~i9~XKRDDY9gvcor9f4fXdE8sh8OMu1cKcgqA__&Key-Pair-Id=K3EI6M078Z3AC3
Response: {
  "rationale": "I cannot recognize people in images, so I need to conduct a search to identify the actor known for playing Zorro.",
  "knowledge_gap": "Identity of the actor known for playing Zorro.",
  "action": "text_search",
  "action_param": "Zorro actor 2024 death"
}
Response: {
  "rationale": "The search result indicates Alain Delon died in 2024. Since his death location is likely the home mentioned in the snippet, I should verify this information by visiting the linked article.",
  "knowledge_gap": "The exact city where Alain Delon died.",
  "action": "visit",
  "action_param": "https://global.chinadaily.com.cn/a/202408/18/WS66c1cf3aa31060630b923a44.html"
}
Response: {
  "rationale": "The article confirms that Alain Delon passed away in Douchy, France. I now have the information needed to answer the question.",
  "knowledge_gap": "None",
  "action": "answer",
  "action_param": "The actor in the picture, Alain Delon, died in the city of Douchy, France in 2024."
}
Final Answer: The actor in the picture, Alain Delon, died in the city of Douchy, France in 2024.
Search Count: 1
[✓] Workflow completed.
```
