
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from typing import Annotated
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv,find_dotenv
from pathlib import Path
import os
import sys

load_dotenv('C:\\Users\\Kisan\\langgraph_fastapi\\.env')
chat_model = ChatOpenAI(model = 'gpt-4o',
                                 temperature = 0)

class OverallSchema(TypedDict):
    messages: Annotated[list, add_messages]

class ChatAgent():
    def __init__(self):
        graph = StateGraph(OverallSchema)
        graph.add_node('llm_node',self.llm_node)
        graph.add_edge(START,'llm_node')
        graph.add_edge('llm_node',END)
        self.graph = graph.compile()
        
    async def llm_node(self,state:OverallSchema):
        response = await chat_model.ainvoke(state['messages'])
        return {'messages': response}
    
agent = ChatAgent()


