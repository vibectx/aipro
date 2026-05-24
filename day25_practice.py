DISCOVERY_QUESTIONS = [
    "Какой процесс отнимает у команды больше всего времени?",
    "Где сотрудники чаще всего ошибаются?",
    "Какие данные уже есть в текстовом виде?",
    "Что хотелось бы автоматизировать ещё год назад?",
    "По какой метрике поймёте, что решение работает?",
]


def summarize_call(answers):
    summary = {
        "main_pain": answers.get("main_pain"),
        "data_available": answers.get("data_available"),
        "success_metric": answers.get("success_metric"),
    }

    hypothesis = (
        f"AI может ускорить процесс '{summary['main_pain']}' "
        f"за счёт обработки данных '{summary['data_available']}' "
        f"с измерением по метрике '{summary['success_metric']}'."
    )

    next_step = "Подготовить короткий аудит и сценарий первого AI-прототипа."

    return {
        "summary": summary,
        "hypothesis": hypothesis,
        "next_step": next_step,
    }


def main():
    print("=== Практика День 25: Диагностический созвон ===")
    print("Задание: пройти по чек-листу вопросов и собрать резюме созвона.")

    print("\nЧек-лист вопросов:")
    for index, question in enumerate(DISCOVERY_QUESTIONS, start=1):
        print(f"{index}. {question}")

    answers = {
        "main_pain": "ручной разбор и маршрутизация входящих тикетов",
        "data_available": "архив тикетов и шаблоны ответов",
        "success_metric": "среднее время обработки тикета",
    }

    call_result = summarize_call(answers)

    print("\nРезюме созвона:")
    for key, value in call_result["summary"].items():
        print(f"{key}: {value}")

    print(f"\nГипотеза:\n{call_result['hypothesis']}")
    print(f"\nСледующий шаг:\n{call_result['next_step']}")


if __name__ == "__main__":
    main()
