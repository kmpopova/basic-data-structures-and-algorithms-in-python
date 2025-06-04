"""
Implementing Stacks using LinkedList() class previously created.
"""

from linked_lists import LinkedList

class Stack():
    def __init__(self):
        self.data = LinkedList()

    # Complexity O(1)
    def push(self, item):
        self.data.insert(0, item)

    # Complexity O(1)
    def pop(self):
        if self.data.head == None:
            print("Stack is empty! Nothing to pop.")
            return None
        else:
            top_of_stack = self.data.head.data
            self.data.delete(0)
            return top_of_stack
    
    # Complexity O(1)
    def peek(self):
        if self.data.head == None:
            print("Stack is empty! Nothing to pop.")
            return None
        else:
            top_of_stack = self.data.head.data
            return top_of_stack
    
    # Complexity O(1)
    def is_empty(self):
        if self.data.head == None:
            return True
        else:
            return False
    
    # Complexity O(n), have to loop over the whole llist
    def size(self):
        current = self.data.head
        length = 0
    
        while current is not None:
            length += 1
            current = current.next
        return length


    
if __name__ == "__main__":
    
    # Testing the functionality using strings as items
    my_stack = Stack()
    print(my_stack.data)
    my_stack.data.print_list()
    my_data = "abcabc"
    my_data_2 = "cbacba"
    my_stack.push(my_data)
    my_stack.push(my_data)
    my_stack.push(my_data_2)
    print(my_stack.data)
    my_stack.data.print_list()
    print(my_stack.is_empty())
    print(my_stack.size())
    print(my_stack.pop())