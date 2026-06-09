"""Практика День 42: генератор кейса из метрик пилота.

Закрытый пилот нужно превратить в кейс, который продаёт следующих клиентов.
Собираем текст кейса из метрик до/после, срока и отзыва. Чистая стандартная
библиотека.
"""


def format_metric(metric):
    """Строка одной метрики в формате было — стало."""
    return f"- {metric['name']}: было {metric['before']} {metric['unit']} — стало {metric['after']} {metric['unit']}"


def build_case(data):
    """Собрать готовый текст кейса из данных пилота."""
    lines = []
    lines.append(f"Кейс: {data['industry']}")
    lines.append("")
    lines.append("Было:")
    lines.append(f"- сотрудники отвечали на типовые вопросы вручную;")
    lines.append(f"- ответ занимал до {data['metrics'][0]['before']} {data['metrics'][0]['unit']}.")
    lines.append("")
    lines.append("Стало:")
    for metric in data["metrics"]:
        lines.append(format_metric(metric))
    lines.append("")
    lines.append(f"Срок внедрения: {data['days']} дней.")
    lines.append(f"Стек: {data['stack']}.")
    lines.append(f"Отзыв клиента: \"{data['review']}\"")
    return "\n".join(lines)


def main():
    print("=== Практика День 42: генератор кейса из метрик ===")
    print("Задание: собрать текст кейса из результатов пилота.")

    data = {
        "industry": "Интернет-магазин техники",
        "metrics": [
            {"name": "Время ответа", "before": 300, "after": 4, "unit": "сек"},
            {"name": "Вопросов на людях в день", "before": 80, "after": 24, "unit": "шт"},
            {"name": "Покрытие вопросов ботом", "before": 0, "after": 70, "unit": "%"},
        ],
        "days": 14,
        "stack": "YandexGPT, RAG на pgvector, Telegram",
        "review": "Менеджеры перестали тонуть в одинаковых вопросах, клиенты получают ответ сразу.",
    }

    case_text = build_case(data)

    print("\n" + case_text)
    print("\nКуда идёт кейс: пост в канал и слайд-доказательство в КП следующему клиенту.")


if __name__ == "__main__":
    main()
