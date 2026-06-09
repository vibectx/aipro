"""Практика День 40: RAG с порогом релевантности против выдумок.

Бот не должен врать. Ищем ближайший кусок базы знаний через ручной cosine на
Counter, и если релевантность ниже порога — честно отвечаем "нет в базе".
Чистая стандартная библиотека, без внешних API.
"""

import math
import re
from collections import Counter

THRESHOLD = 0.2  # минимальная релевантность, ниже которой бот не отвечает


def tokenize(text):
    """Разбить текст на слова в нижнем регистре."""
    return re.findall(r"[а-яёa-z0-9]+", text.lower())


def cosine(text_a, text_b):
    """Косинусная близость двух текстов через мешок слов."""
    vec_a = Counter(tokenize(text_a))
    vec_b = Counter(tokenize(text_b))
    common = set(vec_a) & set(vec_b)
    dot = sum(vec_a[word] * vec_b[word] for word in common)
    norm_a = math.sqrt(sum(value * value for value in vec_a.values()))
    norm_b = math.sqrt(sum(value * value for value in vec_b.values()))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def answer(question, knowledge_base):
    """Найти лучший документ и ответить, только если релевантность выше порога."""
    best_doc = None
    best_score = 0.0
    for doc in knowledge_base:
        score = cosine(question, doc["text"])
        if score > best_score:
            best_score = score
            best_doc = doc
    if best_doc is None or best_score < THRESHOLD:
        return {"ok": False, "text": "Нет в базе, передаю вопрос сотруднику.", "score": round(best_score, 2)}
    return {"ok": True, "text": best_doc["text"], "source": best_doc["source"], "score": round(best_score, 2)}


def main():
    print("=== Практика День 40: RAG с порогом релевантности ===")
    print("Задание: отвечать по базе и честно молчать, когда ответа нет.")

    knowledge_base = [
        {"text": "Доставка по России занимает от 3 до 7 рабочих дней.", "source": "Доставка.pdf"},
        {"text": "Возврат товара возможен в течение 14 дней с момента покупки.", "source": "Возврат.pdf"},
        {"text": "Оплата принимается картой, наличными и по счёту для юрлиц.", "source": "Оплата.pdf"},
    ]

    questions = [
        "Сколько дней идёт доставка?",
        "Можно ли оформить возврат товара?",
        "Какая у вас вакансия для программиста?",
    ]

    print("\nОтветы бота:")
    for question in questions:
        result = answer(question, knowledge_base)
        print(f"\n  Вопрос: {question}")
        if result["ok"]:
            print(f"  OK   ({result['score']}) {result['text']}")
            print(f"       источник: {result['source']}")
        else:
            print(f"  FAIL ({result['score']}) {result['text']}")


if __name__ == "__main__":
    main()
