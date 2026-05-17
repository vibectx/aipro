def calculate_monthly_savings(hours_saved_per_month, hourly_rate):
    return hours_saved_per_month * hourly_rate


def estimate_project_price(monthly_savings, payback_months=2):
    return monthly_savings * payback_months


def build_price_options(base_price):
    return {
        "audit": round(base_price * 0.2),
        "prototype": round(base_price * 0.5),
        "pilot": round(base_price),
        "implementation": round(base_price * 2),
    }


def main():
    print("=== Практика День 20: Экономика и цена AI/MVP ===")
    print("Задание: оценить экономию времени и собрать варианты цены.")

    hours_saved_per_month = 40
    hourly_rate = 2500

    monthly_savings = calculate_monthly_savings(hours_saved_per_month, hourly_rate)
    suggested_price = estimate_project_price(monthly_savings)
    price_options = build_price_options(suggested_price)

    print(f"\nЭкономия часов в месяц: {hours_saved_per_month}")
    print(f"Стоимость часа сотрудника: {hourly_rate} ₽")
    print(f"Оценка экономии в месяц: {monthly_savings} ₽")
    print(f"Ориентир цены проекта: {suggested_price} ₽")

    print("\nПакеты:")
    for package, price in price_options.items():
        print(f"{package}: {price} ₽")


if __name__ == "__main__":
    main()
