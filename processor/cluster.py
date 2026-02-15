def cluster_articles(articles):
    clusters = {}
    clustered_articles = []

    for article in articles:
        key = article["title"].split()[0].lower()

        if key not in clusters:
            clusters[key] = article
            clustered_articles.append(article)

    return clustered_articles