from graphs.linear_graph import build_linear_graph


if __name__ == "__main__":
    graph = build_linear_graph()

    initial_state = {
        "question": "What is LangGraph?",
        "plan": "",
        "answer": "",
        "verified": False,
    }

    final_state = graph.invoke(initial_state)

    print("\n=== FINAL STATE ===")
    for k, v in final_state.items():
        print(f"{k}: {v}")
