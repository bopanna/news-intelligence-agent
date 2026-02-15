def dedupe_articles(articles):
    seen = set()
    unique = []

    for a in articles:
        title = a["title"].lower()

        if title not in seen:
            seen.add(title)
            unique.append(a)

    return unique
