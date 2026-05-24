def build_weekly_plan(outreach_per_day, calls_per_week, posts_per_week):
    return {
        "outreach_messages_per_week": outreach_per_day * 5,
        "discovery_calls_per_week": calls_per_week,
        "content_posts_per_week": posts_per_week,
    }


def project_monthly_funnel(weekly_plan, response_rate, call_rate, proposal_rate, deal_rate):
    weekly_messages = weekly_plan["outreach_messages_per_week"]

    monthly_messages = weekly_messages * 4
    responses = round(monthly_messages * response_rate)
    calls = round(responses * call_rate)
    proposals = round(calls * proposal_rate)
    deals = round(proposals * deal_rate)

    return {
        "messages": monthly_messages,
        "responses": responses,
        "calls": calls,
        "proposals": proposals,
        "deals": deals,
    }


def build_monthly_targets(funnel, average_pilot_price):
    return {
        "pilots_target": funnel["deals"],
        "expected_revenue": funnel["deals"] * average_pilot_price,
        "cases_to_build": max(funnel["deals"], 1),
    }


def main():
    print("=== Практика День 28: Операционная система AI-практика ===")
    print("Задание: собрать недельный план, прогноз воронки и месячные цели.")

    weekly_plan = build_weekly_plan(
        outreach_per_day=6,
        calls_per_week=3,
        posts_per_week=2,
    )

    funnel = project_monthly_funnel(
        weekly_plan=weekly_plan,
        response_rate=0.2,
        call_rate=0.5,
        proposal_rate=0.5,
        deal_rate=0.4,
    )

    targets = build_monthly_targets(funnel, average_pilot_price=180000)

    print("\nНедельный план:")
    for key, value in weekly_plan.items():
        print(f"{key}: {value}")

    print("\nПрогноз месячной воронки:")
    for stage, value in funnel.items():
        print(f"{stage}: {value}")

    print("\nЦели на месяц:")
    for key, value in targets.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
