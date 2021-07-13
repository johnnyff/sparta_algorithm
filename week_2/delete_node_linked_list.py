class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

        return
    def get_node(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.data

    def add_node(self,index, value):
        new_node = Node(value)
        if (index==0):

            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.add_node(0,6)
linked_list.print_all()


