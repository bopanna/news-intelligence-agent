from config import MODEL_PROVIDER


def summarize_articles(articles):
    if MODEL_PROVIDER == "ollama":
        from .ollama_summary import summarize
    if MODEL_PROVIDER == "openai":
        from .openai_summary import summarize
    else:
        raise ValueError("Unsupported MODEL_PROVIDER")

    return summarize(articles)
