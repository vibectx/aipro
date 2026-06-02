import math
from collections import Counter

VOCAB = [
    "счёт", "оплата", "тариф", "pro", "вернуть", "деньги", "возврат",
    "сменить", "переход", "понижение", "биллинг", "проблема",
    "ошибка", "доступ", "вход", "авторизация", "пароль", "кабинет",
]


def tokenize(text):
    cleaned = text.lower()
    for ch in ",.!?;:":
        cleaned = cleaned.replace(ch, " ")
    return [token for token in cleaned.split() if token]


def embed(text):
    counts = Counter(tokenize(text))
    vector = [float(counts.get(word, 0)) for word in VOCAB]
    norm = math.sqrt(sum(v * v for v in vector))
    if norm == 0:
        return vector
    return [v / norm for v in vector]


def cosine_similarity(a, b):
    return round(sum(x * y for x, y in zip(a, b)), 4)


class VectorIndex:
    def __init__(self):
        self.items = []

    def add(self, doc_id, text, metadata=None):
        self.items.append({
            "doc_id": doc_id,
            "text": text,
            "vector": embed(text),
            "metadata": metadata or {},
        })

    def search(self, query, top_k=3, filters=None):
        query_vec = embed(query)
        scored = []
        for item in self.items:
            if filters and not all(item["metadata"].get(k) == v for k, v in filters.items()):
                continue
            score = cosine_similarity(query_vec, item["vector"])
            if score > 0:
                scored.append({
                    "score": score,
                    "doc_id": item["doc_id"],
                    "text": item["text"],
                    "metadata": item["metadata"],
                })
        scored.sort(key=lambda hit: -hit["score"])
        return scored[:top_k]


def main():
    print("=== Практика День 32: Векторный поиск с метаданными ===")
    print("Задание: проиндексировать документы и найти похожие с фильтром по источнику.")

    index = VectorIndex()
    index.add("doc-1", "Возврат денег за тариф Pro оформляется через поддержку.", {"source": "regulation"})
    index.add("doc-2", "Сменить тариф можно в личном кабинете.", {"source": "faq"})
    index.add("doc-3", "Проблема с биллингом: счёт не пришёл вовремя.", {"source": "regulation"})
    index.add("doc-4", "Сброс пароля и восстановление доступа.", {"source": "auth"})

    print(f"\nПроиндексировано документов: {len(index.items)}")

    query = "хочу вернуть деньги за тариф"
    print(f"\nЗапрос: {query}")

    print("\nПоиск без фильтров:")
    for hit in index.search(query, top_k=3):
        print(f"- {hit['doc_id']} score={hit['score']} source={hit['metadata']['source']}")

    print("\nПоиск только в источнике regulation:")
    for hit in index.search(query, top_k=3, filters={"source": "regulation"}):
        print(f"- {hit['doc_id']} score={hit['score']}")


if __name__ == "__main__":
    main()
