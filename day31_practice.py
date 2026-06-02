def chunk_text(text, chunk_size=60, overlap=10):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end == len(text):
            break
        start = end - overlap
    return chunks


def tokenize(text):
    cleaned = text.lower()
    for ch in ",.!?;:":
        cleaned = cleaned.replace(ch, " ")
    return [token for token in cleaned.split() if token]


def score_chunk(query, chunk):
    query_tokens = set(tokenize(query))
    chunk_tokens = set(tokenize(chunk))
    if not query_tokens or not chunk_tokens:
        return 0.0
    intersection = query_tokens & chunk_tokens
    return round(len(intersection) / len(query_tokens), 3)


def build_index(documents, chunk_size=60, overlap=10):
    return {
        doc_id: chunk_text(text, chunk_size=chunk_size, overlap=overlap)
        for doc_id, text in documents.items()
    }


def retrieve(query, index, top_k=3):
    scored = []
    for doc_id, chunks in index.items():
        for chunk_id, chunk in enumerate(chunks):
            score = score_chunk(query, chunk)
            if score > 0:
                scored.append({
                    "doc": doc_id,
                    "chunk_id": chunk_id,
                    "score": score,
                    "text": chunk,
                })
    scored.sort(key=lambda item: -item["score"])
    return scored[:top_k]


def build_answer(query, retrieved):
    if not retrieved:
        return {"answer": "Ответ не найден в базе.", "sources": []}
    sources = [f"{item['doc']}#chunk-{item['chunk_id']}" for item in retrieved]
    snippets = " | ".join(item["text"] for item in retrieved)
    return {
        "answer": f"По запросу '{query}' найдены фрагменты: {snippets}",
        "sources": sources,
    }


def main():
    print("=== Практика День 31: RAG-пайплайн ===")
    print("Задание: разрезать документы, найти релевантные чанки и собрать ответ.")

    documents = {
        "regulation.md": (
            "Возврат денег за тариф Pro оформляется в течение 14 дней. "
            "Запрос подаётся через службу поддержки."
        ),
        "faq.md": (
            "Сменить тариф можно в личном кабинете. "
            "Понижение тарифа доступно в начале месяца."
        ),
        "billing.md": (
            "Счёт формируется первого числа каждого месяца. "
            "Если счёт не пришёл, обратитесь в поддержку."
        ),
    }

    index = build_index(documents, chunk_size=70, overlap=15)
    print(f"\nПроиндексировано документов: {len(index)}")
    for doc_id, chunks in index.items():
        print(f"- {doc_id}: {len(chunks)} чанков")

    query = "Как вернуть деньги за тариф?"
    print(f"\nЗапрос: {query}")

    retrieved = retrieve(query, index, top_k=2)
    print(f"\nНайдено фрагментов: {len(retrieved)}")
    for item in retrieved:
        print(f"- {item['doc']} chunk-{item['chunk_id']} score={item['score']}")

    answer = build_answer(query, retrieved)
    print(f"\nОтвет:\n{answer['answer']}")
    print(f"Источники: {answer['sources']}")


if __name__ == "__main__":
    main()
