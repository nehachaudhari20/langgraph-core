from state.agent_state import AgentState


def worker_node(state: AgentState) -> dict:
    """
    Produces an answer based on the plan.
    """
    plan = state["plan"]

    answer = f"This is an answer generated using the plan: {plan}"

    return {
        "answer": answer
    }
