import json

PROMPT_VERSION = "v1.0"

SYSTEM_PROMPT = (
    "Ты классификатор обращений в поддержку SaaS. "
    "Отвечай только JSON по схеме. "
    "Если категория неясна — возвращай 'unknown'. "
    "Никогда не придумывай поля."
)

USER_TEMPLATE = (
    "Текст обращения:\n"
    "{ticket}\n\n"
    "Верни JSON со следующими полями: category, priority, summary."
)

EXPECTED_SCHEMA = {
    "category": str,
    "priority": str,
    "summary": str,
}

VALID_CATEGORIES = {"billing", "bug", "feature", "auth", "unknown"}
VALID_PRIORITIES = {"low", "medium", "high"}


def build_system_prompt():
    return SYSTEM_PROMPT


def render_user_prompt(ticket):
    return USER_TEMPLATE.format(ticket=ticket)


def validate_structured_output(raw):
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        return {"valid": False, "error": f"невалидный JSON: {exc.msg}"}

    for field, expected_type in EXPECTED_SCHEMA.items():
        if field not in data:
            return {"valid": False, "error": f"нет поля {field}"}
        if not isinstance(data[field], expected_type):
            return {"valid": False, "error": f"неверный тип поля {field}"}

    if data["category"] not in VALID_CATEGORIES:
        return {"valid": False, "error": f"недопустимая категория: {data['category']}"}
    if data["priority"] not in VALID_PRIORITIES:
        return {"valid": False, "error": f"недопустимый приоритет: {data['priority']}"}

    return {"valid": True, "data": data}


def run_prompt_tests(cases):
    passed = 0
    results = []
    for index, case in enumerate(cases, start=1):
        result = validate_structured_output(case["response"])
        ok = result["valid"]
        if ok:
            passed += 1
        results.append({
            "index": index,
            "name": case["name"],
            "status": "OK" if ok else "FAIL",
            "error": result.get("error", ""),
        })
    return passed, results


def main():
    print("=== Практика День 30: Prompt engineering как код ===")
    print(f"Задание: проверить структурированный JSON-ответ модели. Версия промпта: {PROMPT_VERSION}")

    print(f"\nSystem prompt:\n{build_system_prompt()}")

    ticket = "Не приходит счёт на оплату за апрель, тариф Pro."
    print(f"\nUser prompt:\n{render_user_prompt(ticket)}")

    cases = [
        {
            "name": "корректный ответ",
            "response": '{"category": "billing", "priority": "high", "summary": "проблема со счётом"}',
        },
        {
            "name": "нет поля summary",
            "response": '{"category": "billing", "priority": "high"}',
        },
        {
            "name": "недопустимая категория",
            "response": '{"category": "spam", "priority": "low", "summary": "тест"}',
        },
        {
            "name": "не JSON",
            "response": "Это billing обращение, приоритет high.",
        },
    ]

    passed, results = run_prompt_tests(cases)
    print(f"\nРезультаты тестов ({passed}/{len(cases)} прошли):")
    for item in results:
        line = f"- кейс {item['index']} ({item['name']}): {item['status']}"
        if item["error"]:
            line += f" — {item['error']}"
        print(line)


if __name__ == "__main__":
    main()
