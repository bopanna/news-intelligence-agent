# News Intelligence Agent

A daily automated news intelligence agent that collects, ranks, summarizes, and emails important global developments.

This project is designed both as a learning exercise in agent development and as a personal current-affairs briefing system.

---

## What the agent does

Twice daily, the agent:

1. Collects news from multiple sources
2. Deduplicates similar headlines
3. Ranks articles by importance
4. Filters previously-seen news (memory)
5. Clusters related topics
6. Summarizes developments using an LLM
7. Emails a digest

---

## Architecture

Collector → Processor → Summarizer → Storage → Email

### Collector
- RSS feeds (BBC, The Hindu, Reddit RSS)
- News API

### Processor
- Deduplication
- Ranking
- Me
