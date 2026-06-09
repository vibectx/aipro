"""Практика День 38: покрытие демо на вопросах клиента.

Демо продаёт, когда показывает процент реальных вопросов, на которые бот отвечает.
Симулируем покрытие через сопоставление тем вопроса и тем базы знаний.
Чистая стандартная библиотека.
"""


def is_covered(question_tags, knowledge_tags):
    """Вопрос покрыт, если хотя бы одна его тема есть в базе знаний."""
    return bool(set(question_tags) & set(knowledge_tags))


def coverage_report(questions, knowledge_tags):
    """Какие вопросы покрыты, какие нет, и общий процент покрытия."""
    covered = []
    missed = []
    for question in questions:
        if is_covered(question["tags"], knowledge_tags):
            covered.append(question["text"])
        else:
            missed.append(question["text"])
    total = len(questions)
    percent = round(len(covered) / total * 100) if total else 0
    return {"covered": covered, "missed": missed, "percent": percent}


def main():
    print("=== Практика День 38: покрытие демо ===")
    print("Задание: посчитать, на какой процент вопросов клиента отвечает бот.")

    # Темы, которые есть в загруженной базе знаний клиента.
    knowledge_tags = ["доставка", "оплата", "возврат", "гарантия", "ассортимент"]

    questions = [
        {"text": "Сколько идёт доставка в регионы?", "tags": ["доставка"]},
        {"text": "Какие способы оплаты?", "tags": ["оплата"]},
        {"text": "Как оформить возврат товара?", "tags": ["возврат"]},
        {"text": "Есть ли гарантия на технику?", "tags": ["гарантия"]},
        {"text": "Работаете ли вы с юрлицами по договору?", "tags": ["договор"]},
        {"text": "Какой у вас график работы в праздники?", "tags": ["график"]},
    ]

    report = coverage_report(questions, knowledge_tags)

    print(f"\nПокрытие: {report['percent']}%")

    print("\nБот ответил (OK):")
    for text in report["covered"]:
        print(f"  OK   {text}")

    print("\nНе покрыто, в доработку на пилоте (FAIL):")
    for text in report["missed"]:
        print(f"  FAIL {text}")

    print(f"\nВывод для клиента: бот сразу закрывает {report['percent']}% реальных вопросов.")


if __name__ == "__main__":
    main()
