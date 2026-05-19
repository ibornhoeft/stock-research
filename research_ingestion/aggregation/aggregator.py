from collections import defaultdict

def aggregate_documents(document_outputs):
    aggregate = {
        "entities": {},
        "sentiment_counts": defaultdict(lambda: {"positive": 0, "negative": 0, "cautious": 0}),
        "theme_counts": defaultdict(int),
        "mention_counts": defaultdict(int)
    }

    for doc in document_outputs:
        for entity in doc.entities:
            ticker = entity.ticker_candidates[0]

            aggregate["mention_counts"][ticker] += entity.mention_count

        for theme in doc.themes:
            aggregate["theme_counts"][theme] += 1

        for sec, sentiment in doc.sentiment.by_section.items():
            aggregate["sentiment_counts"][sec][sentiment] += 1

    return aggregate