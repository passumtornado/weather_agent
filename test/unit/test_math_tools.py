import pytest
from mcp_agent.servers.math.tools import add,divide,multiply,subtract

def test_add():
    assert add(10,5) == 15
def test_divide():
    assert divide(10,5) == 2
def test_multiply():
    assert multiply(10,5) == 50
def test_subtract():
    assert subtract(10,5) == 5
def test_divide_by_zero()->None:
    with pytest.raises(ValueError,match='divide by zero encountered'):
        divide(10,0)
