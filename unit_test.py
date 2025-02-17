#%%
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from graph import agent
import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_graph():
    result = await agent.graph.ainvoke({"messages": [{"role": "user", "content": "Hello"}]})
    assert result is not None



# %%
