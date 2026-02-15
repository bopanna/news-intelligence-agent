import feedparser

RSS_FEEDS = [
    # Global
    "http://feeds.bbci.co.uk/news/world/rss.xml",
    "http://feeds.reuters.com/Reuters/worldNews",
    "https://www.aljazeera.com/xml/rss/all.xml",

    # India
    "https://www.thehindu.com/news/national/feeder/default.rss",
    "https://indianexpress.com/section/india/feed/",
    "https://feeds.feedburner.com/ndtvnews-india-news",

    # Technology
    "https://techcrunch.com/feed/",
    "https://feeds.arstechnica.com/arstechnica/index",
    "https://news.ycombinator.com/rss",

    # Reddit RSS
    "https://www.reddit.com/r/worldnews/.rss",
    "https://www.reddit.com/r/technology/.rss",
]



def fetch_rss():
    articles = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            articles.append({
                "title": entry.title,
                "url": entry.link,
                "source": "rss"
            })

    return articles
