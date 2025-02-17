
from fastapi import FastAPI
from graph import agent
from pydantic import BaseModel

app = FastAPI()

class ChatInput(BaseModel):
    messages: str

@app.post("/chat")
async def chat(input: ChatInput):
    response = await agent.graph.ainvoke({"messages": [{"role": "user", "content": input.messages}]})
    return response["messages"][-1].content
    

