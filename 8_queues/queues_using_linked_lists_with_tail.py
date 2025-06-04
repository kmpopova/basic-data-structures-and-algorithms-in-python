from linked_lists_with_tail import LinkedList

class Queue():
    def __init__(self):
        self.data = LinkedList()
        
    # Complexity O(n), since need to traverse to end of llist
    # # Would need to write and use a doubly-linked list to make this operation O(1) 
    def enqueue(self, item):
        self.data.append(item)

    # Complexity O(1) since only making one step into the llist
    def dequeue(self):
        if self.data.head == None:
            print("Queue is empty, returning None.")
            return None
        else:
            first_in_line = self.data.head.data
            self.data.delete(0)
            return first_in_line
        
    # Complexity O(1)
    def peek(self):
        if self.data.head == None:
            print("Queue is empty, returning None.")
            return None
        else:
            return self.data.head.data
    
    # Complexity O(1)
    def is_empty(self):
        return self.data.head == None
    
    # Complexity O(n), traversing the whole llist
    # Will stay O(n) no matter if llist is single or double linked
    def size(self):
        return self.data.retrieve_length()

if __name__ == "__main__":
    my_queue = Queue()
    
    first_item = my_queue.dequeue()
    print(first_item)
    my_queue.enqueue(5)
    
    print(my_queue.peek())
    print(my_queue.is_empty())
    print(my_queue.size())
        
    first_item = my_queue.dequeue()
    print(first_item)
    print(my_queue.is_empty())
    print(my_queue.size())
    