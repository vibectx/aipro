def build_demo_case(before, after, manual_minutes, ai_seconds):
    saved_minutes = manual_minutes - ai_seconds / 60

    return {
        "before": before,
        "after": after,
        "manual_minutes": manual_minutes,
        "ai_seconds": ai_seconds,
        "saved_minutes": round(saved_minutes, 1),
    }


def build_demo_script(client_name, pain, case):
    return [
        f"Клиент: {client_name}",
        f"Боль: {pain}",
        f"Как сейчас: {case['before']}",
        f"Как с AI: {case['after']}",
        f"Время вручную: {case['manual_minutes']} минут",
        f"Время с AI: {case['ai_seconds']} секунд",
        f"Экономия на одном кейсе: {case['saved_minutes']} минут",
    ]


def main():
    print("=== Практика День 18: Демо AI/MVP для клиента ===")
    print("Задание: подготовить короткий сценарий демо, который показывает бизнес-результат.")

    case = build_demo_case(
        before="оператор вручную читает тикет, ищет контекст и пишет summary",
        after="AI сразу выдаёт категорию, summary и следующий шаг",
        manual_minutes=12,
        ai_seconds=20,
    )

    script = build_demo_script(
        client_name="SaaS-поддержка",
        pain="много времени уходит на первичный разбор тикетов",
        case=case,
    )

    print("\nСценарий демо:")
    for step in script:
        print(f"- {step}")


if __name__ == "__main__":
    main()
