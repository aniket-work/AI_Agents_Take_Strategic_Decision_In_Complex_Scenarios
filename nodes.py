from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import OllamaLLM
from langchain_core.messages import AIMessage, HumanMessage, BaseMessage
from typing import List, Sequence
from utils import load_prompts, log_response, load_config

config = load_config()
prompts = load_prompts()

llm = OllamaLLM(model=config["model_name"])

# Properly creating the generation and reflection prompt templates
def get_generation_node():
    return ChatPromptTemplate.from_messages(
        [
            ("system", prompts["generation_prompt"]["system"]),
            MessagesPlaceholder(variable_name="messages")
        ]
    ) | llm

def get_reflection_node():
    return ChatPromptTemplate.from_messages(
        [
            ("system", prompts["reflection_prompt"]["system"]),
            MessagesPlaceholder(variable_name="messages")
        ]
    ) | llm

generate_prompt = get_generation_node()
reflect_prompt = get_reflection_node()

async def generation_node(state: Sequence[BaseMessage]):
    res = await generate_prompt.ainvoke({"messages": state})
    log_response(f"Generation: {res}")
    return res

async def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    cls_map = {"ai": HumanMessage, "human": AIMessage}
    translated = [messages[0]] + [
        cls_map[msg.type](content=msg.content) for msg in messages[1:]
    ]
    res = await reflect_prompt.ainvoke({"messages": translated})
    log_response(f"Reflection: {res}")
    return HumanMessage(content=res)
