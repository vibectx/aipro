def build_outreach_message(context, pain, idea, next_step):
    return (
        f"Здравствуйте, {context}. "
        f"Часто в таких командах встречается боль: {pain}. "
        f"Я собираю короткое AI-решение: {idea}. "
        f"Если интересно, {next_step}."
    )


def score_outreach(message):
    score = 0
    reasons = []

    checks = {
        "personal_context": ["видел", "заметил", "читал", "знаю", "понимаю"],
        "concrete_pain": ["время", "ручн", "ошиб", "тикет", "процесс"],
        "specific_idea": ["прототип", "демо", "ai", "автоматиз", "класс"],
        "small_next_step": ["15 минут", "короткое демо", "пример", "посмотреть"],
    }

    normalized = message.lower()

    for key, keywords in checks.items():
        if any(keyword in normalized for keyword in keywords):
            score += 1
            reasons.append(key)

    return score, reasons


def main():
    print("=== Практика День 24: Холодный outreach ===")
    print("Задание: собрать персонализированное сообщение и проверить его по чек-листу.")

    message = build_outreach_message(
        context="видел, что вы развиваете поддержку SaaS-продукта",
        pain="время первичного разбора тикета занимает 10-15 минут",
        idea="прототип классификации и summary для входящих тикетов",
        next_step="могу показать короткое демо на 15 минут на ваших примерах",
    )

    score, reasons = score_outreach(message)

    print("\nСообщение:")
    print(message)

    print(f"\nЧек-лист: {score}/4")
    print("Что есть в сообщении:")
    for reason in reasons:
        print(f"- {reason}")

    funnel = {
        "контакты": 30,
        "ответы": 10,
        "диалоги": 5,
        "созвоны": 3,
        "пилоты": 1,
    }

    print("\nОжидаемая воронка:")
    for stage, value in funnel.items():
        print(f"{stage}: {value}")


if __name__ == "__main__":
    main()
