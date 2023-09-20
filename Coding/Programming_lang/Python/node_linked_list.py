class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def push(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def print_All(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

lllist = LinkedList()

lllist.push(1)
lllist.push(2)
lllist.push(3)

lllist.print_All()
print()
print(lllist.head.value)
print(lllist.tail.value)
