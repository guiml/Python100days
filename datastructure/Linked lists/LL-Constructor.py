class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value): 
        new_node = Node(value)
        if self.length == 0:
             self.tail = new_node
             self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(4)

# print(my_linked_list.head.value)

my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(1)
my_linked_list.print_list()

print(f"Head = {my_linked_list.head.value}")
print(f"Tail = {my_linked_list.tail.value}")