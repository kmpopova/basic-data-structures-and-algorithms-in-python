"""
Objectives:

1. Implement a Python function linear_search(data_list, target) that takes a list and a target value. It should return the index of the first occurrence of the target if found, otherwise return None.
2. Implement a Python function binary_search(sorted_data_list, target) that takes a sorted list and 
a target value. It should return the index of the target if found, otherwise return None. 

"""
# Time complexity: O(n)
def linear_search(data, target):
    """ Accepts data in formats: list, tuple, string, aka ordered Python iterables."""
    # Check if data type given is acceptable
    if type(data) not in [list, tuple, str]:
        print("Wrong input data format. Accepted types: list, tuple, string.")
        return None
    else:
        # Include cases where we are looking e.g. for a number in a string.
        if type(data) == str:
            target = str(target)

        return data.index(target) if target in data else None

# Time complexity: O(n)
def linear_search_explicit(data, target):
    """ Accepts data in formats: list, tuple, string, aka ordered Python iterables."""
    
    if type(data) not in [list, tuple, str]:
        print("Wrong input data format. Accepted types: list, tuple, string.")
        return None
    else:
        # Include cases where we are looking e.g. for a number in a string.
        if type(data) == str:
            target = str(target)

        index = -1
        for item in data:
            index += 1
            if item == target:
                return index
        return None
        
# Time complexity: O(log(n))        
def binary_search(data, target):
    """ Accepts data: list, str.
        Would work for a number or string in an ordered list, since < and > operations work."""
    
    low = 0     # Index of first item
    high = len(data) - 1    # Index of last item
    
    while low <= high:

        middle = low + (high - low) // 2

        if data[middle] == target:
            return middle
        elif data[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    
    return None
        
if __name__== "__main__":

    # Testing linear_search() and linear_search_explicit():
    data = (2, 5, 4, 7, 9)
    #data = "hdgafk5"
    index = data.index(5)
    print(index)
    print(linear_search(data, 5))
    print(linear_search_explicit(data, 5))
    print(linear_search(data, 10))
    print(linear_search_explicit(data, 10))
    data = {3, 5, 2, 5, 7}
    print(linear_search(data, 5))
    print(linear_search_explicit(data, 5))

    # Testing binary_search()
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 20]
    print(binary_search(data, 20))
    print(binary_search(data, 1))
    print(binary_search(data, 3))
    print(binary_search(data, 9))
    print(binary_search(data, 40))