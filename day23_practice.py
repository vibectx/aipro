def score_channel(channel):
    score = 0
    reasons = []

    criteria = {
        "has_decision_makers": "присутствуют ЛПР",
        "discuss_pain": "обсуждают рабочие задачи",
        "allow_personal_outreach": "можно написать в личку",
        "low_noise": "мало рекламы и спама",
        "matches_niche": "соответствует выбранной нише",
    }

    for key, description in criteria.items():
        if channel.get(key):
            score += 1
            reasons.append(description)

    return score, reasons


def rank_channels(channels):
    ranked = []

    for channel in channels:
        score, reasons = score_channel(channel)
        ranked.append({
            "name": channel["name"],
            "score": score,
            "reasons": reasons,
        })

    return sorted(ranked, key=lambda item: item["score"], reverse=True)


def main():
    print("=== Практика День 23: Где искать первых клиентов ===")
    print("Задание: оценить каналы поиска клиентов и выбрать топ-3 для outreach.")

    channels = [
        {
            "name": "профильный Telegram-чат SaaS-руководителей",
            "has_decision_makers": True,
            "discuss_pain": True,
            "allow_personal_outreach": True,
            "low_noise": True,
            "matches_niche": True,
        },
        {
            "name": "общий чат фрилансеров",
            "has_decision_makers": False,
            "discuss_pain": False,
            "allow_personal_outreach": True,
            "low_noise": False,
            "matches_niche": False,
        },
        {
            "name": "LinkedIn руководителей поддержки",
            "has_decision_makers": True,
            "discuss_pain": True,
            "allow_personal_outreach": True,
            "low_noise": True,
            "matches_niche": True,
        },
        {
            "name": "общий канал по AI без ниши",
            "has_decision_makers": False,
            "discuss_pain": False,
            "allow_personal_outreach": False,
            "low_noise": False,
            "matches_niche": False,
        },
    ]

    ranked = rank_channels(channels)

    print("\nРейтинг каналов:")
    for index, channel in enumerate(ranked, start=1):
        print(f"{index}. {channel['name']} — {channel['score']}/5")
        for reason in channel["reasons"]:
            print(f"   - {reason}")

    print("\nТоп-3 канала для outreach:")
    for channel in ranked[:3]:
        print(f"- {channel['name']}")


if __name__ == "__main__":
    main()
