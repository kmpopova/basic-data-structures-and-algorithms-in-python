"""
Objective:
Create a Stack class using Python list as foundation.
"""

# __init__(self): Initializes an empty stack.
# Complexity O(1)
class Stack():
    def __init__(self):
        self.data = []



# push(self, item): Adds item to the top.
# Complexity O(1)
    def push(self, item):
        self.data.append(item)

    

# pop(self): Removes and returns the top item. Handle the empty stack case 
# (e.g., print an error and return None, or raise an Exception).
# Complexity O(1)
    def pop(self):
        if self.is_empty():
            print("The stack is empty!")
            return None
        else:
            return self.data.pop()



# is_empty(self): Returns True if the stack is empty, False otherwise.
# Complexity O(1)
    def is_empty(self):
        if self.data != []:
            return False
        else:
            return True




# (Optional) size(self): Returns the number of items.
# Complexity O(1), because of efficiency of Python in-built list class
    def size(self):
        return len(self.data)


# Returning the top item without removing it
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        else:
            return self.data[- 1]


    
if __name__ == "__main__":
    # Testing the functionality using strings as items
    my_stack = Stack()
    print(my_stack.data)
    my_data = "abcabc"
    my_data_2 = "cbacba"
    my_stack.push(my_data)
    my_stack.push(my_data)
    my_stack.push(my_data_2)
    print(my_stack.data)
    print(my_stack.is_empty())
    print(my_stack.size())
    print(my_stack.peek())
    print(my_stack.size())
    print(my_stack.pop())
    print(my_stack.size())
    print(my_stack.peek())
