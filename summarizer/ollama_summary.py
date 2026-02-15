import requests
from datetime import datetime

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def summarize(articles):
    text_blob = "\n".join([a["title"] for a in articles])
    today = datetime.now().strftime("%b %d, %Y")

    prompt = f"""
You are a global news intelligence analyst preparing a daily briefing.

Start the output with:
Daily News Digest — {today}

Write in a professional briefing style.

Only summarize what is directly supported by the headlines.
Avoid speculation.

From the headlines below:

1. Identify the 5 most important developments globally.
2. Summarize major global geopolitical trends.
3. Summarize key developments in India.
4. Summarize major technology developments.
5. Highlight one surprising or interesting story.

Headlines:
{text_blob}
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()["response"]
