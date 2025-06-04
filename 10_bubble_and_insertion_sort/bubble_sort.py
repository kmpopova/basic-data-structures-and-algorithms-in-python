"""
Objective: 

Implement a Python function bubble_sort(data_list) that sorts 
the given list in-place (modifies the original list directly) using 
the Bubble Sort algorithm. 
Include the optimization to stop early if no swaps occur in a pass.

"""
import random

def bubble_sort(data_list: list) -> list:
    n = len(data_list)
    swap_occured = False
    i = n-1
    
    while i > 0:
        swap_occured = False

        for j in range(0, i):
            current_element = data_list[j]
            next_element = data_list[j+1]
            if current_element > next_element:
                data_list[j] = next_element
                data_list[j+1] = current_element
                swap_occured = True
        
        if swap_occured == False:
            
            return data_list
        i -= 1

    return data_list



if __name__ == "__main__":

    # Testing different scenarios
    test_list = []
    print(test_list)
    sorted_test_list = bubble_sort(test_list)
    print(sorted_test_list)


    test_list = [5]
    print(test_list)
    sorted_test_list = bubble_sort(test_list)
    print(sorted_test_list)

    test_list = [1,2,3,4,5]
    print(test_list)
    sorted_test_list = bubble_sort(test_list)
    print(sorted_test_list)

    test_list = [5,4,3,2,1]
    print(test_list)
    sorted_test_list = bubble_sort(test_list)
    print(sorted_test_list)

    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(test_list)
    sorted_test_list = bubble_sort(test_list)
    print(sorted_test_list)

    test_list = [random.randint(1, 100) for _ in range(10)]
    print(test_list)
    sorted_test_list = bubble_sort(test_list)
    print(sorted_test_list)