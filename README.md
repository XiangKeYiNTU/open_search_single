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

---

## Example command and output

```bash
python workflow.py "What is the best university in the country where Michelle Yeoh was born?"
```

```output
Response: {
  "rationale": "I need to find out the country where Michelle Yeoh was born.",
  "knowledge_gap": "Michelle Yeoh's country of birth.",
  "action": "text_search",
  "action_param": "Michelle Yeoh country of birth"
}
Response: {
  "rationale": "Michelle Yeoh was born in Malaysia. Now I need to identify the best university in Malaysia.",
  "knowledge_gap": "Best university in Malaysia.",
  "action": "text_search",
  "action_param": "best university in Malaysia 2025"
}
Response: {
  "rationale": "The search results suggest multiple sources that rank Malaysian universities. The University of Malaya is frequently mentioned as one of the top institutions.",
  "knowledge_gap": "Final confirmation of the best-ranked university in Malaysia for 2025.",
  "action": "visit",
  "action_param": "https://www.timeshighereducation.com/student/best-universities/best-universities-malaysia"
}
Response: {
  "rationale": "The University of Malaya is listed as one of the best universities in Malaysia for 2025 according to the Times Higher Education rankings.",
  "knowledge_gap": "None",
  "action": "answer",
  "action_param": "The best university in Malaysia, where Michelle Yeoh was born, is the University of Malaya according to the 2025 Times Higher Education rankings."
}
Final Answer: The best university in Malaysia, where Michelle Yeoh was born, is the University of Malaya according to the 2025 Times Higher Education rankings.
Search Count: 2
```
