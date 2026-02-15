import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def summarize(articles):
    headlines = "\n".join([a["title"] for a in articles])

    prompt = f"""
You are generating a factual news intelligence briefing.

Rules:
- Use only the provided headlines
- Do not infer missing facts
- Do not fabricate details
- Keep summaries concise

Group into:
- Global
- India
- Technology
- Interesting

Headlines:
{headlines}
"""


    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
