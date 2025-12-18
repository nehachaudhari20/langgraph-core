from langgraph.graph import StateGraph, END
from state.agent_state import AgentState

from nodes.planner import planner_node
from nodes.worker import worker_node
from nodes.verifier import verifier_node
from nodes.decision import decision_node


MAX_ATTEMPTS = 2


def route_after_decision(state: AgentState) -> str:
    if state["verified"]:
        return "end"

    if state["attempts"] >= MAX_ATTEMPTS:
        return "end"

    return "retry"


def build_retry_graph():
    graph = StateGraph(AgentState)

    # Register nodes
    graph.add_node("planner", planner_node)
    graph.add_node("worker", worker_node)
    graph.add_node("verifier", verifier_node)
    graph.add_node("decision", decision_node)

    # Entry point
    graph.set_entry_point("planner")

    # Main flow
    graph.add_edge("planner", "worker")
    graph.add_edge("worker", "verifier")
    graph.add_edge("verifier", "decision")

    # Conditional routing (CORRECT)
    graph.add_conditional_edges(
        "decision",
        route_after_decision,   # 👈 routing function
        {
            "retry": "worker",
            "end": END
        }
    )

    return graph.compile()
