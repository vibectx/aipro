ORDERS = {
    "A100": {"status": "доставлено", "amount": 2500},
    "A101": {"status": "в пути", "amount": 4200},
    "A102": {"status": "ожидает оплаты", "amount": 1800},
}

KNOWLEDGE = {
    "возврат": "Возврат оформляется в течение 14 дней через поддержку.",
    "доставка": "Срок доставки — 2-5 рабочих дней.",
    "оплата": "Оплата принимается картой и через СБП.",
}


def tool_get_order_status(params):
    order_id = params.get("order_id")
    if order_id and order_id in ORDERS:
        return {"ok": True, "data": ORDERS[order_id]}
    return {"ok": False, "error": f"заказ {order_id} не найден"}


def tool_search_knowledge(params):
    keyword = params.get("keyword", "").lower()
    for term, answer in KNOWLEDGE.items():
        if term in keyword:
            return {"ok": True, "data": answer}
    return {"ok": False, "error": "по запросу ничего не найдено"}


def tool_escalate_to_operator(params):
    reason = params.get("reason", "не указано")
    return {"ok": True, "data": f"тикет создан для оператора, причина: {reason}"}


TOOLS = {
    "get_order_status": {
        "fn": tool_get_order_status,
        "schema": {"order_id": "строка вида A100"},
    },
    "search_knowledge": {
        "fn": tool_search_knowledge,
        "schema": {"keyword": "ключевое слово из вопроса"},
    },
    "escalate_to_operator": {
        "fn": tool_escalate_to_operator,
        "schema": {"reason": "краткое описание проблемы"},
    },
}


def extract_order_id(text):
    for word in text.split():
        candidate = word.strip(".,!?").upper()
        if len(candidate) >= 2 and candidate[0] == "A" and candidate[1:].isdigit():
            return candidate
    return None


def plan_action(user_query):
    query = user_query.lower()
    if any(word in query for word in ["статус", "заказ", "где"]):
        return {
            "tool": "get_order_status",
            "params": {"order_id": extract_order_id(user_query)},
        }
    if any(word in query for word in ["возврат", "доставка", "оплата", "правил"]):
        return {"tool": "search_knowledge", "params": {"keyword": query}}
    return {"tool": "escalate_to_operator", "params": {"reason": user_query}}


def run_agent(user_query, max_steps=2):
    log = []
    for step in range(max_steps):
        action = plan_action(user_query)
        tool_name = action["tool"]
        result = TOOLS[tool_name]["fn"](action["params"])
        log.append({
            "step": step + 1,
            "tool": tool_name,
            "params": action["params"],
            "ok": result["ok"],
        })
        if result["ok"]:
            return {"answer": result["data"], "log": log}
        if tool_name == "escalate_to_operator":
            break
        user_query = f"проблема не решена: {user_query}"
    fallback = tool_escalate_to_operator({"reason": user_query})
    log.append({
        "step": len(log) + 1,
        "tool": "escalate_to_operator",
        "params": {"reason": user_query},
        "ok": fallback["ok"],
    })
    return {"answer": fallback["data"], "log": log}


def main():
    print("=== Практика День 33: AI-агент и tool calling ===")
    print("Задание: разобрать запрос пользователя, выбрать инструмент и вернуть ответ.")

    queries = [
        "где мой заказ A101",
        "какие правила возврата",
        "у меня списали деньги дважды",
        "статус заказа A999",
    ]

    for query in queries:
        print(f"\nЗапрос: {query}")
        result = run_agent(query)
        for step in result["log"]:
            print(f"  step {step['step']}: tool={step['tool']} params={step['params']} ok={step['ok']}")
        print(f"Ответ: {result['answer']}")


if __name__ == "__main__":
    main()
