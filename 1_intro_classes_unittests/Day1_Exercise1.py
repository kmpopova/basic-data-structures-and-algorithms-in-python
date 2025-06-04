"""
Hands-on - Function Practice (45-60 minutes):
Task: Write a Python function called process_numbers that takes a list of numbers 
as input and returns a dictionary containing:
"sum_even": The sum of all even numbers in the list.
"product_odd": The product of all odd numbers in the list.
"count_positives": The number of positive numbers in the list.
"count_negatives": The number of negative numbers in the list.
"count_zeros": The number of zeros in the list.

Example:
numbers = [1, 2, 3, 4, -1, 0, 5, -2]
result = process_numbers(numbers)
print(result)

# Expected Output: {'sum_even': 6, 'product_odd': 15, 'count_positives': 5, 'count_negatives': 2, 'count_zeros': 1}
"""

import math
import random

def process_numbers(numbers: list) -> dict:
    result_dict = dict()

    sum_even = sum(num for num in numbers if num%2 == 0)
    result_dict['sum_even'] = sum_even

    product_odd = (lambda num: math.prod([num for num in numbers if num%2 == 1]) \
        if len([num for num in numbers if num%2 == 1]) > 0 else 0)(numbers)
    result_dict['product_odd'] = product_odd

    count_positives = len([num for num in numbers if num > 0])
    result_dict['count_positives'] = count_positives

    count_negatives = len([num for num in numbers if num < 0])
    result_dict['count_negatives'] = count_negatives

    count_zeros = numbers.count(0)
    result_dict['count_zeros'] = count_zeros

    return result_dict

if __name__ == "__main__":
    
    input = [random.randint(-100, 100) for i in range(20)]
    
    print(input)
    print(process_numbers(input))