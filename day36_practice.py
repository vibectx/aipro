"""Практика День 36: экономика внедрения RAG-бота.

Чтобы продать бизнесу ИИ-бота, нужно посчитать его выгоду в часах и рублях.
Считаем экономию от того, что часть типовых вопросов закрывает бот, и срок
окупаемости внедрения. Чистая стандартная библиотека, без внешних вызовов.
"""


def current_cost_per_month(requests_per_day, minutes_per_request, hourly_rate_rub, work_days=22):
    """Сколько компания тратит в месяц на ручные ответы на типовые вопросы."""
    hours_per_day = requests_per_day * minutes_per_request / 60
    return round(hours_per_day * hourly_rate_rub * work_days)


def cost_with_bot(requests_per_day, minutes_per_request, hourly_rate_rub, deflection_rate, work_days=22):
    """Стоимость ручных ответов после внедрения: бот снимает часть вопросов."""
    remaining = requests_per_day * (1 - deflection_rate)
    hours_per_day = remaining * minutes_per_request / 60
    return round(hours_per_day * hourly_rate_rub * work_days)


def monthly_savings(before, after):
    """Экономия в рублях в месяц."""
    return before - after


def payback_months(implementation_cost, support_cost_month, savings_month):
    """Через сколько месяцев внедрение окупится с учётом подписки на поддержку."""
    net = savings_month - support_cost_month
    if net <= 0:
        return None
    return round(implementation_cost / net, 1)


def main():
    print("=== Практика День 36: экономика внедрения RAG-бота ===")
    print("Задание: посчитать выгоду клиента в часах и рублях и срок окупаемости.")

    # Профиль типового SMB-клиента.
    requests_per_day = 80        # типовых вопросов в день
    minutes_per_request = 6      # минут на ручной ответ
    hourly_rate_rub = 500        # стоимость часа сотрудника
    deflection_rate = 0.7        # доля вопросов, которые закрывает бот

    implementation_cost = 150000  # внедрение под ключ
    support_cost_month = 20000    # подписка на поддержку

    before = current_cost_per_month(requests_per_day, minutes_per_request, hourly_rate_rub)
    after = cost_with_bot(requests_per_day, minutes_per_request, hourly_rate_rub, deflection_rate)
    savings = monthly_savings(before, after)
    payback = payback_months(implementation_cost, support_cost_month, savings)

    saved_hours = round(requests_per_day * deflection_rate * minutes_per_request / 60 * 22, 1)

    print("\nПрофиль клиента:")
    print(f"  типовых вопросов в день: {requests_per_day}")
    print(f"  минут на ответ: {minutes_per_request}")
    print(f"  ставка сотрудника: {hourly_rate_rub} руб/час")
    print(f"  бот закрывает: {int(deflection_rate * 100)}% вопросов")

    print("\nЭкономика:")
    print(f"  было затрат в месяц: {before} руб")
    print(f"  стало затрат в месяц: {after} руб")
    print(f"  экономия в месяц: {savings} руб")
    print(f"  высвобождено часов в месяц: {saved_hours}")
    print(f"  подписка на поддержку: {support_cost_month} руб/мес")

    print("\nОкупаемость:")
    print(f"  внедрение под ключ: {implementation_cost} руб")
    if payback is None:
        print("  окупаемость: не окупается при текущих параметрах (FAIL)")
    else:
        print(f"  окупаемость: {payback} мес (OK)")

    print("\nВывод для КП:")
    print(f"  клиент экономит {savings} руб/мес и {saved_hours} часов,")
    print(f"  внедрение окупается за {payback} мес с учётом поддержки.")


if __name__ == "__main__":
    main()
