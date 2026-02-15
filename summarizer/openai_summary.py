from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize(articles):
    headlines = "\n".join([a["title"] for a in articles])

    prompt = f"Summarize today's news:\n{headlines}"

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
