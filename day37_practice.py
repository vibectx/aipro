"""Практика День 37: квалификация лидов под RAG-бота.

Не каждый контакт — клиент. Считаем балл лида по признакам силы и сортируем
список, чтобы работать сначала с лучшими. Чистая стандартная библиотека.
"""

# Признаки сильного лида и их вес в баллах (сумма = 100).
CRITERIA = {
    "has_documents": 25,    # есть база документов, регламентов, прайсов
    "repetitive_pain": 25,  # сотрудники отвечают на одни и те же вопросы
    "warm_contact": 20,     # контакт тёплый, не с улицы
    "has_budget": 15,       # есть деньги на внедрение
    "decision_maker": 15,   # есть выход на ЛПР
}


def score_lead(lead):
    """Сумма баллов по выполненным признакам."""
    return sum(weight for key, weight in CRITERIA.items() if lead.get(key))


def label(score):
    """Температура лида по баллу."""
    if score >= 70:
        return "HOT"
    if score >= 40:
        return "WARM"
    return "COLD"


def rank_leads(leads):
    """Отсортировать лиды от лучшего к худшему."""
    scored = [{"name": lead["name"], "score": score_lead(lead), "label": label(score_lead(lead))} for lead in leads]
    return sorted(scored, key=lambda item: item["score"], reverse=True)


def main():
    print("=== Практика День 37: квалификация лидов ===")
    print("Задание: оценить лиды по признакам и отсортировать по приоритету.")

    leads = [
        {"name": "Турагентство (знакомый)", "has_documents": True, "repetitive_pain": True,
         "warm_contact": True, "has_budget": True, "decision_maker": True},
        {"name": "Автосервис по рекомендации", "has_documents": True, "repetitive_pain": True,
         "warm_contact": True, "has_budget": False, "decision_maker": False},
        {"name": "Холодный завод из интернета", "has_documents": False, "repetitive_pain": False,
         "warm_contact": False, "has_budget": True, "decision_maker": False},
        {"name": "Юрфирма бывшего коллеги", "has_documents": True, "repetitive_pain": True,
         "warm_contact": True, "has_budget": True, "decision_maker": False},
    ]

    ranked = rank_leads(leads)

    print("\nПриоритет лидов:")
    for index, item in enumerate(ranked, start=1):
        print(f"  {index}. [{item['label']}] {item['score']:>3} баллов — {item['name']}")

    best = ranked[0]
    print(f"\nБрать в работу первым: {best['name']} ({best['score']} баллов, {best['label']})")


if __name__ == "__main__":
    main()
