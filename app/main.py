
from fastapi import FastAPI
from graph import agent
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class ChatInput(BaseModel):
    messages: str
    
@app.get("/")
def health_check():
    return {'health_check': 'OK'}

# @app.post("/chat")
# async def chat(input: ChatInput):
#     response = await agent.graph.ainvoke({"messages": [{"role": "user", "content": input.messages}]})
#     return response["messages"][-1].content

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    

