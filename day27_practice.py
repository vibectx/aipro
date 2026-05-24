def build_weekly_report(done, in_progress, blocked, risks, next_step):
    return {
        "Сделано": done,
        "В работе": in_progress,
        "Заблокировано": blocked,
        "Риски": risks,
        "Следующий шаг": next_step,
    }


def classify_change_request(request):
    description = request.get("description", "").lower()
    effort_days = request.get("effort_days", 0)

    if effort_days <= 1 and "новый сценарий" not in description:
        return "включить в текущий этап"

    if effort_days <= 3:
        return "обсудить на ближайшем созвоне"

    return "оформить отдельным этапом"


def main():
    print("=== Практика День 27: Ведение AI-проекта ===")
    print("Задание: собрать недельный отчёт и обработать запросы на изменения.")

    report = build_weekly_report(
        done=["собрана выборка из 300 тикетов", "обучен базовый классификатор"],
        in_progress=["сборка summary-шага", "интеграция с архивом ответов"],
        blocked=["нет доступа к части закрытых тикетов"],
        risks=["качество классификации ниже целевого на 7%"],
        next_step="финализировать summary и подготовить промежуточное демо",
    )

    print("\nЕженедельный отчёт:")
    for key, value in report.items():
        print(f"{key}:")
        if isinstance(value, list):
            for item in value:
                print(f"  - {item}")
        else:
            print(f"  {value}")

    change_requests = [
        {"description": "поправить формат summary", "effort_days": 1},
        {"description": "добавить новый сценарий — анализ голосовых звонков", "effort_days": 7},
        {"description": "сделать дашборд по качеству", "effort_days": 3},
    ]

    print("\nЗапросы на изменения:")
    for request in change_requests:
        decision = classify_change_request(request)
        print(f"- {request['description']} ({request['effort_days']} дн.) → {decision}")


if __name__ == "__main__":
    main()
