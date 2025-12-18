from state.agent_state import AgentState


def worker_node(state: AgentState) -> dict:
    """
    Produces an answer based on the plan.
    """
    plan = state["plan"]
    attempts = state.get("attempts", 0) + 1

    answer = f"""
    Attempt {attempts}
    Answer generated using the plan:
    {plan}
    """

    return {
        "answer": answer,
        "attempts": attempts
    }
