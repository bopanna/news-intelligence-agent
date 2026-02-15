import json
import os
from datetime import datetime, timedelta

MEMORY_FILE = "storage/seen_titles.json"
TTL_HOURS = 24


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    # handle old list-based memory
    if isinstance(data, list):
        return {}

    return data


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)


def filter_seen_articles(articles):
    memory = load_memory()
    now = datetime.utcnow()

    new_articles = []

    for a in articles:
        title = a["title"]

        if title in memory:
            seen_time = datetime.fromisoformat(memory[title])
            if now - seen_time < timedelta(hours=TTL_HOURS):
                continue

        new_articles.append(a)
        memory[title] = now.isoformat()

    save_memory(memory)
    return new_articles
