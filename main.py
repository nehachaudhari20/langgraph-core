from graphs.human_in_loop_graph import build_human_in_loop_graph


if __name__ == "__main__":
    graph = build_human_in_loop_graph()

    state = {
        "question": "Explain LangGraph in simple terms",
        "plan": "",
        "answer": "",
        "verified": False,
        "attempts": 0
    }

    # First invocation (will pause)
    result = graph.invoke(state)

    # Handle human interrupt
    if "__interrupt__" in result:
        print("\n--- HUMAN INPUT REQUIRED ---")
        human_input = input("Approve answer? (yes/no): ")

        # ✅ Merge interrupt into existing state
        state = {
            **state,
            "__interrupt__": human_input
        }

        result = graph.invoke(state)

    print("\n=== FINAL STATE ===")
    for k, v in result.items():
        print(f"{k}: {v}")
