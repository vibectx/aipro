MODEL_COSTS = {
    "fast": 0.0001,
    "balanced": 0.001,
    "premium": 0.01,
}

MODEL_LATENCY_MS = {
    "fast": 200,
    "balanced": 800,
    "premium": 2500,
}


class ResponseCache:
    def __init__(self):
        self.store = {}
        self.hits = 0
        self.misses = 0

    def get(self, key):
        if key in self.store:
            self.hits += 1
            return self.store[key]
        self.misses += 1
        return None

    def set(self, key, value):
        self.store[key] = value


def classify_complexity(query):
    text = query.lower()
    if "сравни" in text or "проанализируй" in text or "стратегия" in text:
        return "complex"
    if len(query) < 40:
        return "simple"
    return "medium"


def route_model(complexity):
    return {
        "simple": "fast",
        "medium": "balanced",
        "complex": "premium",
    }[complexity]


def handle_query(query, cache):
    cached = cache.get(query)
    if cached:
        return {**cached, "from_cache": True}

    complexity = classify_complexity(query)
    model = route_model(complexity)

    response = {
        "model": model,
        "cost": MODEL_COSTS[model],
        "latency_ms": MODEL_LATENCY_MS[model],
        "from_cache": False,
    }
    cache.set(query, response)
    return response


def main():
    print("=== Практика День 34: Кеш и роутер моделей ===")
    print("Задание: пропустить поток запросов через кеш и роутер, посчитать экономику.")

    queries = [
        "Какой статус заказа?",
        "Сравни тарифы Pro и Business по выгоде для команды из 10 человек.",
        "Какой статус заказа?",
        "Где счёт?",
        "Проанализируй динамику оттока за последние 3 месяца.",
        "Где счёт?",
        "Какой статус заказа?",
    ]

    cache = ResponseCache()
    real_cost = 0.0
    real_latency = 0
    naive_cost = 0.0
    naive_latency = 0

    print(f"\nОбработка {len(queries)} запросов:")
    for index, query in enumerate(queries, start=1):
        result = handle_query(query, cache)
        tag = "cache" if result["from_cache"] else result["model"]
        print(f"  {index}. [{tag}] cost={result['cost']} latency={result['latency_ms']}ms")
        if not result["from_cache"]:
            real_cost += result["cost"]
            real_latency += result["latency_ms"]
        naive_cost += MODEL_COSTS["premium"]
        naive_latency += MODEL_LATENCY_MS["premium"]

    print("\nИтого с кешем и роутером:")
    print(f"  стоимость: {round(real_cost, 5)} USD")
    print(f"  суммарная латентность LLM-вызовов: {real_latency} ms")
    print(f"  cache hits: {cache.hits}, misses: {cache.misses}")

    print("\nЕсли бы всё шло через premium без кеша:")
    print(f"  стоимость: {round(naive_cost, 5)} USD")
    print(f"  суммарная латентность: {naive_latency} ms")

    print("\nЭкономия:")
    print(f"  по стоимости: {round(naive_cost - real_cost, 5)} USD")
    print(f"  по латентности: {naive_latency - real_latency} ms")


if __name__ == "__main__":
    main()
