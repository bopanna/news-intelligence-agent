import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def summarize(articles):
    headlines = "\n".join([a["title"] for a in articles])

    prompt = f"""
Summarize today's news into:
- Top global developments
- India news
- Technology news
- One interesting story

Headlines:
{headlines}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
