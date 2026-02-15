import requests
from config import NEWS_API_KEY

BASE_URL = "https://newsapi.org/v2/top-headlines"


def fetch_news(country="us", category=None):
    params = {
        "apiKey": NEWS_API_KEY,
        "country": country,
        "pageSize": 10
    }

    if category:
        params["category"] = category

    r = requests.get(BASE_URL, params=params)
    data = r.json()

    return [
        {
            "title": a["title"],
            "url": a["url"],
            "source": a["source"]["name"]
        }
        for a in data["articles"]
    ]
