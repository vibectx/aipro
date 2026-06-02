MODEL_PROFILE = {
    "premium": {"cost": 0.01, "latency_ms": 1500},
    "fast": {"cost": 0.0002, "latency_ms": 200},
}


class Metrics:
    def __init__(self):
        self.calls = 0
        self.errors = 0
        self.latencies = []
        self.cost_usd = 0.0
        self.fallbacks = 0

    def record_success(self, latency_ms, cost, fallback):
        self.calls += 1
        self.latencies.append(latency_ms)
        self.cost_usd += cost
        if fallback:
            self.fallbacks += 1

    def record_error(self):
        self.calls += 1
        self.errors += 1

    def report(self):
        if self.latencies:
            avg = sum(self.latencies) // len(self.latencies)
            ordered = sorted(self.latencies)
            p95_index = max(0, int(len(ordered) * 0.95) - 1)
            p95 = ordered[p95_index]
        else:
            avg = 0
            p95 = 0
        return {
            "calls": self.calls,
            "errors": self.errors,
            "error_rate": round(self.errors / max(self.calls, 1), 3),
            "avg_latency_ms": avg,
            "p95_latency_ms": p95,
            "cost_usd": round(self.cost_usd, 5),
            "fallbacks": self.fallbacks,
        }


def call_llm(prompt, model, fail_modes):
    if "timeout" in fail_modes:
        raise TimeoutError("LLM timeout")
    if "overloaded" in fail_modes and model == "premium":
        raise RuntimeError("model overloaded")
    profile = MODEL_PROFILE[model]
    return {
        "text": f"ответ модели {model} на: {prompt[:30]}",
        "cost": profile["cost"],
        "latency_ms": profile["latency_ms"],
    }


def llm_with_retry_and_fallback(prompt, primary="premium", fallback="fast", retries=2, fail_modes=None):
    fail_modes = fail_modes or []
    last_error = None
    for attempt in range(retries):
        try:
            response = call_llm(prompt, primary, fail_modes)
            return {**response, "model": primary, "fallback_used": False, "attempts": attempt + 1}
        except Exception as exc:
            last_error = exc
    try:
        response = call_llm(prompt, fallback, fail_modes)
        return {**response, "model": fallback, "fallback_used": True, "attempts": retries + 1}
    except Exception as exc:
        return {"error": str(exc) or str(last_error), "attempts": retries + 1}


def handle_request(prompt, metrics, fail_modes=None):
    result = llm_with_retry_and_fallback(prompt, fail_modes=fail_modes)
    if "error" in result:
        metrics.record_error()
        return {"ok": False, "error": result["error"]}
    metrics.record_success(result["latency_ms"], result["cost"], result["fallback_used"])
    return {"ok": True, "text": result["text"], "model": result["model"]}


def main():
    print("=== Практика День 35: Продакшен-обвес AI-сервиса ===")
    print("Задание: прогнать запросы через retry, fallback и собрать метрики.")

    metrics = Metrics()
    requests = [
        {"prompt": "обычный запрос 1", "fail_modes": []},
        {"prompt": "перегруз premium", "fail_modes": ["overloaded"]},
        {"prompt": "обычный запрос 2", "fail_modes": []},
        {"prompt": "тотальный сбой", "fail_modes": ["timeout"]},
        {"prompt": "обычный запрос 3", "fail_modes": []},
        {"prompt": "перегруз premium снова", "fail_modes": ["overloaded"]},
    ]

    print(f"\nОбработка {len(requests)} запросов:")
    for index, req in enumerate(requests, start=1):
        result = handle_request(req["prompt"], metrics, fail_modes=req["fail_modes"])
        if result["ok"]:
            print(f"  {index}. OK model={result['model']}")
        else:
            print(f"  {index}. ERROR: {result['error']}")

    print("\nМетрики сервиса:")
    for key, value in metrics.report().items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
