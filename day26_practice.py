def build_proposal(pain, solution, stage, duration_weeks, success_metric, price, next_step):
    return {
        "Боль": pain,
        "Решение": solution,
        "Этап": stage,
        "Срок": f"{duration_weeks} недели",
        "Результат": success_metric,
        "Цена": f"{price} ₽",
        "Следующий шаг": next_step,
    }


def validate_proposal(proposal):
    required_fields = [
        "Боль",
        "Решение",
        "Этап",
        "Срок",
        "Результат",
        "Цена",
        "Следующий шаг",
    ]

    missing = [field for field in required_fields if not proposal.get(field)]

    return {
        "valid": not missing,
        "missing": missing,
    }


def main():
    print("=== Практика День 26: Коммерческое предложение ===")
    print("Задание: собрать короткое КП на один этап и проверить, что все блоки на месте.")

    proposal = build_proposal(
        pain="операторы тратят 10-15 минут на разбор каждого тикета",
        solution="AI-прототип классификации, summary и подсказки следующего шага",
        stage="AI-прототип",
        duration_weeks=3,
        success_metric="среднее время разбора тикета ↓ на 50% на пилотной выборке",
        price=180000,
        next_step="согласовать дату старта и состав данных для прототипа",
    )

    validation = validate_proposal(proposal)

    print("\nКоммерческое предложение:")
    for key, value in proposal.items():
        print(f"{key}: {value}")

    print("\nПроверка:")
    if validation["valid"]:
        print("Все блоки заполнены.")
    else:
        print("Не хватает блоков:")
        for field in validation["missing"]:
            print(f"- {field}")


if __name__ == "__main__":
    main()
