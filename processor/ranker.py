from datetime import datetime, timezone

KEYWORDS = [
    "war", "military", "nuclear", "china", "russia", "us",
    "election", "government", "policy", "sanctions",
    "economy", "inflation", "bank", "trade",
    "ai", "technology", "cyber", "security", "chip",
    "india", "parliament", "supreme court",
    "climate", "energy", "space", "science"
]


SOURCE_WEIGHTS = {
    "BBC": 3,
    "Reuters": 3,
    "The Hindu": 3,
    "Indian Express": 2,
    "NDTV": 2,
    "rss": 1
}



def keyword_score(title):
    score = 0
    title = title.lower()

    for k in KEYWORDS:
        if k in title:
            score += 1

    return score


def recency_score(article):
    # placeholder until we store timestamps
    return 1


def source_score(article):
    return SOURCE_WEIGHTS.get(article.get("source", ""), 1)


def score_article(article):
    return (
        keyword_score(article["title"]) +
        recency_score(article) +
        source_score(article)
    )


def rank_articles(articles):
    return sorted(articles, key=score_article, reverse=True)
