"""
An expanded version of a Linked List class, with tail attribute.
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
        self.tail = None
 
    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    # Supporting function: calculating the length of the LinkedList object
    def retrieve_length(self):        
        current = self.head
        length = 0

        if current != None:
            length = 1	
            while current.next != None:
                length += 1
                current = current.next
            return length

    

    def insert(self, index: int, data): 
            # Inserting new element before the element that 
            # currently has this index
            new_node = Node(data)
            
            if index < 0:
                print("Cannot insert: Index cannot be a negative.")

            elif index == 0:
                new_node.next = self.head
                self.head = new_node
                # if the llist was empty before this operation? Then reassign tail, too
                if self.tail == None:
                    self.tail = new_node
            else:
                current = self.head
                current_index = 0
                while current and current_index < index - 1:  # Stop at the node *before* the index
                    previous = current
                    current = current.next
                    current_index += 1
                if current == None:
                    previous.next = new_node
                    self.tail = new_node
                    
                    return
                
                new_node.next = current.next
                current.next = new_node


    def delete(self, position: int):
        # Deleting a node at a specified position
        # Complexity is O(n) as in worst case we traverse the whole llist
        

        # Edge case if position = 0 aka head is to be deleted.
        if position == 0:
            old_head = self.head

            # check if the llist is empty
            if old_head == None:
                print("Empty, nothing to delete.")
                return

            self.head = old_head.next
            if self.head == None:
                self.tail = None
            return

        # Otherwise we move to the required position
        current = self.head
        index = 0
        while index < position:
            previous = current
            current = current.next
            index += 1
            if current is None:
                print("Index out of bounds.")
                return
            
        # Now we link previous node directly to current.next node
        previous.next = current.next
        # If we are at the end of the list, updating tail
        if previous.next == None:
            self.tail = previous


    def search(self, data, returning="bool"):
        # Search for a node containing data in the llist
        # Complexity O(n) as in the worst case will traverse whole llist
        # By default, the method will return a True/False answer: item is found
        # or not found.
        # To return the item itself, set returning="data"


        current = self.head
        while current is not None:
            if current.data == data:
                return current.data if returning == "data" else True
            else:
                current = current.next
        return False

    def print_list(self):
        # Printing llist, item by item, each on new line
        # Complexity O(n) as we always traverse the whole llist
        current = self.head
        if current is None:
            print("List is empty.")
            return
        while current is not None:
            print(current.data)
            current = current.next
        
    
    def reverse(self):
        # Reversing a llist
        # Complexity O(n)

        # Edge case when llist provided is empty or 1-item long, return as is
        if self.head is None or self.head.next is None:
            return self
                
        # For non-empty or 1-item llist, do the following  
        
        self.tail = self.head
        current = self.head
        previous = None
        while current is not None:
            # save next node for the future step forward
            next_node = current.next

            # reverse pointer
            current.next = previous

            # make a step forward
            previous = current
            current = next_node

        # once the while loop is done, re-assign head
        # because now current=None, previous is the last non-None
        self.head = previous 


        # now return the llist
        return self

          
    
if __name__ == "__main__":
    # Create and fill a LinkedList.

    my_list = LinkedList()
    my_list.append(0)
    print("Tail:" + str(my_list.tail.data))
    print(my_list.head)
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    print(my_list.tail)
    my_list.append(5)
    
  
    # Test inserting an element
    my_list.insert(2, "Number 42")

    # Test the print_list() method
    my_list.print_list()

    # Test the search() method
    result = my_list.search("Number 42")
    print(result)
    result = my_list.search("Number 42", returning="data")
    print(result)    
    result = my_list.search("Number 43")
    print(result)

    # Test the delete() method
    # Delete existing position in the middle
    my_list.delete(2)
    my_list.print_list()

    # Delete first item
    my_list.delete(0)
    my_list.print_list()

    # Delete non-existing item
    my_list.delete(10)
    my_list.print_list()

    # Test reversing a list with items
    new_list = my_list.reverse()
    new_list.print_list()

    # Checking of tail is updating correctly upon insertion out of bounds
    new_list.insert(100, 24)
    print(f"New tail: {new_list.tail.data}")
    new_list.print_list()
    
    # Test the retrieve_length() function
    print("my_list has a length of " + str(my_list.retrieve_length()))

    # Test reversing an empty list
    empty_list = LinkedList()
    reversed_empty = empty_list.reverse()
    reversed_empty.print_list()

    # Test reversing a list with one node
    one_node_list = LinkedList()
    one_node_list.append(42)
    reversed_one_node = one_node_list.reverse()
    reversed_one_node.print_list()

