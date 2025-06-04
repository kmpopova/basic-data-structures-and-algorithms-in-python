"""
Objective: implement a Queue class and its functionalities using Python lists.
"""


class Queue():
    def __init__(self):
        self.data = []

    # Adding to end of queue.
    # Complexity O(1)
    def enqueue(self, item):
        self.data.append(item)

    # Removing an item from the front of queue
    # Complexity O(n), since items need to be shifted
    def dequeue(self):
        if self.data == []:
            print("Queue is empty, returning None.")
            return None
        else:
            element = self.data.pop(0)
            return element

    # Returning item currently at the front of queue without removing it
    # Complexity O(1)
    def peek(self):
        if self.data == []:
            print("Queue is empty, returning None.")
            return None
        else:
            return self.data[0]

    # Returning True or False, whether queue is empty or not
    # Complexity O(1), utilising efficient implementation of len(list) in Python
    def is_empty(self):
        return len(self.data) == 0


    # Optional 
    # Returning number of elements in queue
    # Complexity O(1) due to efficient Python list implementation
    def size(self):
        return len(self.data)
    
    # Optional
    # Adding item to front of the line
    # Complexity O(n), since items need to be shifted upon reversing
    def enqueue_to_front(self, item):
        self.data.reverse()
        self.data.append(item)
        self.data.reverse()
        
    
    # Optional
    # Removing and returning item that is last in queue
    # Complexity O(1)
    def dequeue_from_back(self):
        if self.data == []:
            print("Queue is empty, returning None.")
        else:
            return self.data.pop()


if __name__ =="__main__":
    my_queue = Queue()
    print(my_queue.data)
    first_item = my_queue.dequeue()
    print(first_item)
    my_queue.enqueue(5)
    print(my_queue.data)
    print(my_queue.peek())
    print(my_queue.is_empty())
    print(my_queue.size())
    last_item = my_queue.dequeue_from_back()
    print(last_item)
    my_queue.enqueue_to_front(42)
    print(my_queue.data)
    last_item = my_queue.dequeue_from_back()
    print(last_item)
    first_item = my_queue.dequeue()
    print(first_item)
    print(my_queue.is_empty())
    print(my_queue.size())