import sys
import os

sys.path.insert(0, os.getcwd())


from collector.news_api import fetch_news
from collector.rss import fetch_rss
from summarizer.summarize import summarize_articles
from storage.writer import save_digest
from processor.ranker import rank_articles
from processor.dedupe import dedupe_articles
from storage.emailer import send_email
from storage.memory import filter_seen_articles
from processor.cluster import cluster_articles




def collect_all_news():
    all_news = []

    # India + global news
    all_news += fetch_news("in")

    # technology news
    all_news += fetch_news("us", "technology")

    # RSS sources (including Reddit RSS)
    all_news += fetch_rss()

    return all_news


if __name__ == "__main__":
    news = collect_all_news()
    news = dedupe_articles(news)
    news = rank_articles(news)
    news = filter_seen_articles(news)
    news = cluster_articles(news)

    TOP_N = 25
    news = news[:TOP_N]

    summary = summarize_articles(news)

    print("\n===== DAILY NEWS DIGEST =====\n")
    print(summary)

    save_digest(summary)

    send_email("Daily News Digest", summary)

