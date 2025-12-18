from state.agent_state import AgentState


def decision_node(state: AgentState) -> dict:
    """
    Decision node does NOT decide routing.
    It only exists so the graph has a step here.
    """
    return {}
