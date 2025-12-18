from graphs.retry_graph import build_retry_graph


if __name__ == "__main__":
    graph = build_retry_graph()

    initial_state = {
        "question": "What is LangGraph?",
        "plan": "",
        "answer": "",
        "verified": False,
        "attempts": 0
    }

    final_state = graph.invoke(initial_state)

    print("\n=== FINAL STATE ===")
    for k, v in final_state.items():
        print(f"{k}: {v}")
