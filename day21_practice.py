def build_outreach_message(niche, pain, result):
    return (
        f"Здравствуйте. Я помогаю компаниям в нише {niche} находить ручные процессы, "
        f"которые можно ускорить с помощью AI. Обычно начинаю с боли: {pain}. "
        f"Могу показать короткое демо, как получить результат: {result}."
    )


def build_commercial_plan(niche, offer, target_clients_count):
    return [
        f"Выбрать нишу: {niche}",
        f"Собрать список из {target_clients_count} потенциальных клиентов",
        f"Отправить короткий оффер: {offer}",
        "Провести 3-5 диагностических созвонов",
        "Выбрать одну повторяющуюся бизнес-боль",
        "Собрать прототип на примерах клиента",
        "Предложить платный пилот с измеримой метрикой",
    ]


def main():
    print("=== Практика День 21: План выхода к первому платному пилоту ===")
    print("Задание: собрать outreach-сообщение и план коммерческого захода.")

    niche = "SaaS-поддержка"
    pain = "операторы тратят много времени на первичный разбор тикетов"
    result = "тикеты быстрее получают категорию, summary и следующий шаг"

    message = build_outreach_message(niche, pain, result)
    plan = build_commercial_plan(
        niche=niche,
        offer="AI-аудит поддержки и быстрый прототип на реальных тикетах",
        target_clients_count=30,
    )

    print("\nСообщение для клиента:")
    print(message)

    print("\nПлан действий:")
    for index, step in enumerate(plan, start=1):
        print(f"{index}. {step}")


if __name__ == "__main__":
    main()
