from langgraph.graph import StateGraph, END
from state.agent_state import AgentState

from nodes.planner import planner_node
from nodes.worker import worker_node
from nodes.verifier import verifier_node


def build_linear_graph():
    graph = StateGraph(AgentState)

    # Register nodes
    graph.add_node("planner", planner_node)
    graph.add_node("worker", worker_node)
    graph.add_node("verifier", verifier_node)

    # Define execution flow
    graph.set_entry_point("planner")
    graph.add_edge("planner", "worker")
    graph.add_edge("worker", "verifier")
    graph.add_edge("verifier", END)

    return graph.compile()
