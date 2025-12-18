from typing import TypedDict


class AgentState(TypedDict):
    """
    Shared state passed between LangGraph nodes.
    LangGraph reads and writes ONLY this object.
    """
    question: str
    plan: str
    answer: str
    verified: bool
