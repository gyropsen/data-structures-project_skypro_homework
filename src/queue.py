class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.head is None or self.tail is None:
            self.tail = self.head = Node(data, None)
            return
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return removed_data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        head = self.head
        data = []
        while head:
            if head.data:
                data.append(head.data)
                head = head.next_node
        return "\n".join(data)
