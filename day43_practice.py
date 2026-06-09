"""Практика День 43: приоритизатор каналов лидогенерации.

Деньги приносит активный поиск там, где покупатель уже собран, а не ожидание со
статей. Каналы различаются по объёму аудитории, теплоте контакта и стоимости входа.
Считаем приоритет каждого канала и раскладываем недельный план касаний. Чистая
стандартная библиотека.
"""


def channel_score(channel):
    """Оценка канала: тёплый и собранный пул при низкой цене входа важнее."""
    reach = channel["reach"]
    warmth = channel["warmth"]
    effort = channel["effort"]
    # Чем больше охват и теплота и чем меньше усилий, тем выше приоритет.
    return round(reach * warmth / effort, 2)


def rank_channels(channels):
    """Отсортировать каналы по убыванию приоритета."""
    scored = []
    for channel in channels:
        scored.append({**channel, "score": channel_score(channel)})
    return sorted(scored, key=lambda c: c["score"], reverse=True)


def split_touches(ranked, total):
    """Разложить недельные касания по каналам пропорционально приоритету."""
    sum_score = sum(c["score"] for c in ranked)
    plan = []
    for channel in ranked:
        share = channel["score"] / sum_score
        touches = max(1, round(total * share))
        plan.append({"name": channel["name"], "touches": touches})
    return plan


def main():
    print("=== Практика День 43: приоритизатор каналов лидогенерации ===")
    print("Задание: отранжировать каналы и разложить 25 касаний в неделю.")

    # reach — размер собранного пула, warmth — теплота контакта, effort — цена входа.
    channels = [
        {"name": "Партнёры-интеграторы", "reach": 9, "warmth": 7, "effort": 4},
        {"name": "Тёплый круг и рекомендации", "reach": 4, "warmth": 9, "effort": 2},
        {"name": "Отраслевые Telegram-чаты", "reach": 8, "warmth": 4, "effort": 3},
        {"name": "Биржи (Kwork, Профи.ру)", "reach": 6, "warmth": 3, "effort": 3},
        {"name": "Прямой выход в нишу", "reach": 7, "warmth": 2, "effort": 5},
        {"name": "Статьи и контент", "reach": 8, "warmth": 2, "effort": 6},
    ]

    ranked = rank_channels(channels)

    print("\nПриоритет каналов (выше — сначала):")
    for i, channel in enumerate(ranked, start=1):
        print(f"{i}. {channel['name']}: score {channel['score']}")

    plan = split_touches(ranked, total=25)

    print("\nНедельный план касаний (цель 25+):")
    for item in plan:
        print(f"- {item['name']}: {item['touches']}")

    print("\nВывод: контент внизу списка — он греет, но активный поиск там, где")
    print("покупатель уже собран, приносит сделку быстрее.")


if __name__ == "__main__":
    main()
