import asyncio

from langgraph.constants import END
from langgraph.graph import MessageGraph
from langchain_core.messages import HumanMessage
from nodes import generation_node, reflection_node
from constants import MAX_ITERATIONS
from utils import load_config

config = load_config()

builder = MessageGraph()
builder.add_node("generate", generation_node)
builder.add_node("reflect", reflection_node)
builder.set_entry_point("generate")


def should_continue(state):
    return END if len(state) > MAX_ITERATIONS else "reflect"


builder.add_conditional_edges("generate", should_continue)
builder.add_edge("reflect", "generate")


async def run_ai_agent():
    graph = builder.compile()
    async for event in graph.astream(
        [HumanMessage(content=f"Analyze {config['scenario']}")], config
    ):
        print(event)
        print("---")

if __name__ == "__main__":
    asyncio.run(run_ai_agent())
