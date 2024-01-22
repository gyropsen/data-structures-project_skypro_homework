class Node:
    """Класс для узла очереди"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        self.length = []

    def is_empty(self):
        return len(self.length) == 0

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)

        if self.is_empty():
            self.head = self.tail = node

        else:
            tail = self.tail
            tail.next_node = node
            self.tail = node
        self.length.append(data)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.is_empty():
            return
        data = self.head.data
        self.head = self.head.next_node
        self.length.pop()
        if self.is_empty():
            self.tail = None
        return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.is_empty():
            return ""
        return f"{"\n".join(self.length)}"
