from state.agent_state import AgentState


def verifier_node(state: AgentState) -> dict:
    """
    Verifies whether the answer is acceptable.
    """
    answer = state["answer"]

    verified = len(answer) > 40  # simple check

    return {
        "verified": verified
    }
