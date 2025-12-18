from state.agent_state import AgentState
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv() 

# Initialize Gemini once (outside node)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

def planner_node(state: AgentState) -> dict:
    """
    Uses Gemini to generate a plan for answering the question.
    """
    question = state["question"]

    prompt = f"""
    You are a planner.
    Given the question below, create a short step-by-step plan.

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return {
        "plan": response.content
    }
