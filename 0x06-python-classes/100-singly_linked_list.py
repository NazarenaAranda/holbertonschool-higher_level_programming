#!/usr/bin/python3
class Node:
    """ class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeErorr('data must be an integer')
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """class SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            tmp = self.__head
            if value < tmp.data:
                self.__head = Node(value, self.__head)
                return
            while tmp.next_node and value > tmp.next_node.data:
                tmp = tmp.next_node
            tmp.next_node = Node(value, tmp.next_node)

    def __str__(self):
        stri = ""
        tmp = self.__head
        while tmp:
            stri += str(tmp.data)
            stri += '\n'
            tmp = tmp.next_node
        return stri[:-1]
