"""Практика День 41: цена внедрения от выгоды клиента.

Цена не берётся с потолка. Считаем её от экономии клиента так, чтобы внедрение
окупалось в заданный срок, и добавляем подписку на поддержку.
Чистая стандартная библиотека.
"""


def recommended_price(savings_month, target_payback_months):
    """Цена внедрения под заданный срок окупаемости."""
    return round(savings_month * target_payback_months)


def support_price(savings_month, share=0.3):
    """Подписка на поддержку как доля от месячной экономии."""
    return round(savings_month * share)


def payback_months(price, support_month, savings_month):
    """Фактическая окупаемость с учётом подписки."""
    net = savings_month - support_month
    if net <= 0:
        return None
    return round(price / net, 1)


def main():
    print("=== Практика День 41: цена внедрения от выгоды ===")
    print("Задание: посчитать цену под окупаемость 3-6 месяцев и подписку.")

    savings_month = 61600  # экономия клиента в месяц из метрик пилота

    support = support_price(savings_month)

    print(f"\nЭкономия клиента в месяц: {savings_month} руб")
    print(f"Подписка на поддержку: {support} руб/мес")

    print("\nВарианты цены внедрения:")
    for target in (3, 4, 6):
        price = recommended_price(savings_month, target)
        fact = payback_months(price, support, savings_month)
        print(f"  окупаемость {target} мес → цена {price} руб → факт с подпиской {fact} мес")

    safe_price = recommended_price(savings_month, 3)
    print(f"\nРекомендация в КП: внедрение {safe_price} руб + поддержка {support} руб/мес.")
    print("Низкая окупаемость снимает возражение по цене.")


if __name__ == "__main__":
    main()
