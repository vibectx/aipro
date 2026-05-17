def diagnose_process(process):
    findings = []

    if process["hours_per_week"] >= 5:
        findings.append("задача занимает много времени")

    if process["repeats_per_week"] >= 20:
        findings.append("задача часто повторяется")

    if process["uses_text_data"]:
        findings.append("есть текстовые данные для AI")

    if process["manual_routing"]:
        findings.append("есть ручная маршрутизация")

    if process["mistakes_are_expensive"]:
        findings.append("ошибки стоят денег")

    return findings


def build_ai_opportunity(process):
    findings = diagnose_process(process)

    if len(findings) >= 3:
        priority = "high"
    elif len(findings) >= 2:
        priority = "medium"
    else:
        priority = "low"

    return {
        "process": process["name"],
        "priority": priority,
        "findings": findings,
        "mvp": process["mvp"],
    }


def main():
    print("=== Практика День 16: Диагностика бизнес-боли ===")
    print("Задание: найти процесс, где AI может убрать ручную работу.")

    process = {
        "name": "первичный разбор заявок клиентов",
        "hours_per_week": 12,
        "repeats_per_week": 80,
        "uses_text_data": True,
        "manual_routing": True,
        "mistakes_are_expensive": True,
        "mvp": "классификация заявки, summary и следующий шаг для оператора",
    }

    opportunity = build_ai_opportunity(process)

    print(f"\nПроцесс: {opportunity['process']}")
    print(f"Приоритет: {opportunity['priority']}")

    print("\nНайденные сигналы боли:")
    for finding in opportunity["findings"]:
        print(f"- {finding}")

    print(f"\nИдея MVP: {opportunity['mvp']}")


if __name__ == "__main__":
    main()
