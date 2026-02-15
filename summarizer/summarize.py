from config import MODEL_PROVIDER


def summarize_articles(articles):
    if MODEL_PROVIDER == "ollama":
        from .ollama_summary import summarize
    elif MODEL_PROVIDER == "groq":
        from .groq_summary import summarize
    elif MODEL_PROVIDER == "basic":
        from .basic_summary import summarize
    else:
        raise ValueError("Unsupported MODEL_PROVIDER")

    return summarize(articles)
