"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import pytest
from src.queue import Node, Queue


@pytest.fixture
def get_queue():
    return Queue()


@pytest.fixture
def get_node():
    return Node("data1")


def test_node(get_node):
    assert "data1" == get_node.data
    assert None is get_node.next_node


def test_enqueue(get_queue):
    get_queue.enqueue('data1')
    get_queue.enqueue('data2')
    get_queue.enqueue('data3')
    assert get_queue.head.data == 'data1'
    assert get_queue.head.next_node.data == 'data2'
    assert get_queue.tail.data == 'data3'
    assert get_queue.tail.next_node is None


def test_dequeue(get_queue):
    get_queue.enqueue('data1')
    get_queue.enqueue('data2')
    get_queue.enqueue('data3')
    assert get_queue.dequeue() == 'data1'
    assert get_queue.dequeue() == 'data2'
    assert get_queue.dequeue() == 'data3'
    assert get_queue.dequeue() is None


def test_str(get_queue):
    assert str(Queue()) == ""

    get_queue.enqueue('data1')
    get_queue.enqueue('data2')
    get_queue.enqueue('data3')

    assert str(get_queue) == "data1\ndata2\ndata3"
