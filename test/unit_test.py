import sys
sys.path.insert(0,'C:\\Users\\Kisan\\langgraph_fastapi\\app')
from graph import agent
import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_graph():
    result = await agent.graph.ainvoke({"messages": [{"role": "user", "content": "Hello"}]})
    assert result is not None


