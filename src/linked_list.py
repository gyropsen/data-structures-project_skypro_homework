class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is not None:
            self.head = Node(data, self.head)
        else:
            self.head = Node(data, None)
            self.tail = self.head

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.tail is not None:
            self.tail.next_node = Node(data, None)
            self.tail = self.tail.next_node
        else:
            self.tail = Node(data, None)
            self.head = self.tail

    def get_data_by_id(self, _id_: int):
        for node in self.to_list():
            try:
                if node["id"] == _id_:
                    return node

            except TypeError:
                print("Данные не являются словарем или в словаре нет id")

    def to_list(self):
        node = self.head
        lst = []
        while node:
            lst.append(node.__dict__["data"])
            node = node.next_node
        return lst

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ""
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()
