def classify_request(text):
    normalized_text = text.lower()

    if "оплат" in normalized_text or "счёт" in normalized_text or "тариф" in normalized_text:
        return "billing"

    if "ошибка" in normalized_text or "не работает" in normalized_text or "сломалось" in normalized_text:
        return "technical"

    if "договор" in normalized_text or "документ" in normalized_text:
        return "documents"

    return "general"


def build_summary(text, max_length=90):
    if len(text) <= max_length:
        return text

    return text[:max_length].rstrip() + "..."


def suggest_next_step(category):
    steps = {
        "billing": "проверить оплату, тариф и статус счёта",
        "technical": "передать инженеру и запросить скриншот ошибки",
        "documents": "найти документ в базе знаний и приложить ссылку",
        "general": "уточнить детали запроса",
    }

    return steps[category]


def run_prototype(request_text):
    category = classify_request(request_text)

    return {
        "category": category,
        "summary": build_summary(request_text),
        "next_step": suggest_next_step(category),
    }


def main():
    print("=== Практика День 17: Быстрый AI-прототип ===")
    print("Задание: собрать прототип обработки клиентского запроса без внешних API.")

    request_text = "Клиент пишет, что после оплаты тарифа доступ к функциям всё ещё не открылся. Просит проверить счёт."
    result = run_prototype(request_text)

    print("\nВходящий запрос:")
    print(request_text)

    print("\nРезультат прототипа:")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
