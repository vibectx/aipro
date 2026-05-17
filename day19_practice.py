def calculate_metric_change(before, after):
    if before == 0:
        return 0

    return round((before - after) / before * 100, 1)


def build_pilot_plan(scenario, team, duration_days, success_metrics):
    return {
        "scenario": scenario,
        "team": team,
        "duration_days": duration_days,
        "success_metrics": success_metrics,
    }


def evaluate_pilot(before_metrics, after_metrics):
    result = {}

    for metric, before_value in before_metrics.items():
        after_value = after_metrics[metric]
        result[metric] = {
            "before": before_value,
            "after": after_value,
            "change_percent": calculate_metric_change(before_value, after_value),
        }

    return result


def main():
    print("=== Практика День 19: План и оценка AI-пилота ===")
    print("Задание: описать пилот и посчитать изменение ключевых метрик.")

    pilot = build_pilot_plan(
        scenario="AI помогает оператору разобрать входящий тикет",
        team="первая линия поддержки",
        duration_days=14,
        success_metrics=["время обработки", "ручные действия", "ошибки маршрутизации"],
    )

    before_metrics = {
        "processing_minutes": 12,
        "manual_actions": 6,
        "routing_errors": 10,
    }

    after_metrics = {
        "processing_minutes": 5,
        "manual_actions": 3,
        "routing_errors": 4,
    }

    evaluation = evaluate_pilot(before_metrics, after_metrics)

    print("\nПлан пилота:")
    for key, value in pilot.items():
        print(f"{key}: {value}")

    print("\nОценка результата:")
    for metric, values in evaluation.items():
        print(
            f"{metric}: {values['before']} → {values['after']} "
            f"({values['change_percent']}% улучшение)"
        )


if __name__ == "__main__":
    main()
