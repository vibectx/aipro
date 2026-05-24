def build_positioning(niche, role, result, proof):
    return (
        f"Я {role} для ниши {niche}. "
        f"Помогаю получать результат: {result}. "
        f"Доказательство: {proof}."
    )


def score_positioning(statement):
    score = 0
    reasons = []

    checks = {
        "niche": ["saas", "поддержк", "hr", "юрист", "школ", "ecommerce"],
        "role": ["ai", "консультант", "инженер", "практик"],
        "result": ["экономи", "ускор", "сокращ", "автоматиз", "качеств"],
        "proof": ["прототип", "пилот", "кейс", "метрик"],
    }

    normalized = statement.lower()

    for key, keywords in checks.items():
        if any(keyword in normalized for keyword in keywords):
            score += 1
            reasons.append(key)

    return score, reasons


def main():
    print("=== Практика День 22: Позиционирование AI-эксперта ===")
    print("Задание: собрать короткое позиционирование и проверить, что в нём есть все элементы.")

    statement = build_positioning(
        niche="SaaS-поддержка",
        role="AI-консультант",
        result="ускорение обработки тикетов и сокращение ручных действий",
        proof="прототип классификатора и пилот на 200 реальных тикетах",
    )

    score, reasons = score_positioning(statement)

    print("\nПозиционирование:")
    print(statement)

    print(f"\nОценка: {score}/4")
    print("Что присутствует:")
    for reason in reasons:
        print(f"- {reason}")


if __name__ == "__main__":
    main()
