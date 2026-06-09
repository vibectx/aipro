"""Практика День 39: метрики пилота до и после.

Пилот продаёт внедрение, когда показывает дельту в цифрах клиента. Считаем
улучшение по ключевым метрикам до бота и после. Чистая стандартная библиотека.
"""


def improvement_percent(before, after, lower_is_better=True):
    """Процент улучшения метрики. Для времени меньше — лучше."""
    if before == 0:
        # Рост с нуля (например покрытие 0 -> 70) считаем в пунктах.
        return after if not lower_is_better else 0
    if lower_is_better:
        return round((before - after) / before * 100)
    return round((after - before) / before * 100)


def build_report(metrics):
    """Собрать отчёт по списку метрик с дельтой и процентом улучшения."""
    report = []
    for metric in metrics:
        percent = improvement_percent(metric["before"], metric["after"], metric["lower_is_better"])
        report.append({
            "name": metric["name"],
            "before": metric["before"],
            "after": metric["after"],
            "unit": metric["unit"],
            "improvement": percent,
        })
    return report


def main():
    print("=== Практика День 39: метрики пилота до и после ===")
    print("Задание: посчитать дельту по метрикам клиента за две недели пилота.")

    metrics = [
        {"name": "Время ответа", "before": 300, "after": 4, "unit": "сек", "lower_is_better": True},
        {"name": "Вопросов на людях в день", "before": 80, "after": 24, "unit": "шт", "lower_is_better": True},
        {"name": "Покрытие вопросов ботом", "before": 0, "after": 70, "unit": "%", "lower_is_better": False},
    ]

    report = build_report(metrics)

    print("\nМетрики пилота:")
    for item in report:
        if item["before"] == 0:
            print(f"  {item['name']}: было {item['before']} {item['unit']} — "
                  f"стало {item['after']} {item['unit']} (+{item['improvement']} пунктов)")
            continue
        sign = "лучше" if item["improvement"] >= 0 else "хуже"
        print(f"  {item['name']}: было {item['before']} {item['unit']} — "
              f"стало {item['after']} {item['unit']} ({abs(item['improvement'])}% {sign})")

    time_metric = report[0]
    print(f"\nВывод для клиента: ответ ускорился на {time_metric['improvement']}%, "
          f"нагрузка на людей снизилась — пилот доказал выгоду.")


if __name__ == "__main__":
    main()
