from langgraph.graph import StateGraph, END
from state.agent_state import AgentState

from nodes.planner import planner_node
from nodes.worker import worker_node
from nodes.verifier import verifier_node
from nodes.human import human_node


def build_human_in_loop_graph():
    graph = StateGraph(AgentState)

    # Register nodes
    graph.add_node("planner", planner_node)
    graph.add_node("worker", worker_node)
    graph.add_node("verifier", verifier_node)
    graph.add_node("human", human_node)

    # Flow
    graph.set_entry_point("planner")
    graph.add_edge("planner", "worker")
    graph.add_edge("worker", "verifier")
    graph.add_edge("verifier", "human")
    graph.add_edge("human", END)

    return graph.compile()
