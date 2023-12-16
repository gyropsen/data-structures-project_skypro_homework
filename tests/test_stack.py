"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest
from src.stack import Node, Stack


@pytest.fixture
def get_data():
    data = ["data1", "data2", "data3"]
    return data


def test_node(get_data):
    n1 = Node(get_data[0], get_data[1])
    n2 = Node(get_data[1], get_data[2])
    assert "data1" == n1.data
    assert "data2" == n2.data
    assert "data2" == n1.next_node
    assert "data3" == n2.next_node


def test_stack(get_data):
    stack = Stack()

    stack.push(get_data[0])
    assert stack.top.data == "data1"

    stack.push(get_data[1])
    assert stack.top.data == "data2"

    stack.push(get_data[2])
    assert stack.top.data == "data3"

    stack.pop()
    assert stack.top.data == "data2"

    stack.pop()
    assert stack.top.data == "data1"

    assert stack.pop() == "data1"
    assert stack.pop() is None
    assert stack.top is None
