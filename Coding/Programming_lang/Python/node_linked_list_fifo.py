class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            self.tail  = new_node                                                                                                                                                              


        # new_node = Node(data)
        # new_node.next = self.head
        # self.head = new_node

    def print_All(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end= " ")
            temp = temp.next

lllist = LinkedList()

lllist.push(1)
lllist.push(2)
lllist.push(3)

lllist.print_All()
print()
print(lllist.head.data)
print(lllist.tail.data)