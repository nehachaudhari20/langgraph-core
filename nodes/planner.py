from state.agent_state import AgentState


def planner_node(state: AgentState) -> dict:
    """
    Turns a question into a simple plan.
    """
    question = state["question"]

    plan = f"Answer the question step by step: {question}"

    return {
        "plan": plan
    }
