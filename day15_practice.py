def score_niche(niche):
    score = 0
    reasons = []

    criteria = {
        "text_data": "есть много текстовых данных",
        "repeated_tasks": "есть повторяющиеся ручные задачи",
        "search_problem": "сотрудники часто ищут информацию",
        "time_cost": "ручная работа занимает много времени",
        "error_cost": "ошибка стоит денег",
    }

    for key, description in criteria.items():
        if niche.get(key):
            score += 1
            reasons.append(description)

    return score, reasons


def rank_niches(niches):
    ranked = []

    for niche in niches:
        score, reasons = score_niche(niche)
        ranked.append({
            "name": niche["name"],
            "score": score,
            "reasons": reasons,
        })

    return sorted(ranked, key=lambda item: item["score"], reverse=True)


def main():
    print("=== Практика День 15: Выбор ниши для AI/MVP ===")
    print("Задание: оценить несколько ниш и выбрать самую перспективную для первого AI-проекта.")

    niches = [
        {
            "name": "служба поддержки SaaS",
            "text_data": True,
            "repeated_tasks": True,
            "search_problem": True,
            "time_cost": True,
            "error_cost": True,
        },
        {
            "name": "локальная кофейня",
            "text_data": False,
            "repeated_tasks": True,
            "search_problem": False,
            "time_cost": False,
            "error_cost": False,
        },
        {
            "name": "HR-отдел средней компании",
            "text_data": True,
            "repeated_tasks": True,
            "search_problem": True,
            "time_cost": True,
            "error_cost": False,
        },
    ]

    ranked_niches = rank_niches(niches)

    print("\nРейтинг ниш:")
    for index, niche in enumerate(ranked_niches, start=1):
        print(f"{index}. {niche['name']} — {niche['score']}/5")
        for reason in niche["reasons"]:
            print(f"   - {reason}")

    best_niche = ranked_niches[0]
    print(f"\nЛучший кандидат для MVP: {best_niche['name']}")


if __name__ == "__main__":
    main()
