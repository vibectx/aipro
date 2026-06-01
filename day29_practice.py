MODELS = {
    "gpt-4o": {"price_in": 0.0025, "price_out": 0.01},
    "gpt-4o-mini": {"price_in": 0.00015, "price_out": 0.0006},
    "claude-haiku": {"price_in": 0.0008, "price_out": 0.004},
}


def estimate_tokens(text):
    return max(1, len(text) // 4)


def estimate_request_cost(model, tokens_in, tokens_out):
    price = MODELS[model]
    return round(
        (tokens_in / 1000) * price["price_in"] + (tokens_out / 1000) * price["price_out"],
        6,
    )


def choose_cheapest_model(tokens_in, tokens_out, max_cost):
    affordable = []
    for name in MODELS:
        cost = estimate_request_cost(name, tokens_in, tokens_out)
        if cost <= max_cost:
            affordable.append((name, cost))
    affordable.sort(key=lambda item: item[1])
    return affordable[0] if affordable else None


def build_request(model, system_prompt, user_prompt, temperature=0.2, max_tokens=500):
    return {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }


def main():
    print("=== Практика День 29: LLM API — токены и стоимость ===")
    print("Задание: оценить токены, стоимость запроса и подобрать модель под бюджет.")

    system_prompt = "Ты помощник оператора поддержки SaaS."
    user_prompt = "Кратко перескажи входящий тикет клиента в 2 предложениях."

    tokens_in = estimate_tokens(system_prompt + user_prompt) + 500
    tokens_out = 200

    print(f"\nОценка входящих токенов: {tokens_in}")
    print(f"Оценка исходящих токенов: {tokens_out}")

    print("\nСтоимость по моделям (за 1 запрос, USD):")
    for model in MODELS:
        cost = estimate_request_cost(model, tokens_in, tokens_out)
        print(f"- {model}: {cost}")

    pick = choose_cheapest_model(tokens_in, tokens_out, max_cost=0.01)
    if pick:
        print(f"\nСамая дешёвая модель под бюджет 0.01 USD: {pick[0]} (стоимость: {pick[1]})")
    else:
        print("\nНи одна модель не укладывается в бюджет.")

    selected_model = pick[0] if pick else "gpt-4o-mini"
    request = build_request(selected_model, system_prompt, user_prompt)

    print("\nТело запроса:")
    for key, value in request.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
