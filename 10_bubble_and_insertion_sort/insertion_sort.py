"""
TASK: Implement a Python function insertion_sort(data_list) that 
sorts the given list in-place using the Insertion Sort algorithm.
"""

import random
from time import time
from bubble_sort import bubble_sort

def insertion_sort(data_list: list) -> list:
# Implements Insertion Sort algorithm

    n = len(data_list)

    for i in range(1, n):
        key = data_list[i]

        # Assume that everything up to key is sorted
        # Only walk through the preceding fragment 
        # if key is smaller than its preceding item

        j = i-1
        while j >= 0 and key < data_list[j]:
            
            data_list[j+1] = data_list[j]
            j -= 1
        data_list[j+1] = key
        
    
    return data_list

def print_list_with_highlight(input_list, index_1, index_2):
    display = []
    for i , value in enumerate(input_list):
        if i == index_1 or i == index_2:
            display.append(f"[{value}]")
        else:
            display.append(f"{value}")
    print(" ".join(display))


if __name__ == "__main__":

    # Testing different scenarios
    test_list = []
    print(test_list)
    sorted_test_list = insertion_sort(test_list)
    print(sorted_test_list)


    test_list = [5]
    print(test_list)
    sorted_test_list = insertion_sort(test_list)
    print(sorted_test_list)

    test_list = [1,2,3,4,5]
    print(test_list)
    sorted_test_list = insertion_sort(test_list)
    print(sorted_test_list)

    test_list = [2,1,3,4,5]
    print(test_list)
    sorted_test_list = insertion_sort(test_list)
    print(sorted_test_list)

    test_list = [1,2,3,5,4]
    print(test_list)
    sorted_test_list = insertion_sort(test_list)
    print(sorted_test_list)

    test_list = [5,4,3,2,1]
    print(test_list)
    sorted_test_list = insertion_sort(test_list)
    print(sorted_test_list)

    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(test_list)
    sorted_test_list = insertion_sort(test_list)
    print(sorted_test_list)

    test_list = [random.randint(1, 100) for _ in range(10)]
    print(test_list)
    sorted_test_list = insertion_sort(test_list)
    print(sorted_test_list)

    test_list = [random.randint(1, 10000) for _ in range(10000)]
    
    time_start = time()
    sorted_test_list_1 = insertion_sort(test_list.copy())
    time_finish = time()
    print(f"Insertion Sort took {(time_finish - time_start)*1000} ms to complete.")

    time_start = time()
    sorted_test_list_2 = bubble_sort(test_list.copy())
    time_finish = time()
    print(f"Bubble Sort took {(time_finish - time_start)*1000} ms to complete.")
    
    