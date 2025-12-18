from graphs.human_in_loop_graph import build_human_in_loop_graph


if __name__ == "__main__":
    graph = build_human_in_loop_graph()

    # Initial input ONLY once
    result = graph.invoke(
        {
            "question": "Explain LangGraph in simple terms",
            "plan": "",
            "answer": "",
            "verified": False,
            "attempts": 0
        },
        config={"configurable": {"thread_id": "session-1"}}
    )

    # Handle interrupt cleanly
    if "__interrupt__" in result:
        print("\n--- HUMAN INPUT REQUIRED ---")
        human_input = input("Approve answer? (yes/no): ")

        result = graph.invoke(
            {"__interrupt__": human_input},
            config={"configurable": {"thread_id": "session-1"}}
        )

    print("\n=== FINAL STATE ===")
    for k, v in result.items():
        print(f"{k}: {v}")
