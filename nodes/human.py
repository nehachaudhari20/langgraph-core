from langgraph.types import interrupt
from state.agent_state import AgentState


def human_node(state: AgentState) -> dict:
    """
    Pauses execution and asks a human for approval.
    """
    approval = interrupt(
        {
            "question": "Do you approve this answer?",
            "answer": state["answer"]
        }
    )

    approved = approval.lower() in ["yes", "y"]

    return {
        "verified": approved
    }
