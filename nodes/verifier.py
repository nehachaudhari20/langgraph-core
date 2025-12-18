from state.agent_state import AgentState


def verifier_node(state: AgentState) -> dict:
    """
    Simple verification logic.
    """
    answer = state["answer"]

    verified = len(answer) > 50

    return {
        "verified": verified
    }
