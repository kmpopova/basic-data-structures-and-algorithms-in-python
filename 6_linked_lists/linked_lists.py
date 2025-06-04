"""
Objective: Implement a singly linked list in Python.
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Node: " + str(self.data)

class LinkedList():
    def __init__(self):
        self.head = None

    def __str__(self):
        nodes_in_llist = []
        current = self.head
        if current != None:
            nodes_in_llist.append(str(current.data))
        while current.next != None:
            nodes_in_llist.append(str(current.next.data))
            current = current.next
        return str(nodes_in_llist)


    def append(self, data):

        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node


    # Supporting function: calculating the length of the LinkedList object
    def retrieve_length(self):
        
        current = self.head
        self.length = 0
        if current != None:
            self.length = 1	
            while current.next != None:
                self.length += 1
                current = current.next
            return self.length


    def insert(self, index, data):
        # Let's say indexing in my LinkedList starts at 0
        # Inserting new element before the element that currently has this index
        new_node = Node(data)
        
        if index == 0:
            if self.head == None:
                self.head = new_node
           	
            else:
               next_node = self.head
               self.head = new_node
               new_node.next = next_node
               
        elif index > self.retrieve_length():
            self.append(data)
         
        else:
            current = self.head
            for i in range(index):
                previous = current
                current = current.next
            previous.next = new_node
            new_node.next = current


if __name__ == "__main__":

    # Testing :

    my_node = Node(5)
    print(my_node.data)
    print(my_node)
    print(my_node.data)

    my_list_1 = LinkedList()
    my_list_2 = LinkedList()


    my_list_2.append(Node(10))
    print(my_list_2.retrieve_length())
    my_list_2.append(my_node)
    print(my_list_2.head.data)
    print(my_list_2.retrieve_length())

    my_list_2.append(Node(20))
    print(my_list_2.retrieve_length())
    my_list_2.append(Node(30))
    print(my_list_2.retrieve_length())
    my_list_2.insert(0, Node(8))
    print(my_list_2.retrieve_length())
    print(my_list_2)
